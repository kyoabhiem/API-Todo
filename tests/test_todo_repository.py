import datetime
import pytest
from todo.model import TodoModel
from todo.repository import TodoRepository


class TestRepository:
    @pytest.fixture
    def repository(self):
        return TodoRepository()

    def test_todo_list_positive(self, repository):
        for index in range(5):
            date_time_now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            todo_model = TodoModel(
                title="Task Title " + str(index),
                description="Description of Task " + str(index),
                created_at=date_time_now,
                updated_at=date_time_now,
            )
            repository.create_todo(todo_model)

        list_todo = repository.fetch_todo()

        assert len(list_todo) == 5, "the list is not 5 data"

    def test_todo_create(self, repository):
        date_time_now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        todo_model = TodoModel(
            title="Task Title create",
            description="Description of Task create",
            created_at=date_time_now,
            updated_at=date_time_now,
        )
        saved_data = repository.create_todo(todo_model)
        detail_todo = repository.show_todo(saved_data.id)

        assert detail_todo.title == todo_model.title
        assert detail_todo.description == todo_model.description

    def test_todo_update(self, repository):
        date_time_now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        todo_model = TodoModel(
            title="Task Title update",
            description="Description of Task update",
            created_at=date_time_now,
            updated_at=date_time_now,
        )
        saved_data = repository.create_todo(todo_model)

        todo_model_update = TodoModel(
            title="Task Title Updated",
            description="Description of Task Updated",
            updated_at=date_time_now,
        )
        update_data = repository.update_todo(saved_data.id, todo_model_update)

        assert saved_data.id == update_data.id
        assert update_data.title == todo_model_update.title
        assert update_data.description == todo_model_update.description

    def test_todo_finish(self, repository):
        date_time_now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        todo_model = TodoModel(
            title="Task Title finish",
            description="Description of Task finish",
            created_at=date_time_now,
            updated_at=date_time_now,
        )
        saved_data = repository.create_todo(todo_model)

        finish_data = repository.finish_todo(saved_data.id)

        assert saved_data.id == finish_data.id
        assert finish_data.finished_at is not None

    def test_todo_delete(self, repository):
        date_time_now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        todo_model = TodoModel(
            title="Task Title finish",
            description="Description of Task finish",
            created_at=date_time_now,
            updated_at=date_time_now,
        )
        saved_data = repository.create_todo(todo_model)

        delete_data = repository.delete_todo(saved_data.id)

        detail_data = repository.show_todo(saved_data.id)

        assert detail_data is None
        assert saved_data.id == delete_data.id
        assert delete_data.deleted_at is not None
