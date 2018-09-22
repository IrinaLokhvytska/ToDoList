class ToDoList(object):
    """ Implements insert, find, delete methods of items in the todo_lists collection"""

    def __init__(self, db: object) -> None:
        """
        :param db: MotorConnection class
        """
        self.db = db
        self.project = 'todo_project'
        self.collection = 'todo_lists'
        self.list = self.db[self.project][self.collection]

    async def insert_todo(self, document: dict) -> object:
        """
        Asynchronous function for inserting todo_list's document

        :param document: a dict, where key - columns of the collection
        :return: id of the last inserted document
        """
        result = await self.list.insert_one(document)
        return result.inserted_id

    async def find_list_by_id(self, list_id):
        document = await self.list.find_one({'_id': list_id})
        return document

    async def find_all_lists(self) -> list:
        """
        Asynchronous function for selecting all documents from the collection

        :return: All lists from the todo_lists collection
        """
        todo_lists = []
        async for doc in self.list.find():
            todo_lists.append(doc)
        return todo_lists
