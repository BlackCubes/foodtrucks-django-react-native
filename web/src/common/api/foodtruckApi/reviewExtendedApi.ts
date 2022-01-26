import coreSplitApi from './coreSplitApi';
import { Review, SuccessResponse } from '../../models';

type CreateReviewRequest = {
  review: string;
  product: string;
};

type UpdateReviewRequest = {
  uuid: string;
  review: string;
};

type GetReviewsResponse = SuccessResponse & {
  data: Review[];
};

type GetReviewsFromUserResponse = SuccessResponse & {
  data: Omit<Review, 'user'>[];
};

type GeneralReviewResponse = Omit<SuccessResponse, 'meta_data'> & {
  data: Review;
};

const reviewExtendedApi = coreSplitApi.injectEndpoints({
  endpoints: (builder) => ({
    getReviews: builder.query<GetReviewsResponse, void>({
      query: () => ({ url: '/reviews' }),
      providesTags: ['Review'],
    }),

    getReviewsFromUser: builder.query<GetReviewsFromUserResponse, void>({
      query: () => ({ url: '/my-reviews' }),
      providesTags: ['Review'],
    }),

    getReviewByUuid: builder.query<GeneralReviewResponse, string>({
      query: (uuid) => ({ url: `/reviews/${uuid}` }),
      providesTags: ['Review'],
    }),

    createReview: builder.mutation<GeneralReviewResponse, CreateReviewRequest>({
      query: (payload) => ({
        url: '/reviews',
        method: 'POST',
        body: payload,
      }),
      invalidatesTags: ['Review'],
    }),

    updateReview: builder.mutation<GeneralReviewResponse, UpdateReviewRequest>({
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
