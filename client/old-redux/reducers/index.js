import { combineReducers } from "redux";

import foodtruckReducer from "./foodtruckReducer";

const rootReducer = combineReducers({
  foodtruck: foodtruckReducer,
  // product: {},
});

export default rootReducer;
