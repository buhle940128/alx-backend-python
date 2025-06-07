async def async_fetch_older_users(db_path):
    async with aiosqlite.connect(db_path) as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        older_users = await cursor.fetchall()
        await cursor.close()
        return older_users

# Function to run both queries concurrently
async def fetch_concurrently():
    db_path = "example.db"
    
    # Ensure both tasks run concurrently
    users, older_users = await asyncio.gather(
        async_fetch_users(db_path),
        async_fetch_older_users(db_path)
    )
    
    print("All Users:")
    for user in users:
        print(user)

    print("\nUsers older than 40:")
    for user in older_users:
        print(user)

# Run the concurrent fetch
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
