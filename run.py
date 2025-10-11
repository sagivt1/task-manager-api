from uvicorn import run
from dotenv import load_dotenv
import os
import sys

# Add src to Python path
sys.path.append("src")

# Load from .env
load_dotenv()

# get host and port from the environment and adding defaults
host = os.getenv("APP_HOST", "127.0.0.1")
port = int(os.getenv("APP_PORT", 8000))



if __name__ == "__main__":
    # Start FastAPI
    run("task_manager_api.main:app", host=host, port=port, reload=True)    