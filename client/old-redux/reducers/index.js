import { combineReducers } from 'redux';

import foodtruckReducer from './foodtruckReducer';
import productReducer from './productReducer';
import reviewReducer from './reviewReducer';
import socialReducer from './socialReducer';

const rootReducer = combineReducers({
  foodtruck: foodtruckReducer,
  product: productReducer,
  review: reviewReducer,
  social: socialReducer,
});

export default rootReducer;
