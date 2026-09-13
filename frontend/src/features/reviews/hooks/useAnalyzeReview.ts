import { useMutation } from "@tanstack/react-query";
import { analyzeReview } from "../api/reviewApi";
import { useReviewStore } from "../stores/reviewStore";

export function useAnalyzeReview() {
  const setLastAnalysis = useReviewStore(
    (state) => state.setLastAnalysis,
  );

  return useMutation({
    mutationFn: analyzeReview,

    onSuccess: (data) => {
      setLastAnalysis(data);
    },
  });
}