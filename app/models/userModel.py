from app.models.baseModel import BaseModel
from sqlalchemy import Column, String

class User(BaseModel):
    __tablename__ ="Users"

    name = Column(String(256), nullable=True)
    username = Column(String(256), unique=True)
    email = Column(String(256), unique=True)
    password = Column(String(256))

def before_hash_password(mapper, connection,target:User):
    """
    TODO: Hash password before create
    """