from fastapi import FastAPI
from task_manager_api.routers import tasks
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get App title 
app_title = os.getenv("APP_TITLE", "Task Manager API")

# Create FastAPI instance 
app = FastAPI(title=app_title)

# Include tasks router with prefix /tasks
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    """
    Root endpoint
    Retrun welcome message 
    """
    return {"message": "Welcome to the task manager API"}