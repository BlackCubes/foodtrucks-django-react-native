import coreSplitApi from './coreSplitApi';
import { Event, Foodtruck, Product, Review, Social } from '../../models';

const foodtruckExtendedApi = coreSplitApi.injectEndpoints({
  endpoints: (builder) => ({
    getFoodtrucks: builder.query<Foodtruck[], void>({
      query: () => ({ url: '/foodtrucks' }),
      providesTags: ['Foodtruck'],
    }),

    getFoodtruckBySlug: builder.query<Foodtruck, string>({
      query: (slug) => ({ url: `/foodtrucks/${slug}` }),
      providesTags: ['Foodtruck'],
    }),

    getEventsByFoodtruckSlug: builder.query<Omit<Event, 'truck'>[], string>({
      query: (slug) => ({ url: `/foodtrucks/${slug}/events` }),
    }),

    getProductsByFoodtruckSlug: builder.query<Omit<Product, 'truck'>[], string>(
      {
        query: (slug) => ({ url: `/foodtrucks/${slug}/products` }),
        providesTags: ['Product'],
      }
    ),

    getReviewsByFoodtruckSlug: builder.query<Review[], string>({
      query: (slug) => ({ url: `/foodtrucks/${slug}/reviews` }),
      providesTags: ['Review'],
    }),

    getSocialsByFoodtruckSlug: builder.query<Social[], string>({
      query: (slug) => ({ url: `/foodtrucks/${slug}/socials` }),
      providesTags: ['Social'],
    }),
  }),

  overrideExisting: false,
});

export const {
  useGetEventsByFoodtruckSlugQuery,
  useGetFoodtruckBySlugQuery,
  useGetFoodtrucksQuery,
  useGetProductsByFoodtruckSlugQuery,
  useGetReviewsByFoodtruckSlugQuery,
  useGetSocialsByFoodtruckSlugQuery,
} = foodtruckExtendedApi;
