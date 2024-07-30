import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

export const getNotifications = async (userId) => {
  const response = await axios.get(`${BASE_URL}/notifications/${userId}`);
  return response.data;
};
