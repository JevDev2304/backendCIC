from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_LINK = os.getenv("DATABASE_LINK")

engine = create_engine(DATABASE_LINK, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
