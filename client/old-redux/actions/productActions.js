import {
  GET_ALL_FOODTRUCK_PRODUCTS,
  GET_ALL_PRODUCTS,
  GET_ONE_PRODUCT,
} from '../constants/productTypes';
import {
  getAllProducts,
  getAllProductsFromFoodtruck,
  getProduct,
} from '../../api/productAPI';
import { headers } from '../../utils';

// GET ALL PRODUCTS
const finishRetrieveAllProducts = (products) => ({
  type: GET_ALL_PRODUCTS,
  payload: { products },
});

export const retrieveAllProducts = () => (dispatch) =>
  getAllProducts(headers())
    .then((res) => dispatch(finishRetrieveAllProducts(res)))
    .catch((err) => console.error(err));

// GET ONE PRODUCT
const finishRetrieveOneProduct = (product) => ({
  type: GET_ONE_PRODUCT,
  payload: { product },
});

export const retrieveOneProduct = (slug) => (dispatch) =>
  getProduct(slug, headers())
    .then((res) => {
      const productData = {
        uuid: res.uuid,
        name: res.name,
        slug: res.slug,
        info: res.info,
        image: res.image,
        price: res.price,
        quantity: res.quantity,
        is_available: res.is_available,
        truck: res.truck,
      };

      dispatch(finishRetrieveOneProduct(productData));
    })
    .catch((err) => console.error(err));

// GET ALL PRODUCTS FROM FOODTRUCK
const finishRetrieveAllProductsFromFoodtruck = (foodtruckProducts) => ({
  type: GET_ALL_FOODTRUCK_PRODUCTS,
  payload: { foodtruckProducts },
});

export const retrieveAllProductsFromFoodtruck =
  (foodtruck_slug) => (dispatch) =>
    getAllProductsFromFoodtruck(foodtruck_slug, headers())
      .then((res) => dispatch(finishRetrieveAllProductsFromFoodtruck(res)))
      .catch((err) => console.error(err));
