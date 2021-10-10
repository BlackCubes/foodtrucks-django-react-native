import { ADD_SOCIAL, GET_ALL_SOCIALS } from '../constants/socialTypes';
import { createSocial, getAllSocials } from '../../api/socialAPI';
import { headers } from '../../utils';

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
