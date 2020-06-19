import random
import aiopg

pool = None

async def get_pool():
    global pool
    if pool is None:
        pool = await aiopg.create_pool(
            "dbname=test user=test password=test port=6432 host=127.0.0.1")
    return pool

max_n = 1000_000 - 1

async def get_row():
    pool = await get_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            index = random.randint(1, max_n)
            await cursor.execute("select a, b from test where a = %s", (index,))
            ((a, b),) = await cursor.fetchall()
    return a, b
