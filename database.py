import motor.motor_asyncio
from bson import ObjectId

CONNECTION_STRING = "mongodb+srv://KHLaP_admin:gg1gqjsL6pYybE2T@khlap.fg2ez.mongodb.net/?retryWrites=true&w=majority&appName=khlap"
client = motor.motor_asyncio.AsyncIOMotorClient(CONNECTION_STRING)

database = client.KHLaP
freeboard_collection = database.get_collection("freeboard")
used_collection = database.get_collection("used")


def freeboard_helper(thread) -> dict:
    return {
        "id": str(thread["_id"]),
        "title": thread["title"],
        "username": thread["username"],
        "content": thread["content"],
        "image": thread["image"],
        "updated_at": thread["updated_at"],
    }


async def retrieve_freeboard(id: str) -> dict:
    freeboard = await freeboard_collection.find_one({"_id": ObjectId(id)})
    if freeboard:
        return freeboard_helper(freeboard)


async def retrieve_freeboards():
    freeboards = []
    async for freeboard in freeboard_collection.find():
        freeboards.append(freeboard_helper(freeboard))
    return freeboards


async def add_freeboard(freeboard_data: dict) -> dict:
    freeboard = await freeboard_collection.insert_one(freeboard_data)
    new_freeboard = await freeboard_collection.find_one({"_id": freeboard.inserted_id})
    return freeboard_helper(new_freeboard)


async def delete_freeboard(id: str):
    freeboard = await freeboard_collection.find_one({"_id": ObjectId(id)})
    if freeboard:
        await freeboard_collection.delete_one({"_id": freeboard.inserted_id})
        return True


async def update_freeboard(id: str, data: dict):
    if len(data) < 1:
        return False
    freeboard = await freeboard_collection.find_one({"_id": ObjectId(id)})
    if freeboard:
        updated_freeboard = await freeboard_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_freeboard:
            return True
        return False


def used_helper(thread) -> dict:
    return {
        "id": str(thread["_id"]),
    }
