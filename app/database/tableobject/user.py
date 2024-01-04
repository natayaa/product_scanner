from sqlalchemy import Integer, String, Column
from database.db import Base

from datetime import datetime


class User(Base):
    __tablename__ = "tb_users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, default=None)
    password = Column(String)
    role = Column(String)
    level = Column(Integer, default=100)
    is_active = Column(Integer, default=1)
    date_created = Column(String, default=datetime.now().strftime("%Y-%m-%d"))