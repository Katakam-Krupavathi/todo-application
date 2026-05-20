
# project : Create RESTful API endpoints to perform CRUD operations and containerize them.


##  Environment Setup:

Python Version: 3.11

Database:
- PostgreSQL 15

Containerization:
- Docker
- Docker Compose

## Folders / Files:

app/ -  Contains all application source code

main.py - Entry point of FastAPI application

database.py - Creates database engine and database sessions

models.py - Defines database tables using SQLAlchemy ORM

schemas.py - Defines request and response data models

crud.py - Contains CRUD database logic

requirements.txt - Stores required Python package

docker-compose.yaml → Manages FastAPI and PostgreSQL containers

Dockerfile - Defines instructions to build Docker image

##  How to run

1. Clone the repository

git clone <repository_url>
cd Mini-Project1


2. Build and start containers

docker compose up --build

3. Verify running containers

docker ps

Expected output:

fastapi_app
todo_postgres

After first build no rebuild is needed

docker compose up
docker compose down


4. Open API documentation in browser

http://localhost:8000/docs


5. Test API endpoints using Swagger UI

Available endpoints:

- POST /tasks → Create task
- GET /tasks → Fetch all tasks
- GET /tasks/{id} → Fetch task by ID
- PUT /tasks/{id} → Update task
- DELETE /tasks/{id} → Delete task

