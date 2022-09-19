from todo.repository import TodoRepository
from flask import request, jsonify
from todo.mapping import TodoMapping
from flask import Blueprint

TodoRepository = TodoRepository()
blueprint = Blueprint(
    'todo_blueprint',
    __name__,
    url_prefix='/todo',
)


@blueprint.route('/', methods=["POST"])
def create():
    data = TodoMapping.map_create_request(request.json)
    response = TodoRepository.create_todo(data)

    return TodoMapping.model_to_json(response)


@blueprint.route('/', methods=['GET'])
def fetch():
    response = TodoRepository.fetch_todo()

    return TodoMapping.list(response)


@blueprint.route('/<todo_id>', methods=['GET'])
def detail(todo_id):
    data = TodoRepository.show_todo(todo_id)
    if data is None:
        return jsonify(None), 404

    return TodoMapping.model_to_json(data)


@blueprint.route('/<todo_id>', methods=['PUT', 'PATCH'])
def update(todo_id):
    update_data = TodoMapping.map_update_request(request.json)

    data = TodoRepository.update_todo(todo_id, update_data)
    if data is None:
        return jsonify(None), 404

    return TodoMapping.model_to_json(data)


@blueprint.route('/<todo_id>', methods=['DELETE'])
def delete(todo_id):
    data = TodoRepository.delete_todo(todo_id)
    if data is None:
        return jsonify(None), 404

    return TodoMapping.model_to_json(data)


@blueprint.route('/<todo_id>/finish', methods=['GET', 'POST', 'PUT', 'PATCH'])
def finish(todo_id):
    data = TodoRepository.finish_todo(todo_id)
    if data is None:
        return jsonify(None), 404

    return TodoMapping.model_to_json(data)
