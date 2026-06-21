import asyncio
from palworld_restapi import AsyncPalworldClient, PalworldApiError


async def main():
    server_url = "http://127.0.0.1:8212"
    password = "admin_password"

    try:
        async with AsyncPalworldClient(server_url, password=password) as client:
            response = await client.get_players()
            print(f"Online Players: {len(response.players)}")
            for player in response.players:
                print(f"- {player.name} (Level: {player.level}, Ping: {player.ping}ms)")
    except PalworldApiError as e:
        print(f"API Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
