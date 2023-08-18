export interface User {
  id: number;
  name: string;
}

export interface PaginationParams {
  size: number;
  page: number;
}

export interface InfiniteScrollOptions {
  size: number;
  onSuccess?: () => void;
  onError?: () => void;
}

export interface PaginationResponse<T> {
  contents: T[];
  pageNumber: number;
  pageSize: number;
  totalPages: number;
  totalCount: number;
  isLastPage: boolean;
  isFirstPage: boolean;
}
