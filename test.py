from flask import Flask
import keras
app = Flask(__name__)
@app.route('/sample')

def running():
    print(keras.__version__)
    return 'Flask is running!'
