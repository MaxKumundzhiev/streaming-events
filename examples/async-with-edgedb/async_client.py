from typing import Optional

import edgedb


class Connection:
    dsn: str
    conn: Optional[edgedb.AsyncIOClient] = None

    async def __aenter__(self) -> edgedb.AsyncIOClient:
        self.conn = await edgedb.create_async_client(self.dsn)
        return self.conn
    
    async def __aexit__(self, type, value, traceback) -> bool:
        if self.conn:
            await self.conn.aclose()
        return False


async def get_users() -> edgedb.Set:
    async with Connection("...") as conn:
        result = await conn.query("...")
    return result