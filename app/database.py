from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os


 # to create sessions  to interact with databses

DATABASE_URL = os.getenv("DATABASE_URL")   # it tells the alchemy to connect to postgres database



engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)   # this is the main part,it is connection object , that starts the process 

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine) # it creates the sessions

Base = declarative_base() 


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


