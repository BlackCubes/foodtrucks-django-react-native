import {
  GET_ALL_FOODTRUCK_PRODUCTS,
  GET_ALL_PRODUCTS,
  GET_ONE_PRODUCT,
} from '../constants/productTypes';

const INITIAL_STATE = {
  products: [],
  product: null,
  foodtruckProducts: [],
};

const productReducer = (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case GET_ALL_PRODUCTS:
      return {
        ...state,
        products: action.payload.products,
      };
    case GET_ONE_PRODUCT:
      return {
        ...state,
        product: action.payload.product,
      };
    case GET_ALL_FOODTRUCK_PRODUCTS:
      return {
        ...state,
        foodtruckProducts: action.payload.foodtruckProducts,
      };
    default:
      return state;
  }
};

export default productReducer;
