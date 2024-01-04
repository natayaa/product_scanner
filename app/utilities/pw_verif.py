from passlib.context import CryptContext

class PasswordVerification:
    def __init__(self):
        self.password_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

    def hash_password(self, password: str):
        return self.password_context.hash(password)
    
    def verify_password(self, password: str, hashed_password: str):
        return self.password_context.verify(password, hashed_password)