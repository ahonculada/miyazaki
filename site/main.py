import os
from enum import Enum

import uvicorn
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.templating import Jinja2Templates

from database import getAnimals, getAscii

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
    #if animal_name == 'fish':
    #    with open('../ascii/fish.txt') as data:
    #        image = ''
    #        for line in data:
    #            image += line
    #elif animal_name == 'cat':
    #    with open('../ascii/cat.txt') as data:
    #        image = ''
    #        for line in data:
    #            image += line
    #elif animal_name == 'dog':
    #    with open('../ascii/dog.txt') as data:
    #        image = ''
    #        for line in data:
    #            image += line
    #elif animal_name == 'rabbit':
    #    with open('../ascii/rabbit.txt') as data:
    #        image = ''
    #        for line in data:
    #            image += line
    #elif animal_name == 'cow':
    #    with open('../ascii/cow.txt') as data:
    #        image = ''
    #        for line in data:
    #            image += line
    result = getAscii(animal_name)
    return templates.TemplateResponse('animal.html', context={'request': request, 'result': result})

@app.get('/animal')
async def form_post(request: Request):
    result = "Which animal would you like to see?"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

@app.post('/animal')
async def form_post(request: Request, animal: str = Form(...)):
    #if animal == 'fish':
    #    with open('../ascii/fish.txt') as data:
    #        image = ''
    #        for line in data:
    #            image += line
    #elif animal == 'cat':
    #    with open('../ascii/cat.txt') as data:
    #        image = ''
    #        for line in data:
    #            image += line
    #elif animal == 'dog':
    #    with open('../ascii/dog.txt') as data:
    #        image = ''
    #        for line in data:
    #            image += line
    #elif animal == 'rabbit':
    #    with open('../ascii/rabbit.txt') as data:
    #        image = ''
    #        for line in data:
    #            image += line
    #elif animal == 'cow':
    #    with open('../ascii/cow.txt') as data:
    #        image = ''
    #        for line in data:
    #            image += line
    result = getAscii(animal)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

@app.get('/user/{username}')
async def get_animal(request: Request, username: str):
    result = {'username': username, 'animals': getAnimals(username)}
    return templates.TemplateResponse('user.html', context={'request': request, 'result': result})


if __name__ == '__main__':
    uvicorn.run(host='0.0.0.0', debug=True, port=int(os.environ.get('PORT', 8080)))
