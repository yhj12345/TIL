"use client";

import { Post } from "@/service/posts";
import React, { useState } from "react";
import PostsGrid from "./PostsGrid";
import Categories from "./Categories";

type Props = {
  posts: Post[];
  categories: string[];
};

const ALL_POSTS = "All Posts";

const FilterablePosts = ({ posts, categories }: Props) => {
  const [seleted, setSelected] = useState(ALL_POSTS);
  const filteredPosts =
    seleted === ALL_POSTS
      ? posts
      : posts.filter((post) => post.category === seleted);

  return (
    <section>
      <PostsGrid posts={filteredPosts} />
      <Categories
        categories={[ALL_POSTS, ...categories]}
        selected={seleted}
        onClick={setSelected}
      />
    </section>
  );
};

export default FilterablePosts;
