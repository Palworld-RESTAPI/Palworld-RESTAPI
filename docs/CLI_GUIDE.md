# Palworld-RESTAPI Command Line Interface (CLI)

The `palworld-cli` tool allows you to query and manage your Palworld dedicated server directly from your terminal.

## Authentication & Configuration

The CLI requires your server's REST API URL and the Admin Password. 

You can provide these in **three** ways, in order of priority:

1. **Command Line Arguments**:
   ```bash
   palworld-cli --base-url "http://127.0.0.1:8212" --password "your_password" info
   ```

2. **Environment Variables**:
   ```bash
   export PALWORLD_BASE_URL="http://127.0.0.1:8212"
   export PALWORLD_PASSWORD="your_password"
   palworld-cli info
   ```

3. **Dotenv (`.env`) File** (Recommended):
   Create a `.env` file in the folder where you run the command. The CLI automatically loads it.
   ```env
   PALWORLD_BASE_URL=http://127.0.0.1:8212
   PALWORLD_USERNAME=admin
   PALWORLD_PASSWORD=your_password
   PALWORLD_TIMEOUT=10.0
   ```
   *Note: If your `.env` file is located somewhere else, you can pass `--env /path/to/.env`.*

---

## Available Commands

All data-fetching commands output their results in clean, formatted **JSON**, making it perfect for piping into other tools like `jq`.

### `info`
Gets general server information (version, name, GUID).
```bash
palworld-cli info
```

### `metrics`
Gets current server metrics (FPS, uptime, current players).
```bash
palworld-cli metrics
```

### `players`
Gets a list of all currently online players, including their level, ping, and Steam ID.
```bash
palworld-cli players
```

### `settings`
Gets the extensive list of server configurations (difficulty, drop rates, PvP settings, etc.).
```bash
palworld-cli settings
```

### `announce`
Broadcasts a system message to all online players.
```bash
palworld-cli announce "Server will restart in 5 minutes!"
```

### `kick`
Kicks a player from the server using their `userid` (Steam ID). An optional message can be provided.
```bash
palworld-cli kick steam_00000000000000000
palworld-cli kick steam_00000000000000000 --message "AFK too long"
```

### `ban`
Bans a player from the server using their `userid`.
```bash
palworld-cli ban steam_00000000000000000 --message "Cheating"
```

### `unban`
Unbans a previously banned player.
```bash
palworld-cli unban steam_00000000000000000
```

### `save`
Forces an immediate save of the world state.
```bash
palworld-cli save
```

### `shutdown`
Initiates a graceful server shutdown. Requires a `waittime` (in seconds).
```bash
palworld-cli shutdown 60 --message "Restarting for update"
```

### `stop`
Forces the server to stop immediately without a grace period.
```bash
palworld-cli stop
```
