import asyncpg


class RequestDB:
    def __init__(self, connection: asyncpg.pool.Pool):
        self.connection = connection

    async def add_user(self, user_id, user_name):
        query = f"""INSERT INTO
        users (id, name)
        VALUES ({user_id}, '{user_name}' ON CONFLICT (id) DO UPDATE SET name = '{user_name}');
        """
        await self.connection.execute(query=query)
