import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {IChatRequest, IChatResponse} from './agent.model';
import {Observable, of} from 'rxjs';

@Injectable({ providedIn: 'root' })
export class AgentService {
  private baseAddress = "http://localhost:8855";

  constructor(private httpClient: HttpClient) { }

  postMessage(request: IChatRequest, sessionId: string): Observable<IChatResponse> {
    return this.httpClient.post<IChatResponse>(`${this.baseAddress}/api/chat?session_id=${sessionId}`, request);
  }

  sendFeedback(request: IChatRequest, sessionId: string): void {
    // return this.httpClient.post<IChatResponse>(`${this.baseAddress}/api/chat/feedback?session_id=${sessionId}`, request);

    return;
  }
}
