from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from decouple import config

import os

if not os.path.exists("database/database-scanner.sqlite3"):
    open("database-scanner.sqlite3", "w").close()

engine = create_engine(config("SQLHOST"), echo=False)
Base = declarative_base()
SessionLocal = sessionmaker(autoflush=False, bind=engine)

def call_database() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()