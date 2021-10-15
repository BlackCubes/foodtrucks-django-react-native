import {
  ADD_REVIEW,
  GET_ALL_FOODTRUCK_REVIEWS,
  GET_ALL_PRODUCT_REVIEWS,
  GET_ALL_REVIEWS,
  GET_ONE_REVIEW,
} from '../constants/reviewTypes';
import {
  createReview,
  getAllReviews,
  getAllReviewsFromFoodtruck,
  getAllReviewsFromProduct,
  getReview,
} from '../../api/reviewAPI';
import { headers } from '../../utils';

// GET ALL REVIEWS
const finishRetrieveAllReview = (reviews) => ({
  type: GET_ALL_REVIEWS,
  payload: { reviews },
});

export const retrieveAllReviews = () => (dispatch) =>
  getAllReviews(headers())
    .then((res) => dispatch(finishRetrieveAllReview(res)))
    .catch((err) => console.error(err));

// ADD REVIEW
const finishAddReview = (
  uuid,
  review,
  product,
  user,
  created_at,
  updated_at
) => ({
  type: ADD_REVIEW,
  payload: { uuid, review, product, user, created_at, updated_at },
});

export const addReview = (review, product_slug, user_uuid) => (dispatch) =>
  createReview(review, product_slug, user_uuid, headers())
    .then((res) =>
      dispatch(
        finishAddReview(
          res.uuid,
          res.review,
          res.product,
          res.user,
          res.created_at,
          res.updated_at
        )
      )
    )
    .catch((err) => console.error(err));

// GET ONE REVIEW
const finishRetrieveOneReview = (review) => ({
  type: GET_ONE_REVIEW,
  payload: { review },
});

export const retrieveOneReview = (uuid) => (dispatch) =>
  getReview(uuid, headers())
    .then((res) => dispatch(finishRetrieveOneReview(res)))
    .catch((err) => console.error(err));

// GET ALL REVIEWS FROM FOODTRUCK
const finishRetrieveAllReviewsFromFoodtruck = (foodtruckReviews) => ({
  type: GET_ALL_FOODTRUCK_REVIEWS,
  payload: { foodtruckReviews },
});

export const retrieveAllReviewsFromFoodtruck = (foodtruck_slug) => (dispatch) =>
  getAllReviewsFromFoodtruck(foodtruck_slug, headers())
    .then((res) => dispatch(finishRetrieveAllReviewsFromFoodtruck(res)))
    .catch((err) => console.error(err));

// GET ALL REVIEWS FROM PRODUCT
const finishRetrieveAllReviewsFromProduct = (productReviews) => ({
  type: GET_ALL_PRODUCT_REVIEWS,
  payload: { productReviews },
});

export const retrieveAllReviewsFromProduct = (product_slug) => (dispatch) =>
  getAllReviewsFromProduct(product_slug, headers())
    .then((res) => dispatch(finishRetrieveAllReviewsFromProduct(res)))
    .catch((err) => console.error(err));
