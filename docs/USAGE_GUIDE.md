# Palworld REST API Usage Guide

This guide covers how to use the Palworld REST API Python client in both Synchronous and Asynchronous applications, and how to use the CLI.

## Installation

Ensure your project environment is setup and install the library (e.g. `uv add palworld-restapi` or `pip install palworld-restapi`).

## Code Examples
We have a full suite of working scripts in the `examples/` directory of the repository:
- `announcement.py`
- `banplayer.py` / `kickplayer.py` / `unbanplayer.py`
- `playerlist.py`
- `serverinfo.py` / `sync_serverinfo.py`
- `shutdown.py`

## Sync Client Usage

Use `PalworldClient` for standard scripts and synchronous applications.

```python
from palworld_restapi import PalworldClient, PalworldApiError

def main():
    try:
        with PalworldClient("http://127.0.0.1:8212", password="admin-pass") as client:
            info = client.get_info()
            print(f"Server Name: {info.servername}")
            print(f"Version: {info.version}")
            
            players_resp = client.get_players()
            print(f"Online Players: {len(players_resp.players)}")
            
            client.announce("Hello from Palworld-RESTAPI!")
    except PalworldApiError as e:
        print(f"API Error: {e}")

if __name__ == "__main__":
    main()
```

## Async Client Usage

Use `AsyncPalworldClient` for highly concurrent applications, like Discord bots (e.g., discord.py).

```python
import asyncio
from palworld_restapi import AsyncPalworldClient, PalworldApiError

async def main():
    try:
        async with AsyncPalworldClient("http://127.0.0.1:8212", password="admin-pass") as client:
            metrics = await client.get_metrics()
            print(f"Server FPS: {metrics.serverfps}")
            
            settings = await client.get_settings()
            print(f"Difficulty: {settings.Difficulty}")
    except PalworldApiError as e:
        print(f"API Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

## CLI Usage

The package provides a built-in CLI `palworld-cli`. 

For full details on authentication, options, and commands, please see the dedicated **[CLI Guide](CLI_GUIDE.md)**!
