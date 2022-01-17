import { createApi } from '@reduxjs/toolkit/query/react';

import customBaseQuery from './customBaseQuery';
import { Emoji, Social } from '../../models';

export const socialApi = createApi({
  reducerPath: 'socialApi',
  baseQuery: customBaseQuery,

  keepUnusedDataFor: 0,
  refetchOnMountOrArgChange: true,
  refetchOnReconnect: true,

  tagTypes: ['Social', 'Emoji'],

  endpoints: (builder) => ({
    getSocials: builder.query<Social[], void>({
      query: () => ({ url: '/socials' }),
      providesTags: ['Social'],
    }),

    getSocialByUuid: builder.query<Social, string>({
      query: (uuid) => ({ url: `/socials/${uuid}` }),
      providesTags: ['Social'],
    }),

    createSocial: builder.mutation<
      Social,
      Pick<Social, 'emoji' | 'like' | 'product'>
    >({
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
});

export const {
  useCreateSocialMutation,
  useGetEmojisQuery,
  useGetSocialsQuery,
  useGetSocialByUuidQuery,
} = socialApi;
