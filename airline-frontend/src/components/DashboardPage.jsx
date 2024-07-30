import React, { useEffect, useState } from 'react';
import { Container, Typography, Button, List, ListItem, ListItemText } from '@mui/material';
import { useAuth } from '../context/AuthContext';
import { getBookings, getNotifications } from '../api/bookings';
import { useNavigate } from 'react-router-dom';

function DashboardPage() {
  const { user, logout } = useAuth();
  const [bookings, setBookings] = useState([]);
  const [notifications, setNotifications] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchData() {
      if (user && user.id) {
        const bookings = await getBookings(user.id);
        setBookings(bookings);

        const notifications = await getNotifications(user.id);
        setNotifications(notifications);
      }
    }
    fetchData();
  }, [user]);

  if (!user) {
    return <Typography variant="h6">Loading...</Typography>;
  }

  return (
    <Container maxWidth="md">
      <Typography variant="h4" gutterBottom>Dashboard</Typography>
      <Button variant="contained" color="secondary" onClick={logout}>Logout</Button>
      <Typography variant="h5" gutterBottom>Bookings</Typography>
      <List>
        {bookings.map(booking => (
          <ListItem key={booking.id}>
            <ListItemText primary={`Flight: ${booking.flight_id} - ${booking.status}`} />
          </ListItem>
        ))}
      </List>
      <Typography variant="h5" gutterBottom>Notifications</Typography>
      <List>
        {notifications.map(notification => (
          <ListItem key={notification.id}>
            <ListItemText primary={notification.message} secondary={notification.timestamp} />
          </ListItem>
        ))}
      </List>
      <Button variant="contained" color="primary" onClick={() => navigate('/book')}>Book a Ticket</Button>
    </Container>
  );
}

export default DashboardPage;
