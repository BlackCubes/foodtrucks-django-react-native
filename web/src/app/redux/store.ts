import { configureStore, ConfigureStoreOptions } from '@reduxjs/toolkit';

import foodtruckApi from '../../common/api/foodtruckApi/coreSplitApi';

export const createAppStore = (
  options?: ConfigureStoreOptions['preloadedState'] | undefined
) =>
  configureStore({
    reducer: {
      [foodtruckApi.reducerPath]: foodtruckApi.reducer,
    },

    middleware: (getDefaultMiddleware) =>
      getDefaultMiddleware().concat(foodtruckApi.middleware),

    ...options,
  });

export const store = createAppStore();

export type RootState = ReturnType<typeof store.getState>;

export type AppDispatch = typeof store.dispatch;
