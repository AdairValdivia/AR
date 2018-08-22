from flask import Flask, jsonify
from flask_cors import CORS 
app = Flask(__name__)
@app.route('/cargarImagen')
def cargarImagen():
    return "Cargar Imagen"
    
@app.route('/AR')
def AR():
    return jsonify({"mensaje":"hola mundo"})

if __name__ == "__main__":
    app.run(port=8080,debug=True)