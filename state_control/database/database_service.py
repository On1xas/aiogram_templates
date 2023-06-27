import asyncpg



class RequestDB:
    def __init__(self, connection: asyncpg.pool.Pool):
        self.connection = connection

    async def add_user(self, user_id, user_name):
        query = f"""INSERT INTO
        users (user_id, user_name)
        VALUES ({user_id}, '{user_name}') ON CONFLICT (user_id) DO UPDATE SET user_name = '{user_name}';
        """
        await self.connection.execute(query=query)
