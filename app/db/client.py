import os

import motor.motor_asyncio

DATABASE_URL = os.environ["MONGODB_URL"]

client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
db = client["database_name"]
