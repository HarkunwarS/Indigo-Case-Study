# Airline Management System

This repository contains an Airline Management System with a backend built using Python FastAPI and PostgreSQL, and a frontend built using React.js. The application allows users to book flights, receive notifications via email (using SMTP), and manage flights. Admin users have the ability to create, update, and delete flights.

## Features

- User registration and login
- Flight booking
- Flight management (admin only)
- Email notifications for flight status changes
- Frontend built with React.js and Tailwind CSS
- Backend built with FastAPI and PostgreSQL

## Future Prospects

- JWT tokens for session management and user role definitions.

## Prerequisites

- Python 3.11
- Node.js and npm
- PostgreSQL

## Installation

### Backend

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HarkunwarS/Airline-Management-System

2. **Install the dependencies:**
    pip install -r requirements.txt

3. Create a .env file in the backend directory with the following content:
   DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database>
   GMAIL_USERNAME=<your-gmail-username>
   GMAIL_PASSWORD=<your-gmail-password>

4. Run the FastAPI server:
   python -m uvicorn main:app --reload

Frontend

5. Navigate to the frontend directory:
   cd ../airline-frontend

6. Install the dependencies:
   npm install

7. Start the development server:
   npm run dev

Note
This project currently uses basic session management for user roles. In the future, we aim to implement JWT tokens for more secure and scalable session management and user role definitions.


   





