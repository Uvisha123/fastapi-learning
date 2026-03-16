# FastAPI Backend API

## Project Description

This project is a **RESTful backend API built with FastAPI** as part of a backend development course.
It implements user authentication, CRUD operations, database integration, and secure API access using JWT tokens.

The application allows users to register, log in, create posts, vote/like posts, and perform various database operations through a REST API.

The goal of this project was to learn **modern backend development with Python and FastAPI**, including database management, authentication, and testing.

---

# Tech Stack

### Backend

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* Alembic

### Database

* PostgreSQL

### Authentication

* JWT (JSON Web Tokens)
* OAuth2 Password Flow
* Password hashing (bcrypt)

### Tools

* Postman (API testing)
* PgAdmin (database management)
* Pytest (testing)

### Development Tools

* VS Code
* Git
* GitHub

---

# Features

### User Management

* User registration
* Password hashing
* User authentication
* Login with JWT tokens

### Posts

* Create posts
* Retrieve all posts
* Retrieve a single post
* Update posts
* Delete posts

### Authorization

* Only authenticated users can access protected routes
* Users can only modify their own posts

### Voting System

* Like/Vote for posts
* Remove vote from posts
* Prevent duplicate votes

### Database

* PostgreSQL relational database
* Foreign key relationships
* SQL joins
* Database migrations using Alembic

### API Documentation

FastAPI automatically generates API documentation:

* `/docs` (Swagger UI)
* `/redoc`

---

# Project Structure

```
app
 ├── routers
 │    ├── auth.py
 │    ├── users.py
 │    ├── posts.py
 │    └── vote.py
 │
 ├── models
 │    ├── user.py
 │    ├── post.py
 │    └── vote.py
 │
 ├── schemas
 │    ├── user.py
 │    ├── post.py
 │    └── vote.py
 │
 ├── database.py
 ├── oauth2.py
 ├── utils.py
 └── main.py
```

---

# Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=yourpassword
DATABASE_NAME=fastapi
DATABASE_USERNAME=postgres

SECRET_KEY=yoursecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Database Setup

Install PostgreSQL and create a database.

Then run migrations:

```bash
alembic upgrade head
```

---

# Running the Application

Start the server:

```bash
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Authentication

| Method | Endpoint | Description              |
| ------ | -------- | ------------------------ |
| POST   | /login   | Login user and get token |

## Users

| Method | Endpoint    | Description    |
| ------ | ----------- | -------------- |
| POST   | /users      | Create user    |
| GET    | /users/{id} | Get user by ID |

## Posts

| Method | Endpoint    | Description    |
| ------ | ----------- | -------------- |
| GET    | /posts      | Get all posts  |
| GET    | /posts/{id} | Get post by ID |
| POST   | /posts      | Create post    |
| PUT    | /posts/{id} | Update post    |
| DELETE | /posts/{id} | Delete post    |

## Votes

| Method | Endpoint | Description           |
| ------ | -------- | --------------------- |
| POST   | /vote    | Like or unlike a post |

---

# Testing

Testing is implemented using **pytest**.

Run tests using:

```bash
pytest
```

Testing includes:

* User creation tests
* Authentication tests
* Token validation tests
* Post CRUD tests

---

# Deployment

The project includes configuration examples for deployment to a Linux server using:

* Gunicorn
* NGINX
* PostgreSQL

Docker and CI/CD pipelines were **not implemented in this version of the project**.

---

# Learning Objectives

This project helped practice:

* REST API design
* Authentication & authorization
* Database design
* SQL joins
* ORM usage
* API testing
* Backend project structure

---

# Author

Uvisha Fernando
Software Engineering Student

---

# License

This project is for educational purposes.
