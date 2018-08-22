from flask import Flask, jsonify, render_template
from flask_cors import CORS 
app = Flask(__name__)
@app.route('/cargarImagen')
def cargarImagen():
    return render_template('cargarImagen.html')
    
@app.route('/AR', methods=['POST'])
def AR():
    return jsonify({"mensaje":"hola mundo"})

if __name__ == "__main__":
    app.run(port=8080,debug=True)