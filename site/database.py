import pymongo

with open('../secrets.txt') as data:
    password = ''.join(data.readlines())[:-1]

client = pymongo.MongoClient(f"mongodb+srv://miyazaki:{ password }@miyazaki-cluster-1.qhpgx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

def getAscii(animal_name: str) -> str:
    mydb = client['Miyazaki-db']
    animals = mydb['animals']
    animal = animals.find_one({'name': f'{animal_name}'})
    return animal['ascii']

def getAnimals(username: str) -> str:
    mydb = client['Miyazaki-db']
    users = mydb['users']
    user = users.find_one({'name': f'{username}'})
    return user['animals']

# def addAnimal()

if __name__ == '__main__':
    getAnimals('vangogh')