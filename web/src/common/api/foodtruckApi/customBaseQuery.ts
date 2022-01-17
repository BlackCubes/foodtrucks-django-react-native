import {
  BaseQueryFn,
  FetchArgs,
  fetchBaseQuery,
  FetchBaseQueryError,
} from '@reduxjs/toolkit/dist/query';
import { StatusCodes } from 'http-status-codes';

import { RootState } from '../../../app/redux';

import * as authLocalStorage from '../../../features/auth/authLocalStorage';
import { authSlice } from '../../../features/auth/authSlice';

const baseQuery = fetchBaseQuery({
  baseUrl: 'http://127.0.0.1:8000/api/v1',
  prepareHeaders: (headers: Headers, { getState }) => {
    const { token } = (getState() as RootState).auth;

    if (token) {
      headers.set('authorization', `Bearer ${token}`);
    }

    return headers;
  },
});

const customBaseQuery: BaseQueryFn<
  FetchArgs | string,
  unknown,
  FetchBaseQueryError
> = async (args, api, extraOptions) => {
  const result = await baseQuery(args, api, extraOptions);

  if (result.error && result.error.status === StatusCodes.UNAUTHORIZED) {
    api.dispatch(authSlice.actions.userLoggedOut());

    authLocalStorage.clearAuthState();
  }

  return result;
};

export default customBaseQuery;
