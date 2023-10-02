# CRUD
Consists of files with CRUD operations using Flask, SQLAlchemy

Baby Tracker Web Application
This is a simple web application built using Flask and SQLAlchemy for tracking baby-related events. It allows users to perform CRUD (Create, Read, Update, Delete) operations on baby events.

## Getting Started
These instructions will help you set up and run the application on your local machine.

## Prerequisites
Before you begin, make sure you have the following installed on your system:
Python (>= 3.6),
PostgreSQL,
pip (Python package manager),
Installing

### Clone the repository to your local machine:
git clone https://github.com/your-username/baby-tracker.git

### Navigate to the project directory:
cd baby-tracker

### Create a virtual environment (optional but recommended):
python -m venv venv
Activate the virtual environment:

### On Windows:
venv\Scripts\activate

### On macOS and Linux:
source venv/bin/activate

### Install the required Python packages:
pip install -r requirements.txt
Configure the Database:

### Open app.py and find the following line:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:newpassword@localhost/baby-tracker'
Replace 'postgresql://postgres:newpassword@localhost/baby-tracker' with your PostgreSQL database URI.

### Create the database tables and initialize the application context:
python app.py
Running the Application

### To run the Flask application, use the following command:
flask run
The application will start locally, and you can access it in your web browser at http://localhost:5000.

### Usage
The home page (/) displays a simple greeting message.

### Use the following endpoints for CRUD operations on baby events:
Create Event: POST /event
Get All Events: GET /event
Get Single Event: GET /event/<id>
Delete Event: DELETE /event/<id>
Update Event: PUT /event/<id>

# Contributing
Feel free to contribute to this project by opening issues or creating pull requests.


