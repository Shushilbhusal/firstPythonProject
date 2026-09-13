import type { FormEvent } from "react";
import { Button } from "../../../components/common/Button";
import { useReviewStore } from "../stores/reviewStore";
import { useAnalyzeReview } from "../hooks/useAnalyzeReview";

export function ReviewForm() {
  const reviewText = useReviewStore(
    (state) => state.reviewText,
  );

  const setReviewText = useReviewStore(
    (state) => state.setReviewText,
  );

  const analyzeMutation = useAnalyzeReview();

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log("Submitting review for analysis:", reviewText);

    const trimmedReview = reviewText.trim();

    if (!trimmedReview) {
      return;
    }

    analyzeMutation.mutate({
      review_text: trimmedReview,
    });
  };

  return (
    <section className="card">
      <div className="card-header">
        <h2>Analyze a Customer Review</h2>
        <p>
          Enter a review and let Gemini analyze its
          sentiment, rating, topics, pros, and cons.
        </p>
      </div>

      <form onSubmit={handleSubmit}>
        <label htmlFor="review">
          Customer review
        </label>

        <textarea
          id="review"
          value={reviewText}
          onChange={(event) =>
            setReviewText(event.target.value)
          }
          placeholder="Example: The food was delicious, delivery was fast, but the packaging was poor."
          rows={8}
          maxLength={5000}
        />

        <div className="form-footer">
          <span className="character-count">
            {reviewText.length} / 5000
          </span>

          <Button
            type="submit"
            loading={analyzeMutation.isPending}
            disabled={!reviewText.trim()}
          >
            Analyze Review
          </Button>
        </div>
      </form>
    </section>
  );
}