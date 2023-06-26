import CarouselPosts from "@/components/CarouselPosts";
import FeaturedPosts from "@/components/FeaturedPosts";
import Hero from "@/components/Hero";

export default function HomePage() {
  return (
    <section>
      <Hero />
      <FeaturedPosts />
      <CarouselPosts />
    </section>
  );
}
