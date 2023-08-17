export type User = {
  id: number;
  name: string;
};

export type PaginationParams = {
  size: number;
  page: number;
};

export type InfiniteScrollOptions = {
  size: number;
  onSuccess?: () => void;
  onError?: () => void;
};

export interface PaginationResponse<T> {
  contents: T[];
  pageNumber: number;
  pageSize: number;
  totalPages: number;
  totalCount: number;
  isLastPage: boolean;
  isFirstPage: boolean;
}
