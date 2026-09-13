import type {
  ButtonHTMLAttributes,
  ReactNode,
} from "react";
import { LoadingSpinner } from "./LoadingSpinner";

interface ButtonProps
  extends ButtonHTMLAttributes<HTMLButtonElement> {
  children: ReactNode;
  loading?: boolean;
}

export function Button({
  children,
  loading = false,
  disabled,
  ...props
}: ButtonProps) {
  return (
    <button
      {...props}
      disabled={disabled || loading}
      className="button"
    >
      {loading && <LoadingSpinner />}
      {loading ? "Analyzing..." : children}
    </button>
  );
}