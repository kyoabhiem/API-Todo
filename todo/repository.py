import datetime
from typing import List
from todo.model import TodoModel


class TodoRepository:
    todo = []

    def fetch_todo(self) -> List[TodoModel]:
        data = list(filter(lambda item: item.deleted_at is None, self.todo))

        return data

    def create_todo(self, data: TodoModel) -> TodoModel:
        index = len(self.todo)
        data.id = index + 1
        self.todo.append(data)

        return data

    def show_todo(self, todo_id) -> (TodoModel, None):
        data = list(filter(lambda item: item.id is int(todo_id) and item.deleted_at is None, self.todo))

        if len(data) == 0:
            return None

        return data[0]

    def update_todo(self, todo_id, data: TodoModel) -> (TodoModel, None):
        todoData = self.show_todo(todo_id)
        if todoData is None:
            return None

        todoData.title = data.title
        todoData.description = data.description
        todoData.updated_at = data.updated_at

        return todoData

    def delete_todo(self, todo_id: int) -> (TodoModel, None):
        todoData = self.show_todo(todo_id)
        if todoData is None:
            return None

        todoData.deleted_at = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        return todoData

    def finish_todo(self, todo_id: int) -> (TodoModel, None):
        todoData = self.show_todo(todo_id)
        if todoData is None:
            return None

        todoData.finished_at = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        return todoData
