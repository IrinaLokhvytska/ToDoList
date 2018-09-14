class ToDoList:
    def __init__(self, db):
        self.db = db
        self.lists = db.todo_project.todo_lists

    async def insert_todo(self, document):
        result = await self.lists.insert_one(document)
        return result.inserted_id

    async def find_list_by_id(self, list_id):
        document = await self.lists.find_one({'_id': list_id})
        return document

    async def find_all_lists(self):
        todo_lists = []
        async for doc in self.lists.find():
            todo_lists.append(doc)
        return todo_lists
