import {
  GET_ALL_FOODTRUCKS,
  GET_ONE_FOODTRUCK,
} from '../constants/foodtruckTypes';
import { getAllFoodtrucks, getFoodtruck } from '../../api/foodtruckAPI';
import { headers } from '../../utils';

// GET ALL FOODTRUCKS
const finishRetrieveAllFoodtrucks = (foodtrucks) => ({
  type: GET_ALL_FOODTRUCKS,
  payload: { foodtrucks },
});

export const retrieveAllFoodtrucks = () => (dispatch) =>
  getAllFoodtrucks(headers())
    .then((res) => dispatch(finishRetrieveAllFoodtrucks(res)))
    .catch((err) => console.log(err));

// GET ONE FOODTRUCK
const finishRetrieveOneFoodtruck = (foodtruck) => ({
  type: GET_ONE_FOODTRUCK,
  payload: { foodtruck },
});

export const retrieveOneFoodtruck = (slug) => (dispatch) =>
  getFoodtruck(slug, headers())
    .then((res) => {
      const foodtruckData = {
        uuid: res.uuid,
        name: res.name,
        slug: res.slug,
        info: res.info,
        phone_number: res.phone_number,
        email: res.email,
        website: res.website,
        images: res.images,
        events: res.events,
      };

      let foodtruckSocials = [];

      if (res.products.length) {
        res.products.forEach((product) => {
          if (product.likes.length) {
            product.likes.forEach((like) => {
              foodtruckSocials.push(like);
            });
          }
        });
      }

      dispatch(finishRetrieveOneFoodtruck(foodtruckData));
    })
    .catch((err) => err);
