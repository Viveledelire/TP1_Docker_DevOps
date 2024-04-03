from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    nb_visites.inc()
    return 'HelloWorld!'

app.run(host='0.0.0.0', port=8080)
