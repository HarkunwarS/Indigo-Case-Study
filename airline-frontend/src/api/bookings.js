import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

export const getBookings = async (userId) => {
  const response = await axios.get(`${BASE_URL}/bookings?userId=${userId}`);
  return response.data;
};

export const getNotifications = async (userId) => {
  const response = await axios.get(`${BASE_URL}/notifications?userId=${userId}`);
  return response.data;
};

export const bookFlight = async (bookingData) => {
    const response = await axios.post(`${BASE_URL}/bookings`, bookingData);
    return response.data;
  };