from flask import Blueprint, jsonify


main = Blueprint("main", __name__)


@main.route("/")
def home():
    return "<h1>DevOps Task Manager - Branch DEV</h1>"


@main.route("/api/tasks")
def tasks():
    return jsonify([
        {
            "id": 1,
            "title": "Configurar Git",
            "status": "concluída"
        },
        {
            "id": 2,
            "title": "Criar container Docker",
            "status": "pendente"
        },
        {
            "id": 3,
            "title": "Configurar integração contínua",
            "status": "pendente"
        }
    ])