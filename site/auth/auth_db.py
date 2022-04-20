from datetime import datetime, timedelta
from typing import Optional
from unittest.mock import Base

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from auth_models import Token, TokenData, User, UserInDB

from unicodedata import name

import pymongo
from bson.objectid import ObjectId

with open('../../secrets.txt') as data:
    password = ''.join(data.readlines())[:-1]

client = pymongo.MongoClient(f"mongodb+srv://miyazaki:{ password }@miyazaki-cluster-1.qhpgx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str) -> User:
    mydb = client['Miyazaki-db']
    user_collection = mydb['users']
    user = user_collection.find_one({"name":username})
    new_user = User(username= user['name'], animals= user['animals'], hashed_password=user['hashed_password'])
    if user:
        return new_user
    
    return None


if __name__ == '__main__':
   print( get_user('kanye'))