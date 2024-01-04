from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_
from database.db_api import DatabaseConnection
# load logscan object
from database.tableobject.scanned import Scanned

class Logscan(DatabaseConnection):
    def __init__(self):
        super().__init__()

    def insert_logscan(self, incharge: str, result: str,  **product_detail):
        try:
            scanned = Scanned()
            scanned.tv_model = product_detail.get("tv_model")
            scanned.remote_barcode = product_detail.get("remote_barcode")
            scanned.pic = incharge
            scanned.result = result
            self.session.add(scanned)
            self.session.commit()
            return True
        except IntegrityError as ie:
            print(str(ie))
            self.session.rollback()
            return False
        finally:
            self.session.close()

    def show_logs(self, search=None, limit: int = int, offset: int = int):
        query = self.session.query(Scanned)
        total_records = self.session.query(Scanned).count()
        if search:
            search = f"%{search}%"
            logs = query.filter(
                or_(
                    Scanned.tv_model.ilike(search),
                    Scanned.remote_name.ilike(search),
                    Scanned.result.ilike(search)
                )
            )
        data_logs = logs.limit(limit).offset(offset).all()
        retval = {"data_logs": data_logs, "total_records": total_records}
        return retval
    
    