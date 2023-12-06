from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.config import get_db
from app.schemas.userSchema import UserSchema
from app.helper.util import find_by_username
from app.models.userModel import User 


router = APIRouter()

@router.get("/", tags=["Get All User"])
async def index(db:Session = Depends(get_db)):
    return {"mess": "hello"}

@router.post("/", tags=["Create User"])
async def __store__(user:UserSchema, db:Session = Depends(get_db)):
    try:
        isUser = find_by_username(db, user, user.username)
        print(isUser)
    except Exception as err:
        print(err)