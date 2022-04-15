import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return { "message": "Hello, Girl!"}

if __name__ == '__main__':
    uvicorn.run(host='0.0.0.0', debug=True, port=int(os.environ.get('PORT', 8080)))
