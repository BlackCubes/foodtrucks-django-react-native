import coreSplitApi from './coreSplitApi';
import { Session, User } from '../../models';

type ChangePasswordRequest = {
  old_password: string;
  old_password_confirmation: string;
  new_password: string;
};
type LoginRequest = Pick<User, 'email'> & {
  password: string;
};
type LoginResponse = Pick<User, 'email'> & Session;
type RegisterRequest = User & {
  password: string;
  password_confirmation: string;
};
type UserSessionResponse = User & Session;

const userExtendedApi = coreSplitApi.injectEndpoints({
  endpoints: (builder) => ({
    getUserProfile: builder.query<UserSessionResponse, void>({
      query: () => ({ url: '/users/profile' }),
      providesTags: ['User'],
    }),

    register: builder.mutation<UserSessionResponse, RegisterRequest>({
      query: (payload) => ({
        url: '/users/register',
        method: 'POST',
        body: payload,
      }),
    }),

    login: builder.mutation<LoginResponse, LoginRequest>({
      query: (payload) => ({
        url: '/users/login',
        method: 'POST',
        body: payload,
      }),
    }),

    updateProfile: builder.mutation<UserSessionResponse, User>({
      query: (payload) => ({
        url: '/users/profile',
        method: 'PATCH',
        body: payload,
      }),
      invalidatesTags: ['User'],
    }),

    changePassword: builder.mutation<Session, ChangePasswordRequest>({
      query: (payload) => ({
        url: '/user/change-password',
        method: 'PATCH',
        body: payload,
      }),
    }),
  }),

  overrideExisting: false,
});

export const {
  useChangePasswordMutation,
  useGetUserProfileQuery,
  useLoginMutation,
  useRegisterMutation,
  useUpdateProfileMutation,
} = userExtendedApi;
