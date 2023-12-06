from sqlalchemy.orm import Session
from app.models.userModel import User
from app.schemas.userSchema import UserSchema

def find_by_username(query_db:Session,query_model:User,username:str)-> UserSchema:
    return query_db.query(query_model).filter(query_model.username == username).first()