from flask import Flask
from healthcheck import HealthCheck
from prometheus_client import generate_latest

from utils.logging import get_logger, APP_RUNNING
from utils.config import DEBUG, POD_NAME


def create_app():
    app = Flask(__name__)
    health = HealthCheck()
    app.add_url_rule("/healthz", "healthcheck", view_func=lambda: health.run())
    app.add_url_rule('/metrics', "metrics", view_func=generate_latest)
    APP_RUNNING.labels(POD_NAME).set(1)
    return app


logger = get_logger(__name__)
app = create_app()


if __name__ == "__main__":  # pragma: no cover
    app.run(debug=DEBUG, host='0.0.0.0', port=8080)
