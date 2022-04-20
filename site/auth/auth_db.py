from datetime import datetime, timedelta
from typing import Optional
from unicodedata import name

import pymongo
from bson.objectid import ObjectId
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from auth_models import Token, TokenData, User, UserInDB

with open('../../secrets.txt') as data:
    password = ''.join(data.readlines())[:-1]

client = pymongo.MongoClient(f"mongodb+srv://miyazaki:{ password }@miyazaki-cluster-1.qhpgx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

def get_user(username: str) -> User:
    mydb = client['Miyazaki-db']
    user_collection = mydb['users']
    user = user_collection.find_one({"name":username})
    if user:
        return user
    
    return None


if __name__ == '__main__':
   print( get_user('kanye'))
