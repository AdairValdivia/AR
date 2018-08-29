from flask import Flask, jsonify, render_template, request
from flask_cors import CORS 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np 
import cv2
import time
app = Flask(__name__)
@app.route('/cargarImagen')
def cargarImagen():
    return render_template('cargarImagen.html')
    
@app.route('/AR', methods=['POST'])
def AR():
    a=request.files['image']
    nparr = np.fromstring(a, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #print(type(a))
    #img=mpimg.imread(a)
    #imgplot = plt.imshow(img)
    #plt.show()
    #time.sleep(5)
    return jsonify({"mensaje":"hola mundo"})

if __name__ == "__main__":
    app.run(port=8080,debug=True)