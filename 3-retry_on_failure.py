import sqlite3
import time
import random
from functools import wraps

def retry_on_failure(retries=3, delay=2):
    """
    Decorator that retries a function if it raises an exception.
    Useful for handling transient database errors.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt < retries:
                        time.sleep(delay)
                    else:
                        print("All retry attempts failed.")
                        raise last_exception
        return wrapper
    return decorator
   @retry_on_failure(retries=3, delay=1)
def insert_user_unstable(conn, name):
    if random.random() < 0.5:  # Simulate a 50% chance of failure
        raise sqlite3.OperationalError("Simulated transient database error.")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    print(f"User '{name}' inserted successfully.")

# Setup database
def setup_database():
    conn = sqlite3.connect('example.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Usage
if __name__ == '__main__':
    setup_database()
    conn = sqlite3.connect('example.db')

    try:
        insert_user_unstable(conn, 'Alice')
    except Exception as e:
        print(f"Operation failed after retries: {e}")
    finally:
        conn.close()

    # Verify result
    conn = sqlite3.connect('example.db')
    users = conn.execute('SELECT * FROM users').fetchall()
    print("Users in database:", users)
    conn.close() 
