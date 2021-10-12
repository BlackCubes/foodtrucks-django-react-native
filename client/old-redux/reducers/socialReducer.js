import {
  ADD_SOCIAL,
  GET_ALL_FOODTRUCK_SOCIALS,
  GET_ALL_PRODUCT_SOCIALS,
  GET_ALL_SOCIALS,
} from '../constants/socialTypes';

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
      let foodtruckUuidExists = false;

      let newFoodtruckSocials = state.foodtruckSocials.map((social) => {
        const clonedSocial = { ...social };

        if (clonedSocial.uuid === action.payload.uuid) {
          clonedSocial.like += action.payload.uuid;
          foodtruckUuidExists = true;
        }

        return clonedSocial;
      });

      newFoodtruckSocials = foodtruckUuidExists
        ? newFoodtruckSocials
        : [
            ...state.foodtruckSocials,
            {
              uuid: action.payload.uuid,
              like: action.payload.like,
              emoji: action.payload.emoji,
              product: action.payload.product,
            },
          ];

      let productUuidExists = false;

      let newProductSocials = state.productSocials.map((social) => {
        const clonedSocial = { ...social };

        if (clonedSocial.uuid === action.payload.uuid) {
          clonedSocial += action.payload.uuid;
          productUuidExists = true;
        }

        return clonedSocial;
      });

      newProductSocials = productUuidExists
        ? newProductSocials
        : [
            ...state.productSocials,
            {
              uuid: action.payload.uuid,
              like: action.payload.like,
              emoji: action.payload.emoji,
              product: action.payload.product,
            },
          ];

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
