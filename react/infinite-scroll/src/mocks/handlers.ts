// src/mocks/handlers.js
import { rest } from "msw";
import { PaginationResponse, User } from "../models/user";

const users = Array.from(Array(1024).keys()).map(
  (id): User => ({
    id,
    name: `denis${id}`,
  })
);

export const handlers = [
  rest.get("/users", async (req, res, ctx) => {
    const { searchParams } = req.url;
    const size = Number(searchParams.get("size"));
    const page = Number(searchParams.get("page"));
    const totalCount = users.length;
    const totalPages = Math.round(totalCount / size);

    return res(
      ctx.status(200),
      ctx.json<PaginationResponse<User>>({
        contents: users.slice(page * size, (page + 1) * size),
        pageSize: size,
        pageNumber: page,
        totalPages,
        totalCount,
        isLastPage: totalPages <= page,
        isFirstPage: page === 0,
      }),
      ctx.delay(500)
    );
  }),
];
