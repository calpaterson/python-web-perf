import random
import asyncpg

pool = None

async def get_pool():
    global pool
    if pool is None:
        pool = await asyncpg.create_pool("postgres://test:test@localhost:6432/test")
    return pool

max_n = 1000_000 - 1

async def get_row():
    pool = await get_pool()
    async with pool.acquire() as conn:
        index = random.randint(1, max_n)
        ((a, b),) = await conn.fetch(f"select a, b from test where a = {index}")
    return a, b
