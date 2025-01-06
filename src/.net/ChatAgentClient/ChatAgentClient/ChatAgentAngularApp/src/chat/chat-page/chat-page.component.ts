import {AfterViewChecked, Component, ElementRef, model, signal, ViewChild} from '@angular/core';
import { MatFormField, MatLabel } from '@angular/material/form-field';
import { MatInput } from '@angular/material/input';
import { AgentService } from '../../core/agent/agent.service';
import { MatCard, MatCardContent, MatCardTitle } from '@angular/material/card';
import { ChatItem } from '../models/chat.model';
import { FormsModule } from '@angular/forms';
import {MatFabButton} from '@angular/material/button';
import {MatProgressBar} from '@angular/material/progress-bar';

@Component({
  selector: 'app-chat-page',
  imports: [
    MatFormField,
    MatInput,
    MatCard,
    MatCardContent,
    MatLabel,
    MatCardTitle,
    FormsModule,
    MatFabButton,
    MatProgressBar,
  ],
  templateUrl: './chat-page.component.html',
  standalone: true,
  styleUrl: './chat-page.component.scss'
})
export class ChatPageComponent implements AfterViewChecked {
  @ViewChild('chatContainer') private chatContainer!: ElementRef;
  isLoading = signal(false);
  finish = signal(false);
  sessionId = signal<string>('')
  chatMessages = signal<ChatItem[]>([]);
  message = model('');
  shouldSendFeedback = signal(false);
  disableChat = signal(false);

  constructor(private agentService: AgentService) {
    this.resetChat();
  }

  ngAfterViewChecked(): void {
    this.scrollToBottom();
  }

  private resetChat() {
    this.chatMessages.update((values) => {
      return [
        { isAgentResponse: true, content: 'Witam. W czym mogę Ci dzisiaj pomóc?', timestamp: Date.now() },
      ]
    });

    this.finish.set(false);
    this.disableChat.set(false);
    this.sessionId.set('')
    this.shouldSendFeedback.set(false);
    this.message.set('');
    this.isLoading.set(false);
  }

  restart(): void {
    this.resetChat()
  }

  scrollToBottom(): void {
    try {
      this.chatContainer.nativeElement.scrollTop = this.chatContainer.nativeElement.scrollHeight;
    } catch (err) {
      console.error('Scroll to bottom failed:', err);
    }
  }

  sendMessage(event: KeyboardEvent): void {
    if (event.key === 'Enter') {
      this.isLoading.set(true);

      const data = this.message();
      this.message.set('');

      this.chatMessages.update((values) => {
        return [
          ...values,
          { isAgentResponse: false, content: data, timestamp: Date.now() },
        ]
      });

      this.message.set('');

      if (this.finish()) {
        this.disableChat.set(true);

        //this.agentService.sendFeedback({ user_message: data }, this.sessionId());
          this.isLoading.set(false);

          this.chatMessages.update((values) => {
            return [
              ...values,
              { isAgentResponse: true, content: "Dziękujemy za feedback.", timestamp: Date.now() },
            ]
          });
        // });

        return;
      }

      this.agentService.postMessage({ user_message: data }, this.sessionId())
        .pipe()
        .subscribe((response) => {
          this.chatMessages.update((values) => {
            return [
              ...values,
              { isAgentResponse: true, content: response.llm_response, timestamp: Date.now() },
            ]
          });

          this.sessionId.set(response.session_id);

          if (response.finish) {
            this.finish.set(true);
          }

          this.isLoading.set(false);
          this.message.set('');
        });
    }
  }
}
