def with_db_connection():
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Simulate opening a DB connection
            connection = "DB_CONNECTION_OBJECT"
            print("[INFO] Opening database connection.")
            try:
                # Pass the connection as a keyword argument
                result = func(*args, connection=connection, **kwargs)
                return result
            finally:
                # Simulate closing the connection
                print("[INFO] Closing database connection.")
        return wrapper
    return decorator

class Database:
    def __init__(self, name):
        self.name = name

    @with_db_connection()
    def execute_query(self, query, connection=None):
        print(f"[DEBUG] Using connection: {connection}")
        print(f"[EXECUTE] Query '{query}' on database '{self.name}'.")



