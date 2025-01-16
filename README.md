# Task App

// ...existing code...

## Instructions to run migrations and run the application locally

1. Open a terminal and navigate to the project directory.
2. Run the following command to apply the migrations:
   ```bash
   python manage.py migrate
   ```
3. Start the local development server with the following command:
   ```bash
   python manage.py runserver
   ```
4. Open your web browser and navigate to `http://127.0.0.1:8000/` to see the application running.

// ...existing code...

## Instructions to build and run the Docker container

1. Open a terminal and navigate to the project directory.
2. Build the Docker image with the following command:
   ```bash
   docker build -t task-app .
   ```
3. Run the Docker container with the following command:
   ```bash
   docker run -p 8000:8000 task-app
   ```
4. Open your web browser and navigate to `http://127.0.0.1:8000/` to see the application running.

// ...existing code...

## Instructions to use Docker Compose

1. Open a terminal and navigate to the project directory.
2. Run the following command to start the services:
   ```bash
   docker-compose up --build
   ```
3. Open your web browser and navigate to `http://127.0.0.1:8000/` to see the application running.
