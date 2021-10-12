import {
  ADD_SOCIAL,
  GET_ALL_FOODTRUCK_SOCIALS,
  GET_ALL_PRODUCT_SOCIALS,
  GET_ALL_SOCIALS,
} from '../constants/socialTypes';

const newSocials = (stateArray, actionPayload) => {
  let uuidExists = false;

  const updateSocials = stateArray.map((social) => {
    const clonedSocial = { ...social };

    if (clonedSocial.uuid === actionPayload.uuid) {
      clonedSocial.like += actionPayload.like;
      uuidExists = true;
    }

    return clonedSocial;
  });

  return uuidExists
    ? updateSocials
    : [
        ...stateArray,
        {
          uuid: actionPayload.uuid,
          like: actionPayload.like,
          emoji: actionPayload.emoji,
          product: actionPayload.product,
        },
      ];
};

const INITIAL_STATE = {
  foodtruckSocials: [],
  productSocials: [],
};

const socialReducer = (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case GET_ALL_SOCIALS:
      return {
        ...state,
        socials: action.payload.socials,
      };
    case GET_ALL_FOODTRUCK_SOCIALS:
      return {
        ...state,
        foodtruckSocials: action.payload.foodtruckSocials,
      };
    case GET_ALL_PRODUCT_SOCIALS:
      return {
        ...state,
        productSocials: action.payload.productSocials,
      };
    case ADD_SOCIAL:
      const newFoodtruckSocials = newSocials(
        state.foodtruckSocials,
        action.payload
      );
      const newProductSocials = newSocials(
        state.productSocials,
        action.payload
      );

      return {
        ...state,
        foodtruckSocials: newFoodtruckSocials,
        productSocials: newProductSocials,
      };
    default:
      return state;
  }
};

export default socialReducer;
