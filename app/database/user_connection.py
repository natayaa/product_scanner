from sqlalchemy.exc import IntegrityError

# import api db
from database.db_api import DatabaseConnection
# import table object for user
from database.tableobject.user import User

# import password verify
from utilities.pw_verif import PasswordVerification
# init pw ver
pw_ver = PasswordVerification()

class UserConnection(DatabaseConnection):
    def __init__(self):
        super().__init__()

    def register_user(self, **payload):
        try:
            user = User()
            user.username = payload.get("username")
            user.password = pw_ver.hash_password(payload.get("password"))
            user.role = payload.get("role")
            user.level = payload.get("level")
            user.is_active = 1
            self.session.add(user)
            self.session.commit()
            return True
        except IntegrityError as ie:
            self.session.rollback()
            print(ie)
            return False
        
    def get_user(self, username: str):
        user = self.session.query(User).filter_by(username=username).first()
        if user:
            return user
        elif user.is_active == 0:
            return False
        else:
            return None
        
    def user_authenticate(self, username: str, password: str):
        user = self.get_user(username)
        if not user:
            return False
        if not PasswordVerification.verify_password(password, user.password):
            return False
        
        return user
    
    def delete_user(self, user_id: int):
        try:
            query = self.session.query(User).filter_by(user_id=user_id).first()
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
        
    def update_user(self, user_id: int, **payload_edit):
        pass