interface Product {
  id: number;
  name: string;
  price: number;
  brand: string;
  stock: number;
}

// const fetchProducts = (): Promise<Product[]> => {

// }

// interface ProductDetail {
//   id: number;
//   name: string;
//   price: number;
// }

type ShoppingItem = Pick<Product, 'id' | 'name' | 'price'>

const displayProductDetail = (shoppingItem: Pick<Product, 'id' | 'name' | 'price'>) => {

}