from flask import Blueprint, jsonify

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return """
    <h1>DevOps Task Manager - Versao Final Integrada</h1>
    <p>Aplicacao criada para demonstrar praticas DevOps.</p>
    """


@main.route("/api/tasks")
def tasks():
    return jsonify([
        {"id": 1, "title": "Configurar Git", "status": "concluida"},
        {"id": 2, "title": "Criar container Docker", "status": "pendente"},
        {"id": 3, "title": "Configurar integracao continua", "status": "pendente"},
    ])