
from database.db import SessionLocal
# import tables object
from database.tableobject.user import User

class DatabaseConnection:
    def __init__(self):
        self.session = SessionLocal()

