from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

# Load from .env
load_dotenv()

database_url = os.getenv("DATABASE_URL", "sqlite:///./tasks.db")

engine = create_engine(database_url, echo=True)

def init_db():
    """
    create all databses tables define by sql classes
    """
    SQLModel.metadata.create_all(engine)

def get_session():
    """
    Provide a session (connection) to the database for each request
    """
    with Session(engine) as session:
        yield session