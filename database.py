from sqlalchemy import create_engine
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()