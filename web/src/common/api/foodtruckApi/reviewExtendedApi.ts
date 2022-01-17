import coreSplitApi from './coreSplitApi';
import { Review } from '../../models';

const reviewExtendedApi = coreSplitApi.injectEndpoints({
  endpoints: (builder) => ({
    getReviews: builder.query<Review[], void>({
      query: () => ({ url: '/reviews' }),
      providesTags: ['Review'],
    }),

    getReviewsFromUser: builder.query<Review[], void>({
      query: () => ({ url: '/my-reviews' }),
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

  overrideExisting: false,
});

export const {
  useCreateReviewMutation,
  useDeleteReviewMutation,
  useGetReviewByUuidQuery,
  useGetReviewsFromUserQuery,
  useGetReviewsQuery,
  useUpdateReviewMutation,
} = reviewExtendedApi;
