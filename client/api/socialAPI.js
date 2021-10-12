import { axiosInit } from '../utils';

export const getAllSocials = (headers) =>
  new Promise((resolve, reject) =>
    setTimeout(() => {
      try {
        axiosInit('socials')
          .get('', headers)
          .then((res) => resolve(res.data))
          .catch((err) => {
            if (err.response) {
              reject(err.response.data);
            } else if (err.request) {
              reject(err.request);
            } else {
              reject(err.message);
            }
          });
      } catch (err) {
        reject('System error. Please try again later.');
      }
    }, 1000)
  );

export const createSocial = (emoji, product_slug, like, headers) =>
  new Promise((resolve, reject) =>
    setTimeout(() => {
      try {
        axiosInit('socials')
          .post(
            '',
            {
              emoji,
              product: product_slug,
              like,
            },
            headers
          )
          .then((res) => resolve(res.data))
          .catch((err) => {
            if (err.response) {
              reject(err.response.data);
            } else if (err.request) {
              reject(err.request);
            } else {
              reject(err.message);
            }
          });
      } catch (err) {
        reject('System error. Please try again later.');
      }
    }, 1000)
  );

export const getAllSocialsFromFoodtruck = (foodtruck_slug, headers) =>
  new Promise((resolve, reject) =>
    setTimeout(() => {
      try {
        axiosInit('foodtrucks')
          .get(`${foodtruck_slug}/socials`, headers)
          .then((res) => resolve(res.data))
          .catch((err) => {
            if (err.response) {
              reject(err.response.data);
            } else if (err.request) {
              reject(err.request);
            } else {
              reject(err.message);
            }
          });
      } catch (err) {
        reject('System error. Please try again later.');
      }
    }, 1000)
  );

export const getAllSocialsFromProduct = (product_slug, headers) =>
  new Promise((resolve, reject) =>
    setTimeout(() => {
      try {
        axiosInit('products')
          .get(`${product_slug}/socials`, headers)
          .then((res) => resolve(res.data))
          .catch((err) => {
            if (err.response) {
              reject(err.response.data);
            } else if (err.request) {
              reject(err.request);
            } else {
              reject(err.message);
            }
          });
      } catch (err) {
        reject('System error. Please try again later.');
      }
    }, 1000)
  );
