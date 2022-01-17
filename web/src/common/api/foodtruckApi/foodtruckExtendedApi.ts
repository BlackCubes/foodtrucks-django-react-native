import { createApi } from '@reduxjs/toolkit/query/react';

import customBaseQuery from './customBaseQuery';
import { Foodtruck, Product, Review, Social } from '../../models';

export const foodtruckApi = createApi({
  reducerPath: 'foodtruckApi',
  baseQuery: customBaseQuery,

  keepUnusedDataFor: 0,
  refetchOnMountOrArgChange: true,
  refetchOnReconnect: true,

  tagTypes: ['Foodtruck', 'Product', 'Review', 'Social'],

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
});

export const {
  useGetFoodtruckBySlugQuery,
  useGetFoodtrucksQuery,
  useGetProductsByFoodtruckSlugQuery,
  useGetReviewsByFoodtruckSlugQuery,
  useGetSocialsByFoodtruckSlugQuery,
} = foodtruckApi;
