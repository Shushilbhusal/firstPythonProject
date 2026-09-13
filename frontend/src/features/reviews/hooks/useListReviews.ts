import { useQuery } from "@tanstack/react-query";
import { listReviews } from "../api/reviewApi";

export function useListReviews() {
  return useQuery({
    queryKey: ["reviews"],
    queryFn: ({ signal }) => listReviews(signal),
  });
}