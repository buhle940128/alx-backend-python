# alx-backend-pythondef log_queries(func):
    def wrapper(*args, **kwargs):
        query = args[1] if len(args) > 1 else kwargs.get('query')
        print(f"[LOG] Executing query: {query}")
        return func(*args, **kwargs)
    return wrapper

class Database:
    def __init__(self, name):
        self.name = name 

    @log_queries
    def execute_query(self, query):
        # Simulate query execution
        print(f"Query '{query}' executed on database '{self.name}'.")

def log_queries():
    def decorator(func):
        def wrapper(*args, **kwargs):
            query = args[1] if len(args) > 1 else kwargs.get('query')
            print(f"[LOG] Executing query: {query}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

class Database:
    def __init__(self, name):
        self.name = name

    @log_queries()
    def execute_query(self, query):
        # Simulate query execution
        print(f"Query '{query}' executed on database '{self.name}'.")

