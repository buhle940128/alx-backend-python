@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()
 First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
