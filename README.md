# FastAPI-Postgre Website Core Template

This project provides a basic template for building a FastAPI-based website with PostgreSQL integration. It includes essential components like authentication, database models, and API routing.

## Features

* **FastAPI framework** for high-performance web applications
* **PostgreSQL** as the database
* **Alembic** for database migrations
* **Docker & Docker Compose** for containerization
* **Async SQLAlchemy ORM** for efficient database interactions
* **User authentication** with JWT tokens
* **Pydantic** for request validation
* **Pre-configured project structure** for easy scalability

## Project Structure

```
.
├── .venv/                        # Virtual environment
├── shop-application/             # Source root
|   ├── alembic/                  # Alembic folder
|       ├── versions/             # Migration versions folder
|           └── .keep             # Keep empty dir file for git
|       └──env.py                 # Alembic environment
│   ├── api/                      # API routes
|        └── api_v1/              # First version of api
|            ├── crud/            # Crud operations folder
|                └──users.py      # Crud operations for user
|            └── users.py         # Routs for users
│   ├── core/                     # Core settings and configurations
|       ├── models/               # Db models folder
|           ├── mixins/           # Db mixins folder
|               └── int_id_pk.py  # Mixin for int primary key
|           ├── base.py           # Base db model
|           ├── db_helper.py      # Db helper
|           └── user.py           # User db model
|       ├── schemas/              # Schemas folder
|           └── user.py           # Schema for user
|       └── config.py             # Config file
|   ├── utils/                    # Utilities folder
|        └── case_converter.py    # Converter from camel case to snake case
|   ├── .env                      # Environment variables
|   ├── .env.template             # Template fo fill .env file
|   ├── alembic.ini               # Initial file for alembic
│   └── main.py                   # Main FastAPI app entry point
├── .gitignore                    # Gitignore file
├── docker-compose.yml            # Docker Compose configuration
├── poetry.lock                   # Poetry dependencies
├── pyproject.toml                # Project dependencies and settings
└── README.md                     # Project documentation

```

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/FASTAPI-POSTGRE_website_core_template.git
   ```
2. Navigate to the project folder:
   ```sh
   cd FASTAPI-POSTGRE_website_core_template
   ```
3. Create and activate a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Configure environment variables by copying `.env.example`:
   ```sh
   cp .env.example .env
   ```
6. Start the application using Docker:
   ```sh
   docker-compose up --build
   ```

## Usage

* Access the API documentation at `http://localhost:8000/docs`
* API requests can be made to `http://localhost:8000/api/v1/...`

## Contributing

Feel free to submit issues or pull requests to improve the project!
