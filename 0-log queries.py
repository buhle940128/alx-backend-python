import functools
import logging
import sqlite3

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get("query") or (args[1] if len(args) > 1 else None)
        if query:
            logger.info(f"Executing SQL Query: {query}")
        else:
            logger.warning("No SQL query found in arguments to log.")
        return func(*args, **kwargs)
    return wrapper

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)

    @log_queries
    def execute(self, query, params=None):
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.connection.commit()
        return cursor.fetchall()

