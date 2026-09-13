import { SentimentBadge } from "./SentimentBadge";
import { useListReviews } from "../hooks/useListReviews";
import { useReviewStore } from "../stores/reviewStore";

export function RecentReviews() {
  const { data: reviews, isLoading, isError } = useListReviews();
  const setLastAnalysis = useReviewStore(
    (state) => state.setLastAnalysis,
  );

  if (isLoading) {
    return (
      <section className="card">
        <div className="card-header">
          <h2>Recent analyses</h2>
        </div>
        <p className="empty-state-p">Loading recent reviews...</p>
      </section>
    );
  }

  if (isError || !reviews || reviews.length === 0) {
    return null;
  }

  return (
    <section className="card">
      <div className="card-header">
        <h2>Recent analyses</h2>
        <p>Click a review to view its full analysis.</p>
      </div>

      <ul className="recent-list">
        {reviews.map((review) => (
          <li key={review.id}>
            <button
              type="button"
              className="recent-item"
              onClick={() => setLastAnalysis(review)}
            >
              <SentimentBadge
                sentiment={review.sentiment ?? "neutral"}
              />

              <p className="recent-summary">{review.summary}</p>

              {review.created_at && (
                <span className="recent-date">
                  {new Date(review.created_at).toLocaleString()}
                </span>
              )}
            </button>
          </li>
        ))}
      </ul>
    </section>
  );
}