import sqlalchemy
import logging

logger = logging.getLogger(__name__)


class DatabaseClient:
    def __init__(self, db_type, database, username, password, host, port=None):
        if db_type.lower() == 'mssql':
            driver = 'mssql+pymssql'
        elif db_type.lower() == 'mariadb':
            driver = 'mariadb+mariadbconnector'
        elif db_type.lower() == 'postgresql':
            driver = 'postgresql+psycopg2'
        else:
            raise ValueError(f"Invalid database type {type}")

        if port:
            host = host + ':' + port

        self.engine = sqlalchemy.create_engine(f'{driver}://{username}:{password}@{host}/{database}')

    def get_connection(self):
        return self.engine.connect()

    def execute_sql(self, sql):
        with self.engine.connect() as conn:
            return conn.execute(sqlalchemy.text(sql))
