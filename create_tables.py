from models import Base
from connect import engine

print("CREATING DATABASE >>>> ")
Base.metadata.create_all(bind=engine)