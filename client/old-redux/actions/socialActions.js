import {
  ADD_SOCIAL,
  GET_ALL_EMOJIS,
  GET_ALL_FOODTRUCK_SOCIALS,
  GET_ALL_PRODUCT_SOCIALS,
  GET_ALL_SOCIALS,
} from '../constants/socialTypes';
import {
  createSocial,
  getAllEmojis,
  getAllSocials,
  getAllSocialsFromFoodtruck,
  getAllSocialsFromProduct,
} from '../../api/socialAPI';
import { headers } from '../../utils';

// GET ALL EMOJIS
const finishAllEmojis = (emojis) => ({
  type: GET_ALL_EMOJIS,
  payload: { emojis },
});

export const allEmojis = () => (dispatch) =>
  getAllEmojis(headers())
    .then((res) => dispatch(finishAllEmojis(res)))
    .catch((err) => console.error(err));

// GET ALL SOCIALS
const finishAllSocials = (socials) => ({
  type: GET_ALL_SOCIALS,
  payload: { socials },
});

export const allSocials = () => (dispatch) =>
  getAllSocials(headers())
    .then((res) => dispatch(finishAllSocials(res)))
    .catch((err) => console.error(err));

// ADD SOCIAL
const finishAddSocial = (uuid, like, emoji, product) => ({
  type: ADD_SOCIAL,
  payload: { uuid, like, emoji, product },
});

export const addSocial = (emoji, product_slug, like) => (dispatch) =>
  createSocial(emoji, product_slug, like, headers())
    .then((res) =>
      dispatch(finishAddSocial(res.uuid, res.like, res.emoji, res.product))
    )
    .catch((err) => console.error(err));

// GET ALL SOCIALS FROM FOODTRUCK
const finishAllSocialsFromFoodtruck = (foodtruckSocials) => ({
  type: GET_ALL_FOODTRUCK_SOCIALS,
  payload: { foodtruckSocials },
});

export const allSocialsFromFoodtruck = (foodtruck_slug) => (dispatch) =>
  getAllSocialsFromFoodtruck(foodtruck_slug, headers())
    .then((res) => dispatch(finishAllSocialsFromFoodtruck(res)))
    .catch((err) => console.error(err));

// GET ALL SOCIALS FROM PRODUCT
const finishAllSocialsFromProduct = (productSocials) => ({
  type: GET_ALL_PRODUCT_SOCIALS,
  payload: { productSocials },
});

export const allSocialsFromProduct = (product_slug) => (dispatch) =>
  getAllSocialsFromProduct(product_slug, headers())
    .then((res) => dispatch(finishAllSocialsFromProduct(res)))
    .catch((err) => console.error(err));
