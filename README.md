# Building Booking System

Welcome to the Building Booking System project! This Django-based application is designed to provide a comprehensive solution for managing room bookings in a building. Whether you're scheduling events, meetings, or any other activities that require space, this system makes the process seamless and efficient.

## Features

1. **User-friendly Interface:** The application provides an intuitive user interface that allows users to easily navigate and book rooms.

2. **Booking Options:** Users can make both soft and hard bookings based on their needs. Soft bookings act as reservations, while hard bookings are confirmed and require payment.

3. **Payment Integration:** Seamless payment integration ensures secure transactions for confirmed bookings. Users can choose from various payment options.

4. **Flexible Scheduling:** The scheduling system allows users to view room availability and select suitable time slots for their bookings.

5. **User Authentication:** Secure user authentication ensures that only authorized individuals can make bookings, view schedules, and perform administrative tasks.

## Installation

To get started with the Building Booking System, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/building-booking-system.git
   cd building-booking-system
	```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
	```
3. **Run Migrations:**
   ```bash
   python manage.py migrate
	```
4. **Create Superuser (Admin):**
   ```bash
   python manage.py createsuperuser
	```
5. **Run the Development Server:**
   ```bash
   python manage.py runserver
	```
6. **Access the Application:**
Open your web browser and navigate to http://localhost:8000 to access the Building Booking System.

## Usage

1. **Login:**
   - Use the superuser credentials created earlier to log in as an administrator.

2. **Manage Rooms:**
   - Add, edit, or delete rooms in the admin interface.

3. **Booking:**
   - Users can log in, view available rooms, and make bookings. Payment is required for confirmed (hard) bookings.

4. **View Schedule:**
   - Users can check the schedule to see room availability and upcoming bookings.
