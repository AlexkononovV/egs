from sqlalchemy.orm import Session
from passlib.context import CryptContext
import bcrypt

import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password, bcrypt.gensalt())

def get_user(db: Session, username: str):
    print(db.query(models.User).filter(models.User.username == username).first() , 2)
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.User):
    db_user = schemas.UserInDB(email=user.email, username=user.username , hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
