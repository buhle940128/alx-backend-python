import sqlite3
from functools import wraps

def with_transaction(db_path='example.db'):
    """
    Decorator that manages a database transaction.
    - Opens a connection.
    - Commits if the function succeeds.
    - Rolls back if an exception occurs.
    - Closes the connection afterward.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            conn = sqlite3.connect(db_path)
            try:
                result = func(conn, *args, **kwargs)
                conn.commit()
                return result
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                conn.close()
        return wrapper
    return decorator
