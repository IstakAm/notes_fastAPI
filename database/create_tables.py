from utils.database.models import Base
from utils.database.connect import engine

print("CREATING DATABASE >>>> ")
Base.metadata.create_all(bind=engine)