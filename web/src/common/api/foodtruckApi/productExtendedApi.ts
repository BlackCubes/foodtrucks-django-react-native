import coreSplitApi from './coreSplitApi';
import { Product, Review, Social, SuccessResponse } from '../../models';

type GetProductsResponse = SuccessResponse & {
  data: Product[];
};

type GetProductsBySlugResponse = Omit<SuccessResponse, 'meta_data'> & {
  data: Product;
};

type GetReviewsByProductSlugResponse = SuccessResponse & {
  data: Omit<Review, 'product'>[];
};

type GetSocialsByProductSlugResponse = SuccessResponse & {
  data: Omit<Social, 'product'>[];
};

const productExtendedApi = coreSplitApi.injectEndpoints({
  endpoints: (builder) => ({
    getProducts: builder.query<GetProductsResponse, void>({
      query: () => ({ url: '/products' }),
      providesTags: ['Product'],
    }),

    getProductBySlug: builder.query<GetProductsBySlugResponse, string>({
      query: (slug) => ({ url: `/products/${slug}` }),
      providesTags: ['Product'],
    }),

    getReviewsByProductSlug: builder.query<
      GetReviewsByProductSlugResponse,
      string
    >({
      query: (slug) => ({ url: `/products/${slug}/reviews` }),
      providesTags: ['Review'],
    }),

    getSocialsByProductSlug: builder.query<
      GetSocialsByProductSlugResponse,
      string
    >({
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
