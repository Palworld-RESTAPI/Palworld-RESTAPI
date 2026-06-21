import asyncio
from palworld_restapi import AsyncPalworldClient, PalworldApiError


async def main():
    server_url = "http://127.0.0.1:8212"
    password = "admin_password"

    try:
        async with AsyncPalworldClient(server_url, password=password) as client:
            await client.announce(
                "Server restarting in 5 minutes! Please find a safe place."
            )
            print("Announcement sent successfully.")
    except PalworldApiError as e:
        print(f"API Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
