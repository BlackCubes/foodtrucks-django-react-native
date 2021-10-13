import {
  ADD_REVIEW,
  GET_ALL_FOODTRUCK_REVIEWS,
  GET_ALL_PRODUCT_REVIEWS,
  GET_ALL_REVIEWS,
  GET_ONE_REVIEW,
} from '../constants/reviewTypes';

const INITIAL_STATE = {
  reviews: [],
  review: null,
  foodtruckReviews: [],
  productReviews: [],
};

const reviewReducer = (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case GET_ALL_REVIEWS:
      return {
        ...state,
        reviews: action.payload.reviews,
      };
    case GET_ONE_REVIEW:
      return {
        ...state,
        review: action.payload.review,
      };
    case GET_ALL_FOODTRUCK_REVIEWS:
      return {
        ...state,
        foodtruckReviews: action.payload.foodtruckReviews,
      };
    case GET_ALL_PRODUCT_REVIEWS:
      return {
        ...state,
        productReviews: action.payload.productReviews,
      };
    case ADD_REVIEW:
      const newReview = {
        uuid: action.payload.uuid,
        review: action.payload.review,
        product: action.payload.product,
        user: action.payload.user,
        created_at: action.payload.created_at,
        updated_at: action.payload.updated_at,
      };

      return {
        ...state,
        foodtruckReviews: [...state.foodtruckReviews, newReview],
        productReviews: [...state.productReviews, newReview],
      };
    default:
      return state;
  }
};

export default reviewReducer;
