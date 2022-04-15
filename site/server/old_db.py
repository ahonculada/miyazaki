# import motor.motor_asyncio
# from bson.objectid import ObjectId

# MONGO_DETAILS = "mongodb://localhost:8000"

# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database = client.animals

# animal_collection = database.get_collection("animal_collection")

# def animal_helper(animal) -> dict:
#     return {
#         "id": str(animal["id"]),
#         "name": animal["name"],
#         "ascii": animal["ascii"],
#         "artist": animal["artist"],
#     }


# # Retrieve all animals present in the database
# async def retrieve_animals():
#     animals = []
#     async for animal in animal_collection.find():
#         animals.append(animal_helper(animal))
#     return animals

# # Add an animal into the database
# async def add_animal(animal_data: dict) -> dict:
#     animal = await animal_collection.insert_one(animal_data)
#     new_animal = await animal_collection.find_one({"name": animal.inserted_name})
#     return animal_helper(new_animal)

# # Get an animal with a matching name
# async def get_animal(name: str) -> dict:
#     animal = await animal_collection.find_one({"name": ObjectId(name)})
#     if animal:
#         return animal_helper(animal)
