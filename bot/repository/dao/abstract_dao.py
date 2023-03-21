import asyncpg


class AbstractDAO:

    def __init__(self, pool: asyncpg.Pool):
        self._pool = pool
