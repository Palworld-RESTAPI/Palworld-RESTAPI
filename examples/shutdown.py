import asyncio
from palworld_restapi import AsyncPalworldClient, PalworldApiError


async def main():
    server_url = "http://127.0.0.1:8212"
    password = "admin_password"

    try:
        async with AsyncPalworldClient(server_url, password=password) as client:
            # Broadcast a warning message and shutdown after 60 seconds
            await client.shutdown(
                waittime=60,
                message="Server shutting down in 60 seconds for maintenance!",
            )
            print("Shutdown initiated successfully.")
    except PalworldApiError as e:
        print(f"API Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
