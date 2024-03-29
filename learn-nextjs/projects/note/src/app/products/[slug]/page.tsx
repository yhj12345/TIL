import { getProduct, getProducts } from "@/app/api/products";
import { redirect } from "next/navigation";
import Image from "next/image";
import GoProductsButton from "@/components/GoProductsButton";

export const revalidate = 3;

type Props = {
  params: {
    slug: string;
  };
};

export default async function ProductPage({ params: { slug } }: Props) {
  // 서버 파일에 있는 데이터 중 해당 제품의 정보를 찾아서 그걸 보여줌
  const product = await getProduct(slug);

  if (!product) {
    redirect("/products");
  }
  return (
    <>
      <h1>{product?.name} 제품 설명 페이지</h1>
      <Image
        src={`/images/${product?.image}`}
        alt={product!.name}
        height={300}
        width={300}
      />
      <GoProductsButton />
    </>
  );
}

export async function generateStaticParams() {
  // 모든 제품의 페이지들을 미리 만들어 둘 수 있게 해줄거임(SSG)
  const products = await getProducts();
  return products.map((product) => ({
    slug: product.id,
  }));
}
