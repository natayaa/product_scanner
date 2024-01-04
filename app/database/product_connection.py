from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_
from sqlalchemy.orm import defer

# load object table
from database.tableobject.product_template import Products
# load database dependent
from database.db_api import DatabaseConnection

class ProductConnection(DatabaseConnection):
    def __init__(self):
        super().__init__()

    def check_data(self, tv_model_input, remote_barcode_input):
        try:
            query = self.session.query(Products).filter_by(tv_model=tv_model_input, remote_barcode=remote_barcode_input).first()
            if query:
                return True
            else:
                return False
        except IntegrityError as ie:
            print(str(ie))
            self.session.close()
            return None

    async def listing_model(self):
        tv_model = self.session.query(Products.tv_model, Products.tv_barcode).all()
        return tv_model

    def add_product(self, username, **product_detail):
        try:
            product = Products()
            product.tv_model = product_detail.get("tv_model")
            product.tv_barcode = product_detail.get("tv_barcode")
            product.remote_name = product_detail.get("remote_name")
            product.remote_barcode = product_detail.get("remote_barcode")
            product.insert_by = username
            self.session.add(product)
            self.session.commit()
            return True
        except IntegrityError as ie:
            print(ie)
            self.session.rollback()
            return False
        finally:
            self.session.close()

    # to listing all registered data from database
    def product_show(self, search=None, limit=int, offset=int):
        try:
            total_products = self.session.query(Products).count()
            products = self.session.query(Products)
            if search:
                search = f"%{search}%"
                product_records = products.filter(
                    or_(
                        Products.tv_model.ilike(search),
                        Products.remote_name.ilike(search)
                    )
                )
            products_list = product_records.limit(limit).offset(offset).all()
            retval = {"product_list": products_list, "total_products": total_products}
            return retval
        except IntegrityError as ie:
            print(str(ie))
            self.session.rollback()
            return False        

    def delete_product(self, item_id: int):
        try:
            query = self.session.query(Products).filter_by(item_id=item_id).first()
            if query:
                self.session.delete(query)
                self.session.commit()
                return True
            else:
                return False
        except IntegrityError as ie:
            print(str(ie))
            self.session.rollback()
            return False
        finally:
            self.session.close()