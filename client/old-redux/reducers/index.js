import { combineReducers } from 'redux';

import foodtruckReducer from './foodtruckReducer';
import productReducer from './productReducer';
import socialReducer from './socialReducer';

const rootReducer = combineReducers({
  foodtruck: foodtruckReducer,
  product: productReducer,
  social: socialReducer,
});

export default rootReducer;
