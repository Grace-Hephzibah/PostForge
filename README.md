# PostForge
## Environment Setup
Follow these steps to set up your environment for the project:
1. **Clone the GitHub Repository Locally:** Begin by cloning the project's GitHub repository to your local machine.
2. **Create a Virtual Environment:** Create a virtual environment to isolate project dependencies.
```python -m venv venv```
3. **Install Required Libraries:** Install the necessary Python libraries by running the following command:
```pip install -r requirements.txt```
4. **Database Configuration:** Modify the database settings in the ```app/test.env``` file to match your setup.
5. **Initialize the Application:** Start the application using Uvicorn with auto-reloading.
```uvicorn app.main:app --reload```

## Endpoints
The application exposes the following endpoints:

1. **Test Endpoint (GET):** A test endpoint to check if the application is running successfully.
```URL: /```
2. **Access All Posts (GET):** Retrieve all posts from the database.
```URL: /posts```
3. **Create a New Post (POST):** Add a new post to the database.
```URL: /createposts```
4. **Get a Specific Post (GET):** Retrieve a specific post by its ID.
```URL: /posts/{id}```
5. **Delete a Specific Post (DELETE):** Remove a specific post by its ID.
```URL: /posts/{id}```
6. **Update a Specific Post (PUT):** Modify a specific post by its ID.
```URL: /posts/{id}```

## Tech Stack
The application is built using the following technologies:
### Backend Framework:
- **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python.
- **Pydantic:** A data validation and parsing library.
- **SQLAlchemy:** A SQL toolkit and Object-Relational Mapping (ORM) for Python.
- **Uvicorn:** An ASGI server to run your FastAPI application.
### Database:
- **Postgres:** A powerful, open-source relational database management system.
