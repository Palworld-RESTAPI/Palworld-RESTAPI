# Palworld REST API

[![PyPI version](https://badge.fury.io/py/palworld-restapi.svg)](https://pypi.org/project/palworld-restapi/)
[![Python Versions](https://img.shields.io/pypi/pyversions/palworld-restapi.svg)](https://pypi.org/project/palworld-restapi/)

A modern, fast, and fully-typed Python client library and CLI wrapper for the official **Palworld Dedicated Server REST API**. Built on `httpx` to provide first-class support for both synchronous scripts and high-performance asynchronous applications.

## Features

- **Dual Clients**: Contains both `PalworldClient` (sync) and `AsyncPalworldClient` (async) using connection pooling for maximum performance.
- **Strict Typing**: Fully typed with PEP 561 compliance. API responses are parsed into rigorous Python Dataclasses for safety and excellent IDE autocomplete.
- **CLI Included**: Manage your Palworld server directly from your terminal using the built-in `palworld-cli`.
- **Modern**: Formatted with `ruff`, built with `hatchling`, and rigorously tested.

---

## Installation

You can install the package directly from PyPI:

```bash
pip install palworld-restapi
```
*(Or use `uv add palworld-restapi` if you are using `uv`)*

---

## Quickstart

### Async Client (Recommended for Bots / Web Apps)
```python
import asyncio
from palworld_restapi import AsyncPalworldClient

async def main():
    async with AsyncPalworldClient("http://127.0.0.1:8212", password="admin-password") as client:
        info = await client.get_info()
        print(f"Connected to {info.servername} (v{info.version})")
        
        # Announce a message to the server
        await client.announce("Hello from Python!")

if __name__ == "__main__":
    asyncio.run(main())
```

### Sync Client (Recommended for simple scripts)
```python
from palworld_restapi import PalworldClient

with PalworldClient("http://127.0.0.1:8212", password="admin-password") as client:
    players_resp = client.get_players()
    print(f"There are currently {len(players_resp.players)} players online.")
```

---

## Command Line Interface (CLI)

The package ships with a built-in CLI to easily manage your server without writing code. It supports loading credentials from `.env` files automatically.

```bash
# Get server info
palworld-cli info

# See online players
palworld-cli players

# Kick a player by Steam ID
palworld-cli kick steam_00000000000000000 --message "AFK too long"

# Shut the server down in 60 seconds
palworld-cli shutdown 60 --message "Restarting for an update!"
```

---

## Documentation & Examples

For full details, please refer to the documentation:
- **[Usage Guide](https://github.com/KJAyano/Palworld-RESTAPI/blob/main/docs/USAGE_GUIDE.md)**: Deep dive into using the Python clients.
- **[CLI Guide](https://github.com/KJAyano/Palworld-RESTAPI/blob/main/docs/CLI_GUIDE.md)**: Full command reference for the `palworld-cli` terminal tool.
- **[Endpoints Reference](https://github.com/KJAyano/Palworld-RESTAPI/blob/main/docs/ENDPOINTS.md)**: Available endpoints and payload details.

We also have a full suite of working scripts in the [`examples/`](https://github.com/KJAyano/Palworld-RESTAPI/tree/main/examples) directory demonstrating kick/ban management, player tracking, and server metrics.
