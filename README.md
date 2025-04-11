# Event Management API

This project provides a Django-based REST API for managing events such as conferences and meetups. It includes full CRUD operations, user registration with JWT authentication, event registration, filtering and searching events, API documentation with Swagger (drf-yasg), and Docker support.

## Features

- **Event CRUD Operations:** Create, Read, Update, and Delete events.
- **User Registration & JWT Authentication:** Secure access using [SimpleJWT](https://github.com/jazzband/djangorestframework-simplejwt).
- **Event Registration:** Users can register for events.
- **Filtering and Searching:** Events can be filtered by date, location, and organizer using [django-filters](https://django-filter.readthedocs.io/en/stable/).
- **Swagger API Documentation:** Interactive API docs using [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/).
- **Email Notifications:** Send confirmation emails upon event registration.
- **Docker Support:** Easy deployment with Docker and Docker Compose.
- **Environment Configuration:** Use `.env` files for environment-specific settings.

## Project Structure

```
event_management/
├── manage.py
├── event_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── events/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── filters.py
│   └── tests.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd event_management
```

### 2. Running Locally (without Docker)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 3. Running with Docker

```bash
docker compose up --build
```

Access the API at `http://0.0.0.0:8000/api/`.  
Swagger UI available at `http://0.0.0.0:8000/swagger/`.

## API Endpoints Overview

| Method | Endpoint                      | Description                          |
|--------|-------------------------------|--------------------------------------|
| POST   | /api/token/                   | Obtain JWT token                    |
| POST   | /api/token/refresh/            | Refresh JWT token                   |
| GET    | /api/events/                  | List all events                     |
| POST   | /api/events/                  | Create a new event (authenticated)  |
| GET    | /api/events/{id}/             | Retrieve a single event             |
| PUT    | /api/events/{id}/             | Update an event (authenticated)     |
| DELETE | /api/events/{id}/             | Delete an event (authenticated)     |
| POST   | /api/events/{id}/register/    | Register for an event (authenticated)|
| GET    | /api/events-filter/           | Filter and search events            |

## Environment Variables (.env)

Example `.env`:

```env
SECRET_KEY=key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
DEFAULT_FROM_EMAIL=noreply@example.com

ACCESS_TOKEN_LIFETIME_MINUTES=5
REFRESH_TOKEN_LIFETIME_DAYS=1
ROTATE_REFRESH_TOKENS=False
BLACKLIST_AFTER_ROTATION=True
ALGORITHM=HS256
```

## Filtering Events

Filter events easily by adding query parameters:

- By Location: `/api/events-filter/?location=New York`
- By Date Range: `/api/events-filter/?date_from=2025-04-01&date_to=2025-05-01`
- Full-text Search: `/api/events-filter/?search=conference`

## Authentication

Authentication is handled with JWT tokens:

1. **Obtain Token:** POST to `/api/token/` with `username` and `password`.
2. **Use Access Token:** Add `Authorization: Bearer <access_token>` to your headers.
3. **Refresh Token:** POST to `/api/token/refresh/` with the `refresh` token.

## Technologies Used

- Django 5.2
- Django REST Framework
- SimpleJWT
- Django Filters
- drf-yasg (Swagger UI)
- Docker & Docker Compose
- PostgreSQL (in docker-compose)
- WhiteNoise

## License

This project is licensed under the MIT License.