from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase

from dotenv import load_dotenv
import os

load_dotenv()


DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")  
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")



class Base(DeclarativeBase):
    pass


# DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# # DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5432/fastapi_db"

DATABASE_URL = "sqlite:///./DeliveryD.db"
Base = declarative_base()

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)


