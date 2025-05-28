import functools

def log_queries():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG] Executing function: {func.__name__}")
            # Assuming the SQL query is passed as the first argument
            if args:
                query = args[0]
                print(f"[LOG] SQL Query: {query}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator



