from sqlalchemy import Column, String, Integer
from database.db import Base
from datetime import datetime

class Scanned(Base):
    __tablename__ = "tb_scanned"

    scan_id = Column(Integer, autoincrement=True, primary_key=True)
    tv_model = Column(String, nullable=False)
    remote_barcode = Column(String, nullable=False)
    pic = Column(String, nullable=False)
    result = Column(String)
    scanned_date = Column(String, default=datetime.now().strftime("%Y-%m-%d, %HH:%MM"))