class ToDoList(object):
    """ Implements insert, find, delete methods of items in the todo_lists collection"""

    def __init__(self, db: object) -> None:
        """
        :param db: MotorConnection class
        """
        self.db = db
        self.lists = db.todo_project.todo_lists

    async def insert_todo(self, document):
        result = await self.lists.insert_one(document)
        return result.inserted_id

    async def find_list_by_id(self, list_id):
        document = await self.lists.find_one({'_id': list_id})
        return document

    async def find_all_lists(self) -> list:
        """
        :return: All lists from the todo_lists collection
        """
        todo_lists = []
        async for doc in self.lists.find():
            todo_lists.append(doc)
        return todo_lists
