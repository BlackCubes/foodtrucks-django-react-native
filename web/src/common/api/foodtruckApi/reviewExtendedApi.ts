import coreSplitApi from './coreSplitApi';
import { Review } from '../../models';

type CreateReviewRequest = {
  review: string;
  product: string;
};

type UpdateReviewRequest = {
  uuid: string;
  review: string;
};

const reviewExtendedApi = coreSplitApi.injectEndpoints({
  endpoints: (builder) => ({
    getReviews: builder.query<Review[], void>({
      query: () => ({ url: '/reviews' }),
      providesTags: ['Review'],
    }),

    getReviewsFromUser: builder.query<Omit<Review, 'user'>[], void>({
      query: () => ({ url: '/my-reviews' }),
      providesTags: ['Review'],
    }),

    getReviewByUuid: builder.query<Review, string>({
      query: (uuid) => ({ url: `/reviews/${uuid}` }),
      providesTags: ['Review'],
    }),

    createReview: builder.mutation<Review, CreateReviewRequest>({
      query: (payload) => ({
        url: '/reviews',
        method: 'POST',
        body: payload,
      }),
      invalidatesTags: ['Review'],
    }),

    updateReview: builder.mutation<Review, UpdateReviewRequest>({
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
