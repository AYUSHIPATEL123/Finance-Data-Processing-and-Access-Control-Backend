# Finance Data Processing & Role Access Control Backend

A robust backend application built with Python and FastAPI designed to handle finance data processing while enforcing strict Role-Based Access Control (RBAC). This API ensures secure data handling, user authentication, and organized management of financial records.

<br>

## 🚀 Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Database ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
* **Database Migrations:** [Alembic](https://alembic.sqlalchemy.org/)
* **Language:** Python 3.9+
* **Database:** MySQL
<br>

## 📂 Project Structure

The project follows a modular structure for better scalability and separation of concerns:

```text
Finance-Data-Processing-Role-Access-Control-Backend/
│
├── alembic/                # Alembic migration environment and script templates
├── models/                 # SQLAlchemy database models (tables schema)
├── routers/                # FastAPI API route handlers/endpoints
├── schemas/                # Pydantic models for request/response validation
├── services/               # Core business logic and database CRUD operations
│
├── .gitignore              # Files and directories ignored by Git
├── alembic.ini             # Alembic configuration file
├── database.py             # Database connection and session management setup
├── main.py                 # FastAPI application entry point
└── requirements.txt        # Python dependencies
```
<br>

## ⚙️ Local Setup & Installation
Follow these steps to get the project running locally.

### 1. Clone the repository
```Bash
git clone [https://github.com/AYUSHIPATEL123/Finance-Data-Processing-Role-Access-Control-Backend.git](https://github.com/AYUSHIPATEL123/Finance-Data-Processing-Role-Access-Control-Backend.git)
cd Finance-Data-Processing-Role-Access-Control-Backend
```

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage your dependencies.

```Bash
pip install uvicorn
uv venv
```
#### On Windows:
```
.venv\Scripts\activate
```
#### On macOS/Linux:
```
source .venv/bin/activate
```
### 3. Install Dependencies
```Bash
uv pip install -r requirements.txt
```
### 4. Configure Environment Variables
Ensure you update your database.py or .env file with your database connection string (e.g., PostgreSQL, MySQL, or SQLite).
Example Database URL format:
#### SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"                     

<br>

## 🗄️ Alembic Setup & Database Migrations
Alembic is used to track and apply database schema changes.

### Step 1: Initialize Alembic (If not already initialized)
(Note: Since the alembic folder is already in the repo, you likely skip this step, but it is here for reference).

```Bash
alembic init alembic
```

### Step 2: Configure alembic.ini and env.py
Open alembic.ini and ensure the sqlalchemy.url points to your database (or configure it dynamically to read from your app's database.py).

In alembic/env.py, ensure you import your SQLAlchemy Base and set target_metadata:

Python
from models.base import Base # Adjust import based on your exact structure

#### target_metadata = Base.metadata

### Step 3: Create a Migration Revision
Whenever you make changes to your SQLAlchemy models in the models/ directory, you need to generate a new migration script:

```Bash
alembic revision --autogenerate -m "Initial migration or description of changes"
```

### Step 4: Apply Migrations to Database
Run the following command to apply the generated migrations and create the tables in your database:

```Bash
alembic upgrade head
```
(To rollback the last migration, you can use: alembic downgrade -1)

<br>

## 🏃‍♂️ Running the Application
Start the FastAPI server using Uvicorn:

```Bash
uvicorn main:app --reload
```
The API will be running locally at: http://127.0.0.1:8000

Interactive API Documentation
FastAPI automatically generates interactive API documentation. Once the server is running, you can visit:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc
