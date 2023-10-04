from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import POSTGRES_PORT, POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_SERVER, POSTGRES_USER


URL = "postgresql://"+POSTGRES_USER+":"+POSTGRES_PASSWORD+"@"+POSTGRES_SERVER+":"+POSTGRES_PORT+"/"+POSTGRES_DB

engine = create_engine(URL)

Session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = Session_local()
    try:
        yield db
    finally:
        db.close()