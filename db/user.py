class User(object):
    """ Implements insert, find, delete methods of items in the user collection"""

    def __init__(self, db: object) -> None:
        """
        :param db: MotorConnection class
        """
        self.db = db
        self.project = 'todo_project'
        self.collection = 'users'
        self.users = self.db[self.project][self.collection]

    async def insert_user(self, document: dict) -> object:
        """
        Asynchronous function for inserting user's document

        :param document: a dict, where key - columns of the collection
        :return: id of the last inserted document
        """
        result = await self.users.insert_one(document)
        return result.inserted_id

    async def find_user_by_id(self, user_id):
        document = await self.users.find_one({'_id': user_id})
        return document

    async def find_all_users(self) -> list:
        """
        Asynchronous function for selecting all documents from the collection

        :return: User list from the users collection
        """
        user_list = []
        async for doc in self.users.find():
            user_list.append(doc)
        return user_list
