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
