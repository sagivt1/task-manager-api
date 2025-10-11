from fastapi import FastAPI
from task_manager_api.routers import tasks

app = FastAPI(title="Task Manager API")

app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    """
    Root endpoint
    Retrun welcome message 
    """
    return {"message": "Welcome to the task manager API"}