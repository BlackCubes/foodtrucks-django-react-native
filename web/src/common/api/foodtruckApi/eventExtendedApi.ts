import coreSplitApi from './coreSplitApi';
import { Event } from '../../models';

const eventExtendedApi = coreSplitApi.injectEndpoints({
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

  overrideExisting: false,
});

export const { useGetEventByUuidQuery, useGetEventsQuery } = eventExtendedApi;
