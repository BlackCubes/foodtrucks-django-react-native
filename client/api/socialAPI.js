import axios from 'axios';

const axiosInit = axios.create({
  baseURL: 'http://10.0.0.233:8000/api/v1/socials/',
  responseType: 'json',
});

export const getAllSocials = (headers) =>
  new Promise((resolve, reject) =>
    setTimeout(() => {
      try {
        axiosInit
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

export const createSocial = (emoji, product_slug, like) =>
  new Promise((resolve, reject) =>
    setTimeout(() => {
      try {
        axiosInit
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
