import Link from "next/link";
const products = ["shirt", "pants", "skirt", "shoes"];

export default function ProductsPage() {
  return (
    <div>
      <h1>제품 소개 페이지!</h1>
      <ul>
        {products.map((product, index) => (
          <li key={index}>
            <Link href={`/products/${product}`}>{product}</Link>
          </li>
        ))}
      </ul>
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
