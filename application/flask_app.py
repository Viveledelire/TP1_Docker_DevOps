from flask import Flask
from prometheus_client import Counter

# metric n°1 Nombre de visites
nb_visites = Counter("nb_visites", "Nombre de visites sur la page d'accueil")

app = Flask(__name__)

@app.route('/')
def index():
    nb_visites.inc()
    return 'HelloWorld!'

@app.route("/metrics")
def metrics():
    return prometheus_client.generate_metrics()

app.run(host='0.0.0.0', port=8080)
