from motor.motor_asyncio import AsyncIOMotorClient
from sanic import app


class MotorConnection(object):
    """
    Provides a MongoDB connection and sets the DB to be used.
    The class implements the Singleton pattern.
    """
    __instance = None

    def __new__(cls):
        if MotorConnection.__instance is None:
            MotorConnection.__instance = object.__new__(cls)

            MotorConnection.__instance.client = AsyncIOMotorClient(
                    'db',
                    27017,
                    io_loop=app.get_event_loop()
                )
            MotorConnection.__instance.db = MotorConnection.__instance.client.test_database

        return MotorConnection.__instance.db
