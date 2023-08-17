import React, { useCallback, useEffect, useState } from "react";
import {
  InfiniteScrollOptions,
  PaginationParams,
  PaginationResponse,
} from "../models/user";
import { AxiosResponse } from "axios";

const throttle = (handler: (...args: any[]) => void, timeout = 300) => {
  let invokedTime: number;
  let timer: number;
  return function (this: any, ...args: any[]) {
    if (!invokedTime) {
      handler.apply(this, args);
      invokedTime = Date.now();
    } else {
      clearTimeout(timer);
      timer = window.setTimeout(() => {
        if (Date.now() - invokedTime >= timeout) {
          handler.apply(this, args);
          invokedTime = Date.now();
        }
      }, Math.max(timeout - (Date.now() - invokedTime), 0));
    }
  };
};

const useThrottle = <T>(
  fetcher: (
    params: PaginationParams
  ) => Promise<AxiosResponse<PaginationResponse<T>>>,
  { size, onSuccess, onError }: InfiniteScrollOptions
) => {
  const [page, setPage] = useState(0);
  const [data, setData] = useState<T[]>([]);
  const [isFetching, setFetching] = useState(false);
  const [hasNextPage, setNextPage] = useState(true);

  const executeFetch = useCallback(async () => {
    try {
      const {
        data: { contents, pageNumber, isLastPage },
      } = await fetcher({ page, size });
      setData((prev) => prev.concat(contents));
      setPage(pageNumber + 1);
      setNextPage(!isLastPage);
      setFetching(false);
      onSuccess?.();
    } catch (err) {
      onError?.();
    }
  }, [page]);

  useEffect(() => {
    const handleScroll = throttle(() => {
      console.log("scroll event");
      const { scrollTop, offsetHeight } = document.documentElement;
      if (window.innerHeight + scrollTop >= offsetHeight) {
        setFetching(true);
      }
    });

    setFetching(true);
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  useEffect(() => {
    if (isFetching && hasNextPage) executeFetch();
    else if (!hasNextPage) setFetching(false);
  }, [isFetching]);

  return { page, data, isFetching, hasNextPage };
};

export default useThrottle;
