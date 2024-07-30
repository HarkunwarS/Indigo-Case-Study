import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { registerUser } from '../api/auth';

const HomePage = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await registerUser({ username, email, password });
      navigate('/login');
    } catch (error) {
      console.error('Registration failed', error);
    }
  };

  return (
    <div className="flex h-screen bg-airline-background">
      <div className="w-1/2 flex flex-col justify-center items-center bg-white bg-opacity-75 p-8">
        <h2 className="text-2xl mb-4">Register</h2>
        <form onSubmit={handleRegister} className="w-full">
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email"
            className="mb-4 p-2 w-full border rounded"
          />
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
            className="mb-4 p-2 w-full border rounded"
          />
          <button type="submit" className="bg-blue-500 text-white p-2 rounded w-full">Register</button>
        </form>
      </div>
      <div className="w-1/2 flex flex-col justify-center items-center bg-white bg-opacity-75 p-8">
        <h2 className="text-2xl mb-4">Already a user?</h2>
        <button onClick={() => navigate('/login')} className="bg-blue-500 text-white p-2 rounded w-full">Login</button>
      </div>
    </div>
  );
};

export default HomePage;
