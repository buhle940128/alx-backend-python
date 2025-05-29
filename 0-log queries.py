import sqlite3
import functools

# Decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Try to get the SQL query from either positional or keyword arguments
        if args:
            print(f"[LOG] SQL Query: {args[0]}")
        elif 'query' in kwargs:
            print(f"[LOG] SQL Query: {kwargs['query']}")
        else:
            print("[LOG] No SQL query found in arguments.")
        
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")



