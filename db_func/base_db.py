import asyncpg
import os

from dotenv import load_dotenv


class BaseDb:
    _instance = None

    def __init__(self):
        self.pool = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(BaseDb, cls).__new__(cls)
        return cls._instance

    async def init_pool(self):
        load_dotenv()

        database = str(os.getenv("DB_NAME"))
        user = str(os.getenv("DB_USER"))
        password = str(os.getenv("DB_PASSWORD"))
        host = str(os.getenv("DB_HOST"))
        port = str(os.getenv("DB_PORT"))

        self.pool = await asyncpg.create_pool(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )

    async def fetch(self, query, *args, **kwargs):
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, *args, **kwargs)

    async def execute(self, query, *args, **kwargs):
        async with self.pool.acquire() as connection:
            return await connection.execute(query, *args, **kwargs)
