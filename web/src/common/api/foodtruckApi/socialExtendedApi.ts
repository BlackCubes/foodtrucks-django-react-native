import coreSplitApi from './coreSplitApi';
import { Emoji, Social } from '../../models';

type CreateSocialRequest = {
  like: number;
  emoji: string;
  product: string;
};

const socialExtendedApi = coreSplitApi.injectEndpoints({
  endpoints: (builder) => ({
    getSocials: builder.query<Social[], void>({
      query: () => ({ url: '/socials' }),
      providesTags: ['Social'],
    }),

    getSocialByUuid: builder.query<Social, string>({
      query: (uuid) => ({ url: `/socials/${uuid}` }),
      providesTags: ['Social'],
    }),

    createSocial: builder.mutation<Social, CreateSocialRequest>({
      query: (payload) => ({
        url: '/socials',
        method: 'POST',
        body: payload,
      }),
      invalidatesTags: ['Social'],
    }),

    getEmojis: builder.query<Emoji[], void>({
      query: () => ({ url: '/socials/emojis' }),
      providesTags: ['Emoji'],
    }),
  }),

  overrideExisting: false,
});

export const {
  useCreateSocialMutation,
  useGetEmojisQuery,
  useGetSocialByUuidQuery,
  useGetSocialsQuery,
} = socialExtendedApi;
