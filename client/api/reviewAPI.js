import { axiosInit } from '../utils';

export const getAllReviews = (headers) =>
  new Promise((resolve, reject) =>
    setTimeout(() => {
      try {
        axiosInit('reviews')
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

export const createReview = (review, product_slug, user_uuid, headers) =>
  new Promise((resolve, reject) =>
    setTimeout(() => {
      try {
        axiosInit('reviews')
          .post(
            '',
            {
              review,
              product: product_slug,
              user: user_uuid,
            },
            headers
          )
          .then((res) => resolve(res.data))
          .catch((err) => {
            if (err.response) {
              reject(err.reponse.data);
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

export const getReview = (uuid, headers) =>
  new Promise((resolve, reject) =>
    setTimeout(() => {
      try {
        axiosInit('reviews')
          .get(`${uuid}`, headers)
          .then((res) => resolve(res.data))
          .catch((err) => {
            if (err.response) {
              reject(err.reponse.data);
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

export const getAllReviewsFromFoodtruck = (foodtruck_slug, headers) =>
  new Promise((resolve, reject) =>
    setTimeout(() => {
      try {
        axiosInit('foodtrucks')
          .get(`${foodtruck_slug}/reviews`, headers)
          .then((res) => resolve(res.data))
          .catch((err) => {
            if (err.response) {
              reject(err.reponse.data);
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

export const getAllReviewsFromProduct = (product_slug, headers) =>
  new Promise((resolve, reject) =>
    setTimeout(() => {
      try {
        axiosInit('products')
          .get(`${product_slug}/reviews`, headers)
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
