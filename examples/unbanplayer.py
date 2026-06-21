import asyncio
from palworld_restapi import AsyncPalworldClient, PalworldApiError


async def main():
    server_url = "http://127.0.0.1:8212"
    password = "admin_password"

    try:
        async with AsyncPalworldClient(server_url, password=password) as client:
            await client.unban_player("steam_00000000000000000")
            print("Player unbanned successfully.")
    except PalworldApiError as e:
        print(f"API Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
