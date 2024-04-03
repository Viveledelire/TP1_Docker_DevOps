from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def index():
    return 'HelloWorld!'

@app.route("/metrics")
def metrics():
    return metrics.render()

app.run(host='0.0.0.0', port=8080)
