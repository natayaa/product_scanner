from sqlalchemy import Integer, String, Column
from database.db import Base

from datetime import datetime

class Products(Base):
    __tablename__ = "tb_product_items"

    item_id = Column(Integer, autoincrement=True, primary_key=True)
    tv_model = Column(String, nullable=False)
    remote_barcode = Column(String, nullable=False)
    insert_by = Column(String)
    date_added = Column(String, default=datetime.now().strftime("%Y-%m-%d"))
    timestamp = Column(String, default=datetime.now().strftime("%H:%M"))
