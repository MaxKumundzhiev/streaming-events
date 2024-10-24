from __future__ import annotations
from typing import IO

import sys
import asyncio

async def send_file(file: IO[str]) -> None:
    reader, writer = await asyncio.open_connection(host="127.0.0.1", port=8888)

    for message in file:
        message_ = message.encode()
        writer.write(message_)
        await writer.drain()
        
        data = await reader.read(100)
        text = data.decode()
        print(f'received {text} back')
        if text == "quit":
            break
    print("closing connection")
    writer.close()

if __name__ == "__main__":
    asyncio.run(send_file(sys.stdin))