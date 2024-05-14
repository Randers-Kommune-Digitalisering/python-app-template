from flask import Flask
from healthcheck import HealthCheck
from prometheus_client import generate_latest
# from apscheduler.schedulers.background import BackgroundScheduler

from utils.logging import get_logger, APP_RUNNING
from utils.config import DEBUG, POD_NAME


def create_app():
    app = Flask(__name__)
    health = HealthCheck()
    app.add_url_rule("/healthz", "healthcheck", view_func=lambda: health.run())
    app.add_url_rule('/metrics', "metrics", view_func=generate_latest)
    APP_RUNNING.labels(POD_NAME).set(1)
    return app

# def create_scheduler():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(test_job, 'interval', seconds=30) # Every 30 seconds
#     scheduler.add_job(test_job, 'cron', day_of_week='mon', hour=7) # Every Monday at 7 AM
#     return scheduler


# def test_job():
#     logger.info('Hello from test job')


logger = get_logger(__name__)
# scheduler = create_scheduler()
app = create_app()


# @app.route('/test-database', methods=['GET'])
# def test_database():
#     from database import test_database
#     ok = test_database()
#     if ok:
#         return ok
#     return 'failed', 500


if __name__ == "__main__":  # pragma: no cover
    # scheduler.start()
    app.run(debug=DEBUG, host='0.0.0.0', port=8080)