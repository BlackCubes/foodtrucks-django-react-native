import { createApi } from '@reduxjs/toolkit/query/react';

import customBaseQuery from './customBaseQuery';

export default createApi({
  reducerPath: 'foodtruckApi',
  baseQuery: customBaseQuery,

  keepUnusedDataFor: 0,
  refetchOnMountOrArgChange: true,
  refetchOnReconnect: true,

  tagTypes: [
    'Emoji',
    'Event',
    'Foodtruck',
    'Product',
    'Review',
    'Social',
    'User',
  ],

  endpoints: () => ({}),
});
