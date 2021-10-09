import {
  GET_ALL_FOODTRUCKS,
  GET_ONE_FOODTRUCK,
} from '../constants/foodtruckTypes';
import { getAllFoodtrucks, getFoodtruck } from '../../api/foodtruckAPI';
import { headers } from '../../utils';

// GET ALL FOODTRUCKS
const finishAllFoodtrucks = (foodtrucks) => ({
  type: GET_ALL_FOODTRUCKS,
  payload: { foodtrucks },
});

export const allFoodtrucks = () => (dispatch) =>
  getAllFoodtrucks(headers())
    .then((res) => dispatch(finishAllFoodtrucks(res)))
    .catch((err) => console.log(err));

// GET ONE FOODTRUCK
const finishOneFoodtruck = (foodtruck) => ({
  type: GET_ONE_FOODTRUCK,
  payload: { foodtruck },
});

export const oneFoodtruck = (slug) => (dispatch) =>
  getFoodtruck(slug, headers())
    .then((res) => dispatch(finishOneFoodtruck(res)))
    .catch((err) => err);
