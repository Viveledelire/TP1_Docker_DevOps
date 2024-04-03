from flask import Flask
from prometheus_flask_exporter import PrometheusFlaskExporter
from prometheus_client import Counter

app = Flask(__name__)
exporter = PrometheusFlaskExporter(app)

@app.route("/metrics")
def metrics():
    return exporter.render()

# Metric n°1 Nombre de visites
nb_visites = Counter("nb_visites", "Nombre de visites sur la page")

@app.route('/')
def index():
    nb_visites.inc()
    return 'HelloWorld!'

app.run(host='0.0.0.0', port=8080)
