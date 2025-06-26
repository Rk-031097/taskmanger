# Task Manager API

This a Task mangement project here user can register and login and create tasks and he can also update and delete.

**Project structure:**
- `taskmanager/` — Django project root
- `tasks/` — Main app with models, views, serializers, and tests

## Features
- User registration and JWT login
- Task CRUD (Create, Read, Update, Delete)
- Token-based authentication (SimpleJWT)
- API documentation with Swagger (drf-yasg)

## Requirements
- Python 3.11+
Install all dependencies with:

```
pip install -r requirements.txt
```

## Setup
1. **Apply migrations:**
   ```
   python manage.py migrate
   ```
2. **Run the development server:**
   ```
   python manage.py runserver
   ```

## API Endpoints
- `POST /api/register/` — Register a new user
- `POST /api/login/` — Obtain JWT token
- `POST /api/refresh/` — Refresh JWT token
- `GET /api/tasks/` — List tasks (auth required)
- `POST /api/tasks/` — Create task (auth required)
- `GET /api/tasks/{id}/` — Retrieve task (auth required)
- `PATCH /api/tasks/{id}/` — Update task (auth required)
- `DELETE /api/tasks/{id}/` — Delete task (auth required)

## Running Tests
Run all API and unit tests with:

```
python manage.py test tasks
```

## API Documentation
OpenAPI docs available at `/docs/` when the server is running.


