import { useReviewStore } from "../stores/reviewStore";
import { SentimentBadge } from "./SentimentBadge";

export function ReviewResult() {
  const analysis = useReviewStore(
    (state) => state.lastAnalysis,
  );

  if (!analysis) {
    return (
      <section className="card empty-state">
        <h2>No analysis yet</h2>
        <p>
          Submit a customer review above to see the
          AI analysis.
        </p>
      </section>
    );
  }

  return (
    <section className="card">
      {analysis.saved === false && (
        <div className="info-message" role="status">
          Analysis complete, but the result could not be
          saved to the database.
        </div>
      )}

      <div className="result-header">
        <div>
          <p className="eyebrow">Analysis result</p>
          <h2>Review Analysis</h2>
        </div>

        <SentimentBadge sentiment={analysis.sentiment} />
      </div>

      <div className="rating">
        <span className="rating-number">
          {analysis.rating}
        </span>
        <span>/ 5</span>
      </div>

      <div className="result-section">
        <h3>Summary</h3>
        <p>{analysis.summary}</p>
      </div>

      <div className="result-grid">
        <div className="result-section">
          <h3>Topics</h3>

          <div className="tag-list">
            {analysis.topics.length > 0 ? (
              analysis.topics.map((topic) => (
                <span className="tag" key={topic}>
                  {topic}
                </span>
              ))
            ) : (
              <p>No topics found.</p>
            )}
          </div>
        </div>

        <div className="result-section">
          <h3>Pros</h3>

          {analysis.pros.length > 0 ? (
            <ul>
              {analysis.pros.map((pro) => (
                <li key={pro}>{pro}</li>
              ))}
            </ul>
          ) : (
            <p>No pros found.</p>
          )}
        </div>

        <div className="result-section">
          <h3>Cons</h3>

          {analysis.cons.length > 0 ? (
            <ul>
              {analysis.cons.map((con) => (
                <li key={con}>{con}</li>
              ))}
            </ul>
          ) : (
            <p>No cons found.</p>
          )}
        </div>
      </div>

      <div className="original-review">
        <h3>Original Review</h3>
        <p>{analysis.review_text}</p>
      </div>
    </section>
  );
}