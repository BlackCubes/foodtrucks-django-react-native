import { createApi } from '@reduxjs/toolkit/query/react';

import customBaseQuery from './customBaseQuery';
import { Product, Review, Social } from '../../models';

export const productApi = createApi({
  reducerPath: 'productApi',
  baseQuery: customBaseQuery,

  keepUnusedDataFor: 0,
  refetchOnMountOrArgChange: true,
  refetchOnReconnect: true,

  tagTypes: ['Product', 'Review', 'Social'],

  endpoints: (builder) => ({
    getProducts: builder.query<Product, void>({
      query: () => ({ url: '/products' }),
      providesTags: ['Product'],
    }),

    getProductBySlug: builder.query<Product, string>({
      query: (slug) => ({ url: `/products/${slug}` }),
      providesTags: ['Product'],
    }),

    getReviewsByProductSlug: builder.query<Review, string>({
      query: (slug) => ({ url: `/products/${slug}/reviews` }),
      providesTags: ['Review'],
    }),

    getSocialsByProductSlug: builder.query<Social, string>({
      query: (slug) => ({ url: `/products/${slug}/socials` }),
      providesTags: ['Social'],
    }),
  }),
});

export const {
  useGetProductBySlugQuery,
  useGetProductsQuery,
  useGetReviewsByProductSlugQuery,
  useGetSocialsByProductSlugQuery,
} = productApi;
