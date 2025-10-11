from fastapi import FastAPI

app = FastAPI(title="Task Manager API")

@app.get("/")
def root():
    """
    Root endpoint
    Retrun welcome message 
    """
    return {"message": "Welcome to the task manager API"}