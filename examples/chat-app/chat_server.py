from __future__ import annotations
from typing import *


import asyncio


async def process_request(
    reader: asyncio.StreamReader, writer: asyncio.StreamWriter
) -> None:
    addr = writer.get_extra_info("peername")
    while message := await reader.read(100):
        text = message.decode()
        print(f"server recieved {text} from {addr}")
        print(f"sending {text} back to {addr}")
        writer.write(message)
        await writer.drain()
        if text == "quit":
            break
    print("closing connection")
    writer.close()


async def main():
    server = await asyncio.start_server(host="127.0.0.1", port=8888, client_connected_cb=process_request)
    addr = server.sockets[0].getsockname() if server.sockets else "unknbown"
    print(f"serving on {addr}")
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())