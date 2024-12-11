from flask import Flask, render_template, request, jsonify, redirect, url_for
import json

app = Flask(__name__)

# Simulación de base de datos
users = []  # Lista de usuarios
servers = []  # Lista de servidores

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verificar usuario en la base de datos simulada
        user = next((u for u in users if u['username'] == username and u['password'] == password), None)
        if user:
            return redirect(url_for('server_list'))
        return "Usuario o contraseña incorrectos", 401
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    # Agregar nuevo usuario
    users.append({'username': username, 'password': password})
    return jsonify({"message": "Usuario registrado"}), 201

@app.route('/create_server', methods=['POST'])
def create_server():
    server_id = len(servers) + 1
    server_name = f"Servidor {server_id}"
    
    # Crear servidor
    servers.append({"id": server_id, "name": server_name, "status": "running"})
    return jsonify({"server": server_name}), 201

@app.route('/servers', methods=['GET'])
def server_list():
    return render_template('servers.html', servers=servers)

if __name__ == '__main__':
    app.run(debug=True)
