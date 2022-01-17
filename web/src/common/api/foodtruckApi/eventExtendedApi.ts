import { createApi } from '@reduxjs/toolkit/query/react';

import customBaseQuery from './customBaseQuery';
import { Event } from '../models';

export const eventApi = createApi({
  reducerPath: 'eventApi',
  baseQuery: customBaseQuery,

  keepUnusedDataFor: 0,
  refetchOnMountOrArgChange: true,
  refetchOnReconnect: true,

  tagTypes: ['Event'],

  endpoints: (builder) => ({
    getEvents: builder.query<Event[], void>({
      query: () => ({ url: '/events' }),
      providesTags: ['Event'],
    }),

    getEventByUuid: builder.query<Event, string>({
      query: (uuid) => ({ url: `/events/${uuid}` }),
      providesTags: ['Event'],
    }),
  }),
});

export const { useGetEventsQuery, useGetEventByUuidQuery } = eventApi;
