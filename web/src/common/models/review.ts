import { NestedProduct } from './product';

export interface Review {
  uuid: string;
  review: string;
  created_at: string;
  updated_at: string;
  product: NestedProduct;
  user: string;
}
