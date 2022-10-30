from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/api/v1/hello-world-2')
def hello_world():
    return 'Hello World 2'

if __name__ == 'main':
    serve(app,host = '0.0.0.0',post=50100)