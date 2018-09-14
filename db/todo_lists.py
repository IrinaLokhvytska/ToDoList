from db.db import MotorConnection

db = MotorConnection()
lists = db.todo_project.todo_lists


class ToDoLists:
    async def insert_todo(self, document):
        result = await lists.insert_one(document)
        return result.inserted_id

    async def find_list_by_id(self,list_id):
        document = await lists.find_one({'_id': list_id})
        return document

    async def find_all_lists(self):
        todo_lists = []
        async for doc in lists.find():
            todo_lists.append(doc)
        return todo_lists
