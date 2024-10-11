# Task Management System

A real-time **Task Management System** built using **Django** for the backend and **React 18** for the frontend. The system leverages **Django Channels**, **WebSockets**, and **Redis** to provide real-time task updates and notifications. The frontend is styled using **Material UI**, offering a modern, responsive interface.

## Features

- **Task Management**: Create, update, and view tasks.
- **Notifications**: Real-time notifications for task updates using WebSockets.
- **Material UI**: Modern, responsive design with Material UI components.
- **Real-Time WebSockets**: Live task updates via WebSockets integrated with Django Channels.
- **API-Driven**: Uses Django REST Framework for API endpoints.
- **React 18**: Implements React 18 with concurrent features.
- **Docker**: Containerized deployment using Docker and Docker Compose.

## Technologies Used

### Backend (Django)

- **Django** (v4.2) - Web framework
- **Django REST Framework** - API development
- **Django Channels** - WebSocket handling
- **Redis** - In-memory database for caching and WebSockets
- **PostgreSQL** - Relational database
- **Gunicorn** - WSGI server for deployment

### Frontend (React 18)

- **React 18** - JavaScript library for building user interfaces
- **Material UI** - React component library for styling
- **WebSockets** - Real-time communication
- **Axios** - HTTP client for API requests

## Prerequisites

Make sure you have the following tools installed:

- **Node.js** (v16 or above)
- **npm** or **yarn**
- **Python** (v3.9 or above)
- **Docker** (optional, for containerized deployment)
- **PostgreSQL** (or use Docker for the database)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/task-management-system.git
cd task-management-system
```

### 2. Backend Setup (Django)

1. Navigate to the `backend` folder:

```bash
cd backend
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the PostgreSQL database (update the database settings in `settings.py` as needed).
5. Apply migrations:

```bash
python manage.py migrate
```

6. Start the Django development server:

```bash
python manage.py runserver
```

### 3. Frontend Setup (React)

1. Navigate to the `frontend` folder:

```bash
cd ../frontend
```

2. Install the required dependencies:

```bash
npm install
```

3. Start the React development server:

```bash
npm start
```

### 4. Running with Docker (Optional)

If you'd like to run the app using Docker, you can use Docker Compose:

1. Make sure Docker is installed and running.
2. In the root directory, run:

```bash
docker-compose up --build
```

Docker Compose will build and start the backend, frontend, and PostgreSQL database containers.

### 5. WebSocket Setup

Ensure Redis is installed and running. For development, you can install Redis locally or run it via Docker:

```bash
docker run -p 6379:6379 redis
```

Redis is required for Django Channels to handle WebSockets.

## Project Structure

```
backend/
├── manage.py
├── task_management_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
frontend/
├── src/
│   ├── App.js
│   ├── index.js
│   ├── components/
│   │   ├── TaskList.js
│   │   ├── NotificationList.js
│   └── WebSocketComponent.js
```

- **Backend** (`backend/`): Django project files.
- **Frontend** (`frontend/`): React project files.
- **Docker** (`docker-compose.yml`): Docker Compose configuration for running the app.

## API Endpoints

The backend uses **Django REST Framework** to provide API endpoints for managing tasks and notifications.

- `GET /tasks/` - Retrieve all tasks
- `POST /tasks/` - Create a new task
- `GET /notifications/` - Retrieve all notifications

## WebSocket Communication

WebSocket endpoints are provided for real-time updates. Tasks are broadcast to clients whenever there is a change in their status.

- WebSocket URL: `ws://localhost:8000/ws/tasks/`

## Deployment

You can deploy the app using Docker, or deploy the backend and frontend separately. For production, make sure to:

1. Use a production WSGI server like Gunicorn.
2. Use Nginx as a reverse proxy.
3. Ensure the React frontend is built with `npm run build` and served statically.

## License

This project is licensed under the MIT License.
