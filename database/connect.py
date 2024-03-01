from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

c_string = os.getenv('DATABASE_URL')
username = 'postgres'
password = 'postgres'
host = 'localhost'  # or the IP address/hostname of your PostgreSQL server
port = '5434'  # default PostgreSQL port
database = 'firstapi'

# Construct the connection string
connection_string = "postgresql://postgres:postgres@notes_db:5432/firstapi"
print(connection_string)

engine = create_engine(connection_string, echo=True)
