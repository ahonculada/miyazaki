from enum import Enum
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="../templates/")

class AnimalName(str, Enum):
    fish = 'fish'
    cat = 'cat'

@app.get('/')
async def root():
    return { "message": "Hello, Girl!"}

@app.get('/animal/{animal_name}')
async def get_animal(request: Request, animal_name: AnimalName):
    if animal_name == AnimalName.fish:
        with open('../ascii/fish.txt') as data:
            image = ''
            for line in data:
                image += line

    elif animal_name == AnimalName.cat:
        with open('../ascii/cat.txt') as data:
            image = ''
            for line in data:
                image += line
    #return {'animal_name': animal_name,
    #        'message': image
    #        }
    result = image
    return templates.TemplateResponse('animal.html', context={'request': request, 'result': result})

@app.get('/animal')
async def form_post(request: Request):
    result = "Which animal would you like to see?"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

@app.post('/animal')
async def form_post(request: Request, animal: str = Form(...)):
    if animal == AnimalName.fish:
        with open('../ascii/fish.txt') as data:
            image = ''
            for line in data:
                image += line

    elif animal == AnimalName.cat:
        with open('../ascii/cat.txt') as data:
            image = ''
            for line in data:
                image += line
    result = image
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

