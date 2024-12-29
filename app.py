from flask import Flask, render_template
from keras._tf_keras.keras.models import load_model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if '__main__' == __name__:
    app.run(host='0.0.0.0', debug=True, port=8080)