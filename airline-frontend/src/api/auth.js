import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

export const loginUser = async (credentials) => {
  const response = await axios.post(`${BASE_URL}/auth/login`, credentials);
  return response.data;
};

export const registerUser = async (userDetails) => {
  const response = await axios.post(`${BASE_URL}/auth/register`, userDetails);
  return response.data;
};
