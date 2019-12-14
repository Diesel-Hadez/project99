import asyncio
import json
import logging
import websockets


logging.basicConfig()

STATE = {"value": 0}

USERS2 = []
USERS = set()

async def register(websockets):
    USERS2.append({"socket": websockets, "mod": "false"})


async def unregister(websockets):
    temp = [user for user in USERS2 if user ["socket"] != websockets]
    USERS2 = temp
    await notify_users()

async def counter(websockets, path):
    print(type(websockets))
    await register(websockets)
    try:
        async for message in websockets:
            json1_data = json.loads(message)
            sender_user = None
            for user in USERS2:
                if user["socket"] == websockets:
                   sender_user = user
            if sender_user is None:
                continue;
            print( message)
            if json1_data["password"] == "12345":
                sender_user["mod"] = "teacher"
                await asyncio.wait([user["socket"].send(message)for user in USERS2])
            if json1_data["password"] == "54321":
                print("Right password")
                sender_user["mod"] = "true"
                #for user in USERS2:
                #    if user["socket"] == websockets:
                #        user["mod"] = "true"

            if json1_data["type"] == "realquestion":
                    await asyncio.wait([user["socket"].send(message) for user in USERS2])
            if json1_data["type"] == "question":
                if sender_user["mod"] != "true":
                    await asyncio.wait([user["socket"].send(message) for user in USERS2 if user["mod"] == "true"])
            if json1_data["type"] == "drawbox":
                if sender_user["mod"] == "teacher":
                    await asyncio.wait([user["socket"].send(message) for user in USERS2 if user["mod"] != "teacher"])



    finally:
        await unregister(websockets)


start_server = websockets.serve(counter, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
