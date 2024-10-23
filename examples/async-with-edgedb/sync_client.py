import edgedb
from dataclasses import dataclass

from typing import Optional


@dataclass
class Connection:
    dsn: str
    conn: Optional[edgedb.Client] = None

    def __enter__(self) -> edgedb.Client:
        self.conn = edgedb.create_client(self.dsn)
        return self.conn

    def __exit__(self, type, value, traceback) -> bool:
        if self.conn:
            self.conn.close()
        return False