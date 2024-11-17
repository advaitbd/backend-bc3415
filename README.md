<p align='center'>
<img width="600" alt="image" src="https://github.com/user-attachments/assets/46dc76cc-288b-49ef-a81d-c8c5ccda7586">
</p>

<h2 align="center">FinAdvisor</h2>

<p align="center">
    <a href="https://github.com/advaitbd/frontend-bc3415">Frontend</a>
    |
    <a href="https://github.com/advaitbd/backend-bc3415">Backend</a>
</p>

# FinAdvisor-Backend

This is the backend repository for FinAdvisor.

### Getting Started

# Project Setup and Database Migration Guide

This guide provides step-by-step instructions to set up your project, configure the database, and manage database migrations using Alembic and Docker.

## Prerequisites

Ensure you have the following installed on your system:
- Python (preferably 3.6+)
- Docker
- Docker Compose

## Installation and Setup

### Step 1: Install Alembic

First, install Alembic, a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.

```sh
pip install alembic
```
### Step 2: Configure Database URL

#### Update `alembic.ini`

Set the SQLAlchemy URL in the `alembic.ini` file to point to your local PostgreSQL instance.

```ini
# alembic.ini
[alembic]
sqlalchemy.url = postgresql://postgres:postgres@localhost:5432/postgres
```

#### Set your `.env` File

Create a `.env` file in the root directory of your project and add the following environment variables.

```env
# .env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/postgres
SECRET_KEY=[Ask Advait]
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
OPENAI_API_KEY=[Get your own!]

```

### Step 3: Build and Run the Database

Use Docker Compose to build and run the PostgreSQL database container.

```sh
docker-compose up -d db
```

### Step 4: Generate the Initial Migration

Generate the initial database migration script using Alembic.

```sh
alembic revision --autogenerate -m "Initial migration"
```

### Step 5: Apply the Migration

Apply the generated migration to update the database schema.

```sh
alembic upgrade head
```

### Step 6: Update Database URLs for Docker

After applying the migration, update the database URLs to point to the Docker container.

```sh
set sqlalchemy.url=postgresql://postgres:postgres@db:5432/postgres
set DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
```

### Step 7: Build and Run Docker Containers

Build and run the Docker containers for your application.

```sh
docker-compose up -d --build
```

### Step 8: Stop the Database Container

When you are done, stop the database container.

```sh
docker-compose down
```
