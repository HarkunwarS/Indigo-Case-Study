import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './components/HomePage';
import LoginPage from './components/LoginPage';
import DashboardPage from './components/DashboardPage';
import FlightConfigPage from './components/FlightConfigPage';
import { AuthProvider } from './context/AuthContext';
import Navbar from './components/Navbar';
import BookingPage from './components/BookingPage';

const App = () => {
  return (
    <AuthProvider>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/dashboard" element={<DashboardPage />} />
          <Route path="/flight-config" element={<FlightConfigPage />} />
          <Route path="/book" element={<BookingPage />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
};

export default App;
