import axios from "axios";
import { api } from "../../../lib/axios";
import type {
  AnalyzeReviewRequest,
  ReviewAnalysis,
} from "../types/review.types";

function detailFrom(error: unknown): string | null {
  if (!axios.isAxiosError(error)) {
    return null;
  }

  const detail = error.response?.data?.detail;

  if (typeof detail === "string" && detail.trim()) {
    return detail;
  }

  if (Array.isArray(detail)) {
    return detail
      .map((item) => item?.msg ?? JSON.stringify(item))
      .join(", ");
  }

  return null;
}

export async function analyzeReview(
  data: AnalyzeReviewRequest,
): Promise<ReviewAnalysis> {
  try {
    const response = await api.post<ReviewAnalysis>(
      "/api/reviews/analyze",
      data,
    );

    console.log("Received response from analyzeReview:", response.data);

    return response.data;
  } catch (error) {
    const detail = detailFrom(error);

    if (detail) {
      throw new Error(detail, { cause: error });
    }

    if (axios.isAxiosError(error) && error.response?.status === 500) {
      throw new Error(
        "The server encountered an error while analyzing the review.",
        { cause: error },
      );
    }

    if (axios.isAxiosError(error) && !error.response) {
      throw new Error("Unable to connect to the backend.", {
        cause: error,
      });
    }

    throw new Error(
      "Something went wrong while analyzing the review.",
      { cause: error },
    );
  }
}

export async function listReviews(
  signal?: AbortSignal,
): Promise<ReviewAnalysis[]> {
  try {
    const response = await api.get<ReviewAnalysis[]>("/api/reviews", {
      signal,
    });
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error) && !error.response) {
      throw new Error("Unable to connect to the backend.", {
        cause: error,
      });
    }

    throw new Error("Could not load recent reviews.", {
      cause: error,
    });
  }
}