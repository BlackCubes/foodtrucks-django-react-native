export interface Product {
  uuid: string;
  name: string;
  slug: string;
  info: string;
  image: string;
  price: number;
  quantity: number;
  is_available: boolean;
  truck: string;
  likes: Array<string | null>;
  reviews: Array<string | null>;
}
