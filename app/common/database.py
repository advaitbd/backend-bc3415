from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databases import Database
from app.common.config import settings
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = settings.DATABASE_URL
database = Database(DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Define the Base class
Base = declarative_base()
