from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from task_manager_api.routers import tasks, auth
from task_manager_api.database import init_db
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Starting Task Manager API...")

# Get App title 
app_title = os.getenv("APP_TITLE", "Task Manager API")

# init databas tabels
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

# Create FastAPI instance 
app = FastAPI(title=app_title, lifespan=lifespan)

# Include tasks router with prefix /tasks
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

# Global exception handler)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """
    Global exception handler
    """
    return JSONResponse(
        status_code=500,
        content={"message": f"Internal Server Error: {exc}"}
    )

@app.get("/")
def root():
    """
    Root endpoint
    Retrun welcome message 
    """
    return {"message": "Welcome to the task manager API"}
