import React, { useState, useEffect } from 'react';
import { Container, Typography, Button, List, ListItem, ListItemText, TextField, Alert } from '@mui/material';
import { useAuth } from '../context/AuthContext';
import { createFlight, getFlights, updateFlight, deleteFlight } from '../api/flights';

function FlightConfigPage() {
  const { logout } = useAuth();
  const [flights, setFlights] = useState([]);
  const [flightDetails, setFlightDetails] = useState({ 
    flight_id: '', 
    airline: '', 
    status: '', 
    departure_gate: '', 
    arrival_gate: '', 
    scheduled_departure: '', 
    scheduled_arrival: '', 
    actual_departure: '', 
    actual_arrival: '' 
  });
  const [message, setMessage] = useState('');
  const [messageType, setMessageType] = useState('');

  useEffect(() => {
    async function fetchFlights() {
      const flightsData = await getFlights();
      setFlights(flightsData);
    }
    fetchFlights();
  }, []);

  const handleFlightChange = (e) => {
    setFlightDetails({ ...flightDetails, [e.target.name]: e.target.value });
  };

  const handleCreateFlight = async () => {
    const newFlightDetails = { ...flightDetails };

    // Remove actual_departure and actual_arrival if they are empty
    if (!newFlightDetails.actual_departure) delete newFlightDetails.actual_departure;
    if (!newFlightDetails.actual_arrival) delete newFlightDetails.actual_arrival;

    try {
      const newFlight = await createFlight(newFlightDetails);
      setFlights([...flights, newFlight]);
      setMessage('Flight created successfully!');
      setMessageType('success');
    } catch (error) {
      console.error('Flight creation failed', error);
      setMessage('Flight creation failed');
      setMessageType('error');
    }
  };

  const handleUpdateFlight = async (id) => {
    const updatedFlightDetails = { ...flightDetails };

    // Remove actual_departure and actual_arrival if they are empty
    if (!updatedFlightDetails.actual_departure) delete updatedFlightDetails.actual_departure;
    if (!updatedFlightDetails.actual_arrival) delete updatedFlightDetails.actual_arrival;

    try {
      const updatedFlight = await updateFlight(id, updatedFlightDetails);
      setFlights(flights.map(flight => (flight.flight_id === id ? updatedFlight : flight)));
      setMessage('Flight updated successfully!');
      setMessageType('success');
    } catch (error) {
      console.error('Flight update failed', error);
      setMessage('Flight update failed');
      setMessageType('error');
    }
  };

  const handleDeleteFlight = async (id) => {
    try {
      await deleteFlight(id);
      setFlights(flights.filter(flight => flight.flight_id !== id));
      setMessage('Flight deleted successfully!');
      setMessageType('success');
    } catch (error) {
      console.error('Flight deletion failed', error);
      setMessage('Flight deletion failed');
      setMessageType('error');
    }
  };

  return (
    <Container maxWidth="md">
      <Typography variant="h4" gutterBottom>Flight Configuration</Typography>
      <Button variant="contained" color="secondary" onClick={logout}>Logout</Button>

      {message && <Alert severity={messageType} onClose={() => setMessage('')}>{message}</Alert>}

      <Typography variant="h5" gutterBottom>Create/Update Flight</Typography>
      <TextField label="Flight ID" name="flight_id" value={flightDetails.flight_id} onChange={handleFlightChange} fullWidth margin="normal" />
      <TextField label="Airline" name="airline" value={flightDetails.airline} onChange={handleFlightChange} fullWidth margin="normal" />
      <TextField label="Status" name="status" value={flightDetails.status} onChange={handleFlightChange} fullWidth margin="normal" />
      <TextField label="Departure Gate" name="departure_gate" value={flightDetails.departure_gate} onChange={handleFlightChange} fullWidth margin="normal" />
      <TextField label="Arrival Gate" name="arrival_gate" value={flightDetails.arrival_gate} onChange={handleFlightChange} fullWidth margin="normal" />
      <TextField label="Scheduled Departure" name="scheduled_departure" type="datetime-local" value={flightDetails.scheduled_departure} onChange={handleFlightChange} fullWidth margin="normal" />
      <TextField label="Scheduled Arrival" name="scheduled_arrival" type="datetime-local" value={flightDetails.scheduled_arrival} onChange={handleFlightChange} fullWidth margin="normal" />
      <TextField label="Actual Departure" name="actual_departure" type="datetime-local" value={flightDetails.actual_departure} onChange={handleFlightChange} fullWidth margin="normal" />
      <TextField label="Actual Arrival" name="actual_arrival" type="datetime-local" value={flightDetails.actual_arrival} onChange={handleFlightChange} fullWidth margin="normal" />
      <Button variant="contained" color="primary" onClick={handleCreateFlight}>Create Flight</Button>
      <Button variant="contained" color="secondary" onClick={() => handleUpdateFlight(flightDetails.flight_id)}>Update Flight</Button>
      <Typography variant="h5" gutterBottom>Flights</Typography>
      <List>
        {flights.map(flight => (
          <ListItem key={flight.flight_id}>
            <ListItemText primary={`Flight ID: ${flight.flight_id}, Airline: ${flight.airline}, Status: ${flight.status}`} />
            <Button variant="contained" color="primary" onClick={() => handleUpdateFlight(flight.flight_id)}>Update</Button>
            <Button variant="contained" color="secondary" onClick={() => handleDeleteFlight(flight.flight_id)}>Delete</Button>
          </ListItem>
        ))}
      </List>
    </Container>
  );
}

export default FlightConfigPage;
