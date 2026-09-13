import type { Sentiment } from "../types/review.types";

interface SentimentBadgeProps {
  sentiment: Sentiment;
}

export function SentimentBadge({
  sentiment,
}: SentimentBadgeProps) {
  return (
    <span className={`sentiment sentiment-${sentiment}`}>
      {sentiment}
    </span>
  );
}