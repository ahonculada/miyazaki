import pymongo

with open('../secrets.txt') as data:
    password = ''.join(data.readlines())[:-1]

client = pymongo.MongoClient(f"mongodb+srv://miyazaki:{ password }@miyazaki-cluster-1.ri5i4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydb = client['Miyazaki-db']
for collection in mydb.list_collection_names():
    print(collection)
