import React from "react";
import PostsGrid from "./PostsGrid";
import { getAllPosts } from "@/service/posts";

const FeaturedPosts = async () => {
  const posts = await getAllPosts();
  return (
    <section className="my-4">
      <h2 className="text-2xl font-bold my-2">Feauterd Posts</h2>
      <PostsGrid posts={posts} />
    </section>
  );
};

export default FeaturedPosts;
