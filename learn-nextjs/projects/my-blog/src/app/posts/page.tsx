import FilterablePosts from "@/components/FilterablePosts";
import { getAllPosts } from "@/service/posts";
import React from "react";

const PostsPage = async () => {
  const posts = await getAllPosts();
  const categories = [...new Set(posts.map((post) => post.category))];
  return <FilterablePosts posts={posts} categories={categories} />;
};

export default PostsPage;
