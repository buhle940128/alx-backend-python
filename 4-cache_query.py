query_cache = {}

def cache_query(func):
    """
    Decorator to cache the result of SQL queries based on the query string.
    """
    def wrapper(query, *args, **kwargs):
        if query in query_cache:
            print("Cache hit for query:", query)
            return query_cache[query]
        else:
            print("Cache miss for query:", query)
            result = func(query, *args, **kwargs)
            query_cache[query] = result
            return result
    return wrapper
