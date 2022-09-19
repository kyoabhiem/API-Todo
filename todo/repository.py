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
        todo_data = self.show_todo(todo_id)
        if todo_data is None:
            return None

        todo_data.title = data.title
        todo_data.description = data.description
        todo_data.updated_at = data.updated_at

        return todo_data

    def delete_todo(self, todo_id: int) -> (TodoModel, None):
        todo_data = self.show_todo(todo_id)
        if todo_data is None:
            return None

        todo_data.deleted_at = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        return todo_data

    def finish_todo(self, todo_id: int) -> (TodoModel, None):
        todo_data = self.show_todo(todo_id)
        if todo_data is None:
            return None

        todo_data.finished_at = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        return todo_data
