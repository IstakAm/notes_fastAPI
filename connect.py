from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

username = 'postgres'
password = 'postgres'
host = 'localhost'  # or the IP address/hostname of your PostgreSQL server
port = '5432'  # default PostgreSQL port
database = 'firstapi'

# Construct the connection string
connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'
print(connection_string)

engine = create_engine(connection_string, echo=True)
