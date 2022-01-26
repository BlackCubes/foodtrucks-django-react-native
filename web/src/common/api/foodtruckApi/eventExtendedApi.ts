import coreSplitApi from './coreSplitApi';
import { Event, SuccessResponse } from '../../models';

type GetEventsResponse = SuccessResponse & {
  data: Event[];
};

type GetEventByUuidResponse = Omit<SuccessResponse, 'meta_data'> & {
  data: Event;
};

const eventExtendedApi = coreSplitApi.injectEndpoints({
  endpoints: (builder) => ({
    getEvents: builder.query<GetEventsResponse, void>({
      query: () => ({ url: '/events/' }),
      providesTags: ['Event'],
    }),

    getEventByUuid: builder.query<GetEventByUuidResponse, string>({
      query: (uuid) => ({ url: `/events/${uuid}` }),
      providesTags: ['Event'],
    }),
  }),

  overrideExisting: false,
});

export const { useGetEventByUuidQuery, useGetEventsQuery } = eventExtendedApi;
