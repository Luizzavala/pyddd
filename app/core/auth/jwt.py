import jwt
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta

from os import environ
from dotenv import load_dotenv
load_dotenv()


class AuthHandler():
    security= HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret= environ.get("SECRET_KEY")
    algorithms="HS256"
        
    def get_password_hash(self, password):
        return self.get_password_hash(password)
        
    def verify_password(self, plain_password, hased_password):
        return self.pwd_context.verify(plain_password, hased_password)
        
    def encode_token(self, user_id):
        payload={
            "exp": datetime.utcnow() + timedelta(days=360),
            "iat": datetime.utcnow(),
            "sub": user_id
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm=self.algorithms
        )
        
    def decode_token(self, token):
        try:
            payload = jwt.decode(token, key=self.secret, algorithms=self.algorithms)
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        
    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)