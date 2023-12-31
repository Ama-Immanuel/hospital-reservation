import os 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

POSTGRES_USER=os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD=os.getenv("POSTGRES_USER")
POSTGRES_SERVER=os.getenv("POSTGRES_SERVER")
POSTGRES_PORT=os.getenv("POSTGRES_PORT")
POSTGRES_DB=os.getenv("POSTGRES_DB")

