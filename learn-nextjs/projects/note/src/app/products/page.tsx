import Link from "next/link";
import { getProducts } from "../api/products";
import MeowArticle from "@/components/MeowArticle";
import Image from "next/image";
import clothesImage from "../../../public/images/clothes.jpg";

// export const revalidate = 3

export default async function ProductsPage() {
  // 서버 파일(데이터베이스)에 있는 제품의 리스트를 읽어와서, 보여 줌
  const products = await getProducts();

  return (
    <div>
      <h1>제품 소개 페이지!</h1>
      <Image src={clothesImage} alt="Clothes" />
      <ul>
        {products.map((product, index) => (
          <li key={index}>
            <Link href={`/products/${product.id}`}>{product.name}</Link>
          </li>
        ))}
      </ul>

      <MeowArticle />
      {/* <ul>
        <li>
          <Link href="/products/shirt">shirt</Link>
        </li>
        <li>
          <Link href="/products/pants">pants</Link>
        </li>
        <li>
          <Link href="/products/skirt">skirt</Link>
        </li>
        <li>
          <Link href="/products/shoes">shoes</Link>
        </li>
      </ul> */}
    </div>
  );
}
