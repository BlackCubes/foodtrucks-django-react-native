import axios from 'axios';

const axiosInit = (path) =>
  axios.create({
    baseURL: `http://10.0.0.233:8000/api/v1/${path}/`,
    responseType: 'json',
  });

export default axiosInit;
