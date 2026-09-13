import { create } from "zustand";
import type { ReviewAnalysis } from "../types/review.types";

interface ReviewState {
  reviewText: string;
  lastAnalysis: ReviewAnalysis | null;

  setReviewText: (reviewText: string) => void;
  setLastAnalysis: (analysis: ReviewAnalysis | null) => void;
  clearReview: () => void;
}

export const useReviewStore = create<ReviewState>((set) => ({
  reviewText: "",
  lastAnalysis: null,

  setReviewText: (reviewText) => {
    set({ reviewText });
  },

  setLastAnalysis: (analysis) => {
    set({ lastAnalysis: analysis });
  },

  clearReview: () => {
    set({
      reviewText: "",
      lastAnalysis: null,
    });
  },
}));