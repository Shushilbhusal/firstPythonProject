import { Header } from "../components/layout/Header";
import { PageContainer } from "../components/layout/PageContainer";
import { ErrorMessage } from "../components/common/ErrorMessage";
import { ReviewForm } from "../features/reviews/components/ReviewForm";
import { ReviewResult } from "../features/reviews/components/ReviewResult";
import { RecentReviews } from "../features/reviews/components/RecentReviews";
import { useAnalyzeReview } from "../features/reviews/hooks/useAnalyzeReview";

export function ReviewAnalyzerPage() {
  const analyzeMutation = useAnalyzeReview();

  const errorMessage =
    analyzeMutation.error instanceof Error
      ? analyzeMutation.error.message
      : null;

  return (
    <div>
      <Header />

      <PageContainer>
        {errorMessage && (
          <ErrorMessage message={errorMessage} />
        )}

        <ReviewForm />

        <ReviewResult />

        <RecentReviews />
      </PageContainer>
    </div>
  );
}