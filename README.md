# Healthcare Backend

A Django-based RESTful API for managing healthcare records with JWT authentication.

# Healthcare Backend API

A secure, RESTful backend system built with **Django**, **Django REST Framework (DRF)**, and **PostgreSQL** for managing healthcare records. This project implements user authentication with **JWT (JSON Web Tokens)**, patient and doctor management, and patient-doctor mappings. It follows best practices for Django development, including environment variable usage, proper error handling, and clean code structure.

---

## Features
- **User Authentication**: Register and log in users with JWT-based authentication.
- **Patient Management**: CRUD operations for patient records (restricted to authenticated users).
- **Doctor Management**: CRUD operations for doctor records.
- **Patient-Doctor Mapping**: Assign doctors to patients and retrieve mappings.
- **Security**: JWT token-based authentication for all protected endpoints.
- **Database**: PostgreSQL for persistent storage.
- **API Testing**: Fully testable with Postman or any API client.



## Tech Stack
- **Backend**: Django 4.2, Django REST Framework
- **Authentication**: djangorestframework-simplejwt
- **Database**: PostgreSQL
- **Environment**: python-dotenv for managing sensitive configurations
- **Testing**: Postman (or any API client)

### Prerequisites
- Python 3.8+
- PostgreSQL installed and running
- Postman (for testing APIs)
- Git

## Setup

1. Clone the repo: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up PostgreSQL and update `.env` with your credentials.
4. Run migrations: `python manage.py makemigrations && python manage.py migrate`
5. Create superuser: `python manage.py createsuperuser`
6. Start server: `python manage.py runserver`

**Create .env file**:
    ```base
    SECRET_KEY=your-secret-key-here
    DEBUG=True
    DB_NAME=healthcare_db
    DB_USER=your_postgres_user
    DB_PASSWORD=your_postgres_password
    DB_HOST=localhost
    DB_PORT=5432


1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd healthcare_backend
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
