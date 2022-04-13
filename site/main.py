from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class AnimalName(str, Enum):
    fish = 'fish'
    cat = 'cat'

@app.get('/')
async def root():
    return { "message": "Hello, Girl!"}

@app.get('/{animal_name}')
async def get_animal(animal_name: AnimalName):
    if animal_name == AnimalName.fish:
        with open('../ascii/fish.txt') as data:
            image = ''
            for line in data:
                image += line
            #print(image)

    elif animal_name == AnimalName.cat:
        with open('../ascii/cat.txt') as data:
            image = ''
            for line in data:
                image += line
    return {'animal_name': animal_name,
            'message': image 
            }
