import os

import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

from database import getAnimals, getAscii

app = FastAPI()
templates = Jinja2Templates(directory="../templates/")

@app.get('/')
async def root(request: Request):
    # result = getAscii(animal_name='cat')
    # return {"cat": result}
    return templates.TemplateResponse('landing.html', context={'request': request, 'result': None})

@app.get('/animal/{animal_name}')
async def get_animal(request: Request, animal_name: str):
    result = getAscii(animal_name)
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



if __name__ == '__main__':
    uvicorn.run(host='0.0.0.0', debug=True, port=int(os.environ.get('PORT', 8080)))
