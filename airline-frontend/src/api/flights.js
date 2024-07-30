import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

export const getFlights = async () => {
  const response = await axios.get(`${BASE_URL}/flights`);
  return response.data;
};

export const createFlight = async (flight) => {
  const response = await axios.post(`${BASE_URL}/flights`, flight);
  return response.data;
};

export const updateFlight = async (flightId, flight) => {
  const response = await axios.put(`${BASE_URL}/flights/${flightId}`, flight);
  return response.data;
};

export const deleteFlight = async (flightId) => {
  const response = await axios.delete(`${BASE_URL}/flights/${flightId}`);
  return response.data;
};