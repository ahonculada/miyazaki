from enum import Enum

from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.templating import Jinja2Templates

from database import (addAnimal, addUser, getAllAnimals, getAnimals, getAscii,
                      getUserId_from_animal, getUsername_from_userId)
from auth.config import ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, DATABASE_SECRET

app = FastAPI()
templates = Jinja2Templates(directory="../templates/")

AnimalName = set(['fish', 'cat', 'rabbit', 'cow', 'dog'])

@app.get('/')
async def root(request: Request):
    result = None
    print(ALGORITHM)
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
