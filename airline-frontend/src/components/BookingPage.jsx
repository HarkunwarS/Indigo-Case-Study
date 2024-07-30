import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { bookFlight } from '../api/bookings';
import { useAuth } from '../context/AuthContext';

function BookingPage() {
  const { user } = useAuth();
  const [flightId, setFlightId] = useState('');
  const [passengerName, setPassengerName] = useState('');
  const [passengerAge, setPassengerAge] = useState('');
  const [passengerContact, setPassengerContact] = useState('');
  const [passengerEmail, setPassengerEmail] = useState('');
  const navigate = useNavigate();

  const handleBooking = async () => {
    const bookingData = {
      flight_id: flightId,
      passenger_name: passengerName,
      passenger_age: passengerAge,
      passenger_contact: passengerContact,
      passenger_email: passengerEmail,
    };

    try {
      await bookFlight(bookingData);
      alert('Booking successful!');
      navigate('/dashboard');
    } catch (error) {
      console.error('Booking failed', error);
      alert('Booking failed');
    }
  };

  return (
    <div>
      <h2>Book a Ticket</h2>
      <form onSubmit={(e) => { e.preventDefault(); handleBooking(); }}>
        <input
          type="text"
          value={flightId}
          onChange={(e) => setFlightId(e.target.value)}
          placeholder="Flight ID"
          required
        />
        <input
          type="text"
          value={passengerName}
          onChange={(e) => setPassengerName(e.target.value)}
          placeholder="Passenger Name"
          required
        />
        <input
          type="number"
          value={passengerAge}
          onChange={(e) => setPassengerAge(e.target.value)}
          placeholder="Passenger Age"
          required
        />
        <input
          type="text"
          value={passengerContact}
          onChange={(e) => setPassengerContact(e.target.value)}
          placeholder="Passenger Contact"
          required
        />
        <input
          type="email"
          value={passengerEmail}
          onChange={(e) => setPassengerEmail(e.target.value)}
          placeholder="Passenger Email"
          required
        />
        <button type="submit">Book Ticket</button>
      </form>
    </div>
  );
}

export default BookingPage;
