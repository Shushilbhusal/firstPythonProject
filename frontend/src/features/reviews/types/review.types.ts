export type Sentiment =
  | "positive"
  | "negative"
  | "neutral";

export interface AnalyzeReviewRequest {
  review_text: string;
}

export interface ReviewAnalysis {
  id?: number;
  review_text: string;
  rating: number;
  sentiment: Sentiment;
  summary: string;
  topics: string[];
  pros: string[];
  cons: string[];
  created_at?: string;
  saved?: boolean;
}