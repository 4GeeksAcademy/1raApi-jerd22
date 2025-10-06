# COMENTO CADA PARTE DE LOS EJERCICIOS
""" 
from flask import Flask

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta (página principal)
@app.route('/todos', methods=["GET"])
def hello_world():
    return "<h1>Hello!</h1>"

# Estas dos líneas siempre deben ir al final del archivo
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
"""


""""
from flask import Flask, jsonify

app = Flask(__name__)

# Variable global con la lista de todos
todos = [
    { "label": "My first task", "done": False }
]

# Endpoint /todos que devuelve la lista en formato JSON
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

# Estas dos líneas siempre al final
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
"""""


"""""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Variable global de todos
todos = [
    { "label": "My first task", "done": False }
]

# Endpoint GET /todos
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

# Endpoint POST /todos
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body:", request_body)
    return 'Response for the POST todo'

# Estas dos líneas siempre al final
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

"""""

"""""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Variable global de todos
todos = [
    { "label": "My first task", "done": False }
]

# Endpoint GET /todos
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

# Endpoint POST /todos
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

# Estas dos líneas siempre al final
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
"""
#EJERCIO 8

"""""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Variable global de todos
todos = [
    { "label": "My first task", "done": False }
]

# Endpoint GET /todos
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

# Endpoint POST /todos
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    return 'something'

# Estas dos líneas siempre al final
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

"""""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Variable global de todos
todos = [
    { "label": "My first task", "done": False }
]

# Endpoint GET /todos
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

# Endpoint POST /todos
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

# ELIMINAR TODOS O DELETE
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)

# Estas dos líneas siempre al final
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)











