import coreSplitApi from './coreSplitApi';
import { Product, Review, Social } from '../../models';

const productExtendedApi = coreSplitApi.injectEndpoints({
  endpoints: (builder) => ({
    getProducts: builder.query<Product[], void>({
      query: () => ({ url: '/products' }),
      providesTags: ['Product'],
    }),

    getProductBySlug: builder.query<Product, string>({
      query: (slug) => ({ url: `/products/${slug}` }),
      providesTags: ['Product'],
    }),

    getReviewsByProductSlug: builder.query<Review[], string>({
      query: (slug) => ({ url: `/products/${slug}/reviews` }),
      providesTags: ['Review'],
    }),

    getSocialsByProductSlug: builder.query<Social[], string>({
      query: (slug) => ({ url: `/products/${slug}/socials` }),
      providesTags: ['Social'],
    }),
  }),

  overrideExisting: false,
});

export const {
  useGetProductBySlugQuery,
  useGetProductsQuery,
  useGetReviewsByProductSlugQuery,
  useGetSocialsByProductSlugQuery,
} = productExtendedApi;
