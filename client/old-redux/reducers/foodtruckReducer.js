import {
  GET_ALL_FOODTRUCKS,
  GET_ONE_FOODTRUCK,
} from "../constants/foodtruckTypes";

const INITIAL_STATE = {
  foodtrucks: [],
  foodtruck: null,
};

const foodtruckReducer = (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case GET_ALL_FOODTRUCKS:
      return {
        ...state,
        foodtrucks: action.payload.foodtrucks,
      };
    case GET_ONE_FOODTRUCK:
      return {
        ...state,
        foodtruck: action.payload.foodtruck,
      };
    default:
      return state;
  }
};

export default foodtruckReducer;
