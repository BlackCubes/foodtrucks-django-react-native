import coreSplitApi from './coreSplitApi';
import {
  Event,
  Foodtruck,
  Product,
  Review,
  Social,
  SuccessResponse,
} from '../../models';

type GetFoodtrucksResponse = SuccessResponse & {
  data: Foodtruck[];
};

type GetFoodtruckBySlugResponse = Omit<SuccessResponse, 'meta_data'> & {
  data: Foodtruck;
};

type GetEventsByFoodtruckSlugResponse = SuccessResponse & {
  data: Omit<Event, 'truck'>[];
};

type GetProductsByFoodtruckSlugResponse = SuccessResponse & {
  data: Omit<Product, 'truck'>[];
};

type GetReviewsByFoodtruckSlugResponse = SuccessResponse & {
  data: Review[];
};

type GetSocialsByFoodtruckSlugResponse = SuccessResponse & {
  data: Social[];
};

const foodtruckExtendedApi = coreSplitApi.injectEndpoints({
  endpoints: (builder) => ({
    getFoodtrucks: builder.query<GetFoodtrucksResponse, void>({
      query: () => ({ url: '/foodtrucks' }),
      providesTags: ['Foodtruck'],
    }),

    getFoodtruckBySlug: builder.query<GetFoodtruckBySlugResponse, string>({
      query: (slug) => ({ url: `/foodtrucks/${slug}` }),
      providesTags: ['Foodtruck'],
    }),

    getEventsByFoodtruckSlug: builder.query<
      GetEventsByFoodtruckSlugResponse,
      string
    >({
      query: (slug) => ({ url: `/foodtrucks/${slug}/events` }),
    }),

    getProductsByFoodtruckSlug: builder.query<
      GetProductsByFoodtruckSlugResponse,
      string
    >({
      query: (slug) => ({ url: `/foodtrucks/${slug}/products` }),
      providesTags: ['Product'],
    }),

    getReviewsByFoodtruckSlug: builder.query<
      GetReviewsByFoodtruckSlugResponse,
      string
    >({
      query: (slug) => ({ url: `/foodtrucks/${slug}/reviews` }),
      providesTags: ['Review'],
    }),

    getSocialsByFoodtruckSlug: builder.query<
      GetSocialsByFoodtruckSlugResponse,
      string
    >({
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
