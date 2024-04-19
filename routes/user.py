from fastapi import APIRouter, Depends
from bson.objectid import ObjectId
from serializers.userSerializers import userResponseEntity

from config.database import User
from config import  oauth2
from schemas import users

router = APIRouter()


@router.get('/me', response_model=users.UserResponse)
def get_me(user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
    return {"status": "success", "user": user}

