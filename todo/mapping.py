import datetime
from todo.model import TodoModel


class TodoMapping:
    @staticmethod
    def map_create_request(data) -> TodoModel:
        dtmNow = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        todoModel = TodoModel(
            title=data['title'],
            description=data['description'],
            finished_at=None,
            created_at=dtmNow,
            updated_at=dtmNow,
            deleted_at=None
        )

        return todoModel

    @staticmethod
    def map_update_request(data) -> TodoModel:
        dtmNow = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        todoModel = TodoModel(
            title=data['title'],
            description=data['description'],
            updated_at=dtmNow,
        )

        return todoModel

    @staticmethod
    def model_to_json(data: TodoModel):
        return {
            "id": data.id,
            "title": data.title,
            "description": data.description,
            "created_at": data.created_at,
            "updated_at": data.updated_at,
            "finished_at": data.finished_at,
            "deleted_at": data.deleted_at,
        }

    @staticmethod
    def list(datas):
        data = []
        for item in datas:
            data.insert(len(data), TodoMapping.model_to_json(item))

        return data
