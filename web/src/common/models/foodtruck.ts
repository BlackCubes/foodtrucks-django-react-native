type FoodtruckImage = {
  uuid: string;
  image: string;
  is_profile_image: boolean;
};

export interface Foodtruck {
  uuid: string;
  name: string;
  slug: string;
  info: string;
  phone_number: string;
  email: string;
  website: string;
  images: FoodtruckImage[] | [];
}

export interface NestedFoodtruck {
  uuid: string;
  name: string;
  slug: string;
  profile_image: string | null;
}
