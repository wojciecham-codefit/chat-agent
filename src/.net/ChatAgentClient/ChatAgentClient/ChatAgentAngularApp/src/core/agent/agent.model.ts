export interface IChatRequest {
  user_message: string;
}

export interface IChatResponse {
  session_id: string;
  llm_response: string;
  finish: boolean;
}
