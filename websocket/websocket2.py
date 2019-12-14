import asyncio
import json
import logging
import websockets


logging.basicConfig()

STATE = {"value": 0}

USERS2 = []
USERS = set()

async def register(websockets):
    USERS2.append({"socket": websockets, "username": "John Doe"})

async def counter(websockets, path):
    print(type(websockets))
    await register(websockets)
    try:
        async for message in websockets:
            json1_data = json.loads(message)

            print("{}", message)
            if json1_data["password"] == "12345":
                await asyncio.wait([user["socket"].send(message)for user in USERS2])
            for mod in USERS2:
                if mod["password"] == "54321":
                    await asyncio.wait(mod.send(message))

            if json1_data["type"] == "question":
                await asyncio.wait([user["socket"].send(message) for user in USERS2])


    finally:
        await unregister(websockets)


start_server = websockets.serve(counter, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()