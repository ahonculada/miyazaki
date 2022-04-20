from unicodedata import name

import pymongo
from bson.objectid import ObjectId

with open('../secrets.txt') as data:
    password = ''.join(data.readlines())[:-1]

client = pymongo.MongoClient(f"mongodb+srv://miyazaki:{ password }@miyazaki-cluster-1.qhpgx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

def animal_helper(animal) -> dict:
    return {
        # "id": str(animal["id"]),
        "name": animal["name"],
        "ascii": animal["ascii"],
        "artist": animal["artist"],
    }

def getAscii(animal_name: str) -> str:
    mydb = client['Miyazaki-db']
    animals = mydb['animals']
    animal = animals.find_one({'name': f'{animal_name}'})
    return animal['ascii']

def getUserId_from_animal(animal_name: str) -> str:
    mydb = client['Miyazaki-db']
    animals = mydb['animals']
    animal = animals.find_one({'name': f'{animal_name}'})
    return animal['userid']

def getUsername_from_userId(user_id: str) -> str:
    mydb = client['Miyazaki-db']
    users = mydb['users']
    user = users.find_one({'_id': ObjectId(f'{user_id}')})
    return user['name']

def getAnimals(username: str) -> str:
    mydb = client['Miyazaki-db']
    users = mydb['users']
    user = users.find_one({'name': f'{username}'})
    return user['animals']

def addAnimal(animal: str, ascii: str, artist: str) -> bool:
    # TODO:
    # check if user exists in database
    # if user exists add animal under that user 
    # if doesnt, cresate user and upload under that user
    # check if ascii already exists under that username

    #CUR:
    # check if ascii currently exists, if so overwrite it,
    # else create new one
    mydb = client['Miyazaki-db']
    animals = mydb['animals']
    users = mydb['users']
    animalQuery = {"name": animal}
    updatedValues = {"$set": {"ascii": ascii, "artist": artist}}

    # check if user exists, and animal is under them?
    # if user doesnt exit add them to database
    if not users.find_one({"name": artist}):
        users.insert_one({"name": artist, "animals": []})

    # check if animal exists
    # animal = animals.find_one({"name": animal})
    if animals.find_one(animalQuery):
        update_animal = animals.update_one(animalQuery, updatedValues)
    else:
        new_animal = animals.insert_one({"name": animal,
        "ascii": ascii,
        "artist": artist,})


    # new_animal = animals.find_one({"name": animal})
    # print(new_animal)
    # return animal_helper(new_animal)
    return True

def addUser(artist: str) -> bool:
    mydb = client['Miyazaki-db']
    users = mydb['users']
    if users.find_one({"name": artist}):
        return False
    users.insert_one({"name": artist, "animals": []})
    return True

# # Get an animal with a matching name
def get_animal(name: str) -> dict:
    mydb = client['Miyazaki-db']
    animal = mydb.find_one({"name": ObjectId(name)})
    if animal:
        return animal_helper(animal)

def addUser(artist: str) -> bool:
    # check if user exists before adding
    mydb = client['Miyazaki-db']
    users = mydb['users']
    users.insert_one({"name": artist, "animals": []})
    return True

def getAllAnimals(animal_name: str) -> pymongo.cursor.Cursor:
    mydb = client['Miyazaki-db']
    animals = mydb['animals']
    results = animals.find({'name': 'cat'})
    return results

if __name__ == '__main__':
    getAnimals('vangogh')

