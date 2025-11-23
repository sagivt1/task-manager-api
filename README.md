# task-manager-api
# Task Manager API

A simple and efficient RESTful API for managing tasks, built with Python.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Setup](#project-setup)
- [Database Migrations](#database-migrations)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

*   Create, Read, Update, and Delete (CRUD) operations for tasks.
*   List all tasks.
*   Fetch a single task by its ID.
*   Asynchronous from the ground up.
*   Database schema management with Alembic.

## Technologies Used

*   **Python 3.10+**
*   **FastAPI**: For building the high-performance API.
*   **SQLAlchemy**: For Object-Relational Mapping (ORM) to interact with the database.
*   **Alembic**: For handling database migrations.
*   **SQLite**: As the backend database, configured in `alembic.ini`.
*   **Uvicorn**: As the ASGI server to run the application.
*   **uv**: For dependency management.

## Project Setup

Follow these steps to get the project up and running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/sagivt1/task-manager-api
    cd task-manager-api
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    This project uses `uv` for dependency management based on the `pyproject.toml` file.
    ```bash
    # Install dependencies using uv
    uv sync
    ```

## Database Migrations

This project uses Alembic to manage database schema changes. The database URL is configured in `alembic.ini`.

*   **To create a new migration:**
    ```bash
    alembic revision --autogenerate -m "A descriptive message for the migration"
    ```

*   **To apply migrations:**
    ```bash
    alembic upgrade head
    ```

## Running the API

This project includes a `run.py` script to start the API server, which also handles loading environment variables from a `.env` file.

1.  **(Optional)** Create a `.env` file in the project root to configure the host and port. It defaults to `127.0.0.1:8000` if the file is not present.
    ```env
    APP_HOST=127.0.0.1
    APP_PORT=8000
    ```

2.  To start the API server, execute the `run.py` script:
    ```bash
    python run.py
    ```

The API will be available at the configured address (e.g., `http://127.0.0.1:8000`). You can access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

## API Endpoints

Here are the main endpoints provided by the API:

*   `GET /tasks`: Retrieve a list of all tasks.
*   `POST /tasks`: Create a new task.
*   `GET /tasks/{task_id}`: Retrieve a specific task by its ID.
*   `PUT /tasks/{task_id}`: Update an existing task.
*   `DELETE /tasks/{task_id}`: Delete a task.

## License

This project is licensed under the MIT License.
