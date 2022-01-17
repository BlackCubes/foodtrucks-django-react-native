import { createApi } from '@reduxjs/toolkit/query/react';

import customBaseQuery from './customBaseQuery';
import { Review } from '../models';

export const reviewApi = createApi({
  reducerPath: 'reviewApi',
  baseQuery: customBaseQuery,

  keepUnusedDataFor: 0,
  refetchOnMountOrArgChange: true,
  refetchOnReconnect: true,

  tagTypes: ['Review'],

  endpoints: (builder) => ({
    getReviews: builder.query<Review[], void>({
      query: () => ({ url: '/reviews' }),
      providesTags: ['Review'],
    }),

    getReviewByUuid: builder.query<Review, string>({
      query: (uuid) => ({ url: `/reviews/${uuid}` }),
      providesTags: ['Review'],
    }),

    createReview: builder.mutation<Review, Pick<Review, 'review' | 'product'>>({
      query: (payload) => ({
        url: '/reviews',
        method: 'POST',
        body: payload,
      }),
      invalidatesTags: ['Review'],
    }),

    updateReview: builder.mutation<Review, Pick<Review, 'uuid' | 'review'>>({
      query: ({ uuid, review }) => ({
        url: `/reviews/${uuid}`,
        method: 'PATCH',
        body: { review },
      }),
      invalidatesTags: ['Review'],
    }),

    deleteReview: builder.mutation<void, string>({
      query: (uuid) => ({
        url: `/reviews/${uuid}`,
        method: 'DELETE',
      }),
      invalidatesTags: ['Review'],
    }),
  }),
});

export const {
  useCreateReviewMutation,
  useDeleteReviewMutation,
  useGetReviewsQuery,
  useGetReviewByUuidQuery,
  useUpdateReviewMutation,
} = reviewApi;
