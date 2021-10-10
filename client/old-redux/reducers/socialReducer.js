import { ADD_SOCIAL, GET_ALL_SOCIALS } from '../constants/socialTypes';

const INITIAL_STATE = {
  socials: [],
};

const socialReducer = (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case GET_ALL_SOCIALS:
      return {
        ...state,
        socials: action.payload.socials,
      };
    case ADD_SOCIAL:
      let uuidExists = false;

      let newSocials = state.socials.map((social) => {
        const clonedSocial = { ...social };

        if (clonedSocial.uuid === action.payload.uuid) {
          clonedSocial.like += action.payload.like;
          uuidExists = true;
        }

        return clonedSocial;
      });

      newSocials = uuidExists
        ? newSocials
        : [
            ...state.socials,
            {
              uuid: action.payload.uuid,
              like: action.payload.like,
              emoji: action.payload.emoji,
              product: action.payload.product,
            },
          ];

      return {
        ...state,
        socials: newSocials,
      };
    default:
      return state;
  }
};

export default socialReducer;
