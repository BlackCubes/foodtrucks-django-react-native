import coreSplitApi from './coreSplitApi';
import { Emoji, Social, SuccessResponse } from '../../models';

type CreateSocialRequest = {
  like: number;
  emoji: string;
  product: string;
};

type GetSocialsResponse = SuccessResponse & {
  data: Social[];
};

type GeneralSocialResponse = Omit<SuccessResponse, 'meta_data'> & {
  data: Social;
};

type GetEmojisReponse = SuccessResponse & {
  data: Emoji[];
};

const socialExtendedApi = coreSplitApi.injectEndpoints({
  endpoints: (builder) => ({
    getSocials: builder.query<GetSocialsResponse, void>({
      query: () => ({ url: '/socials' }),
      providesTags: ['Social'],
    }),

    getSocialByUuid: builder.query<GeneralSocialResponse, string>({
      query: (uuid) => ({ url: `/socials/${uuid}` }),
      providesTags: ['Social'],
    }),

    createSocial: builder.mutation<GeneralSocialResponse, CreateSocialRequest>({
      query: (payload) => ({
        url: '/socials',
        method: 'POST',
        body: payload,
      }),
      invalidatesTags: ['Social'],
    }),

    getEmojis: builder.query<GetEmojisReponse, void>({
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
