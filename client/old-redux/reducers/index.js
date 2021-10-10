import { combineReducers } from 'redux';

import foodtruckReducer from './foodtruckReducer';
import socialReducer from './socialReducer';

const rootReducer = combineReducers({
  foodtruck: foodtruckReducer,
  // product: {},
  social: socialReducer,
});

export default rootReducer;
