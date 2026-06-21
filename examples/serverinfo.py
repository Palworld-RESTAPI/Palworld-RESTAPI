import asyncio
from palworld_restapi import AsyncPalworldClient, PalworldApiError


async def main():
    server_url = "http://127.0.0.1:8212"
    password = "admin_password"

    try:
        async with AsyncPalworldClient(server_url, password=password) as client:
            info = await client.get_info()
            print(f"Server Name: {info.servername}")
            print(f"Version: {info.version}")
            print(f"Description: {info.description}")

            metrics = await client.get_metrics()
            print(f"Current Players: {metrics.currentplayernum}/{metrics.maxplayernum}")
            print(f"Server FPS: {metrics.serverfps}")
    except PalworldApiError as e:
        print(f"API Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
