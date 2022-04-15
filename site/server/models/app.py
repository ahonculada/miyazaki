from fastapi import FastAPI
import pymongo

app = FastAPI()

@app.get('/')
async def root():
    return { "message": "Hello, Girl!"}

client = pymongo.MongoClient("mongodb+srv://miyazaki:<password>@miyazaki-cluster-1.ri5i4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test