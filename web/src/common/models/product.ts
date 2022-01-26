import { NestedFoodtruck } from './foodtruck';

export interface Product {
  uuid: string;
  name: string;
  slug: string;
  info: string;
  image: string | null;
  price: number;
  quantity: number;
  is_available: boolean;
  truck: NestedFoodtruck;
}

export interface NestedProduct {
  uuid: string;
  name: string;
  slug: string;
  image: string | null;
}
