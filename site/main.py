import os

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from database import getAscii

app = FastAPI()
templates = Jinja2Templates(directory="../templates/")

@app.get('/')
async def root(request: Request):
    # result = getAscii(animal_name='cat')
    # return {"cat": result}
    return templates.TemplateResponse('landing.html', context={'request': request, 'result': None})

if __name__ == '__main__':
    uvicorn.run(host='0.0.0.0', debug=True, port=int(os.environ.get('PORT', 8080)))
