from enum import Enum
from datetime import timedelta

from fastapi import FastAPI, Depends, Form, HTTPException, status, Request
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from database import (addAnimal, addUser, getAllAnimals, getAnimals, getAscii,
                      getUserId_from_animal, getUsername_from_userId)
from auth import get_current_active_user, authenticate_user, create_access_token
from auth_config import ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, DATABASE_SECRET
from auth_models import Token, User

app = FastAPI()
templates = Jinja2Templates(directory="../templates/")

AnimalName = set(['fish', 'cat', 'rabbit', 'cow', 'dog'])

@app.get('/')
async def root(request: Request):
    result = None
    return templates.TemplateResponse('landing.html', context={'request': request, 'result': result})

@app.get('/animal/{animal_name}')
async def get_animal(request: Request, animal_name: str):
    if not animal_name in AnimalName:
        raise HTTPException(status_code=404, detail="Animal not found.")
    all_animals = getAllAnimals(animal_name)
    result = [{
            'ascii': animal['ascii'], 
            'animal': animal['name'],
            'artist': getUsername_from_userId(animal['userid'])
            } for animal in all_animals]
    return templates.TemplateResponse('animal.html', context={'request': request, 'result': result})

@app.get('/animal')
async def form_post(request: Request):
    result = "Which animal would you like to see?"
    return templates.TemplateResponse('search.html', context={'request': request, 'result': result})

@app.post('/animal')
async def form_post(request: Request, animal: str = Form(...)):
    result = getAscii(animal)
    return templates.TemplateResponse('search.html', context={'request': request, 'result': result})

@app.get('/signup')
async def form_post(request: Request):
    result = "Enter username and password"
    return templates.TemplateResponse('signup.html', context={'request': request, 'result': result})

@app.post('/signup')
async def form_post(request: Request, username: str = Form(...)):
    addUser(username)
    result = username
    return templates.TemplateResponse('signup.html', context={'request': request, 'result': result})

@app.get('/upload')
async def upload_post(request: Request):
    result = "Add an animal!"
    return templates.TemplateResponse('upload.html', context={'request': request, 'result': result})

@app.post('/upload')
async def upload_post(request: Request, animal: str = Form(...), artist: str = Form(...), ascii: str = Form(...)):
    result = addAnimal(animal, artist, ascii)
    return templates.TemplateResponse('upload.html', context={'request': request, 'result': result})

@app.get('/user/{username}')
async def get_animal(request: Request, username: str):
    result = {'username': username, 'animals': getAnimals(username)}
    return templates.TemplateResponse('user.html', context={'request': request, 'result': result})

@app.get('/token')
async def login_for_access_token(request: Request):
    result = "Enter username and password"
    return templates.TemplateResponse('login.html', context={'request': request, 'result': result})

@app.post('/token', response_model=Token)
#async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
async def login_for_access_token(request: Request, username: str = Form(...), password: str = Form(...)):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Incorrect username or password',
                headers={'WWW-Authenticate': 'Bearer'},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
            data={'sub': user.username}, expires_delta=access_token_expires
    )
    return {'access_token': access_token, 'token_type': 'bearer'}

#@app.get('/users/me/', response_model=User)
@app.get('/users/me/')
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    print(current_user)
    return current_user

@app.get('/users/me/animals/')
async def read_own_animals(request: Request, current_user: User = Depends(get_current_active_user)):
    result = {'username': current_user.username, 'animals': getAnimals(current_user.username)}
    return templates.TemplateResponse('user.html', context={'request': request, 'result': result})

