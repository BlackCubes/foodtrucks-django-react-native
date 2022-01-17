import { configureStore, ConfigureStoreOptions } from '@reduxjs/toolkit';

import foodtruckApi from '../../common/api/foodtruckApi/coreSplitApi';

import { authSlice } from '../../features/auth/authSlice';

export const createAppStore = (
  options?: ConfigureStoreOptions['preloadedState'] | undefined
) =>
  configureStore({
    reducer: {
      auth: authSlice.reducer,
      [foodtruckApi.reducerPath]: foodtruckApi.reducer,
    },

    middleware: (getDefaultMiddleware) =>
      getDefaultMiddleware().concat(foodtruckApi.middleware),

    ...options,
  });

export const store = createAppStore();

export type RootState = ReturnType<typeof store.getState>;

export type AppDispatch = typeof store.dispatch;
