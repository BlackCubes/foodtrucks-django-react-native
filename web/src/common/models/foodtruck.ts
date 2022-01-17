export interface Foodtruck {
  uuid: string;
  name: string;
  slug: string;
  info: string;
  phone_number: string;
  email: string;
  website: string;
  images: Array<string | null>;
  products: Array<string | null>;
  events: Array<string | null>;
}
