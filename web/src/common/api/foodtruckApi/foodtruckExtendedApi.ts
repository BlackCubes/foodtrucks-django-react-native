import coreSplitApi from './coreSplitApi';
import { Foodtruck, Product, Review, Social } from '../../models';

const foodtruckExtendedApi = coreSplitApi.injectEndpoints({
  endpoints: (builder) => ({
    getFoodtrucks: builder.query<Foodtruck[], void>({
      query: () => ({ url: '/foodtrucks' }),
      providesTags: ['Foodtruck'],
    }),

    getFoodtruckBySlug: builder.query<Foodtruck, string>({
      query: (slug) => ({ url: `/foodtrucks/${slug}` }),
      providesTags: ['Foodtruck'],
    }),

    getProductsByFoodtruckSlug: builder.query<Product[], string>({
      query: (slug) => ({ url: `/foodtrucks/${slug}/products` }),
      providesTags: ['Product'],
    }),

    getReviewsByFoodtruckSlug: builder.query<Review[], string>({
      query: (slug) => ({ url: `/foodtrucks/${slug}/reviews` }),
      providesTags: ['Review'],
    }),

    getSocialsByFoodtruckSlug: builder.query<Social[], string>({
      query: (slug) => ({ url: `/foodtrucks/${slug}/socials` }),
      providesTags: ['Social'],
    }),
  }),

  overrideExisting: false,
});

export const {
  useGetFoodtruckBySlugQuery,
  useGetFoodtrucksQuery,
  useGetProductsByFoodtruckSlugQuery,
  useGetReviewsByFoodtruckSlugQuery,
  useGetSocialsByFoodtruckSlugQuery,
} = foodtruckExtendedApi;
