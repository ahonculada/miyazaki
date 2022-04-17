from enum import Enum
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from database import getAscii, getAnimals, getUserId_from_animal, getUsername_from_userId

app = FastAPI()
templates = Jinja2Templates(directory="../templates/")

# TODO generalize this class
#class AnimalName(str, Enum):
#    fish = 'fish'
#    cat = 'cat'
#    rabbit = 'rabbit'
#    cow = 'cow'
#    dog = 'dog'
AnimalName = set(['fish', 'cat', 'rabbit', 'cow', 'dog'])

@app.get('/')
async def root(request: Request):
    result = None
    return templates.TemplateResponse('landing.html', context={'request': request, 'result': result})

@app.get('/animal/{animal_name}')
async def get_animal(request: Request, animal_name: str):
    if not animal_name in AnimalName:
        raise HTTPException(status_code=404, detail="Animal not found.")
    result = {
            'ascii': getAscii(animal_name), 
            'animal': animal_name,
            'artist': getUsername_from_userId(getUserId_from_animal(animal_name))
            }
    return templates.TemplateResponse('animal.html', context={'request': request, 'result': result})

@app.get('/animal')
async def form_post(request: Request):
    result = "Which animal would you like to see?"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

@app.post('/animal')
async def form_post(request: Request, animal: str = Form(...)):
    result = getAscii(animal)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

@app.get('/user/{username}')
async def get_animal(request: Request, username: str):
    result = {'username': username, 'animals': getAnimals(username)}
    return templates.TemplateResponse('user.html', context={'request': request, 'result': result})
