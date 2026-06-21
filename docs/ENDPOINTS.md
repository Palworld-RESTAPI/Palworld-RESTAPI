# Palworld REST API Endpoints

Base URL for all endpoints: `http://<host>:8212/v1/api`
Authentication: **HTTP Basic** (`admin` / `AdminPassword`)

| Method | Endpoint | Description | Request Body | Response Body |
|--------|----------|-------------|--------------|---------------|
| `GET` | `/info` | Get server info | - | `ServerInfo` |
| `GET` | `/players` | Get list of online players | - | `PlayersResponse` |
| `GET` | `/settings` | Get server settings | - | `ServerSettings` |
| `GET` | `/metrics` | Get server metrics | - | `ServerMetrics` |
| `POST` | `/announce` | Send a server announcement | `{"message": "str"}` | - |
| `POST` | `/kick` | Kick a player | `{"userid": "str", "message": "str"}` | - |
| `POST` | `/ban` | Ban a player | `{"userid": "str", "message": "str"}` | - |
| `POST` | `/unban` | Unban a player | `{"userid": "str"}` | - |
| `POST` | `/save` | Save the server world state | - | - |
| `POST` | `/shutdown` | Shutdown the server | `{"waittime": int, "message": "str"}` | - |
| `POST` | `/stop` | Force stop the server | - | - |

> [!NOTE]
> All successful `POST` endpoints return a `200 OK` status without a specific JSON body.
> All endpoints will return `401 Unauthorized` if invalid credentials are provided.
> Endpoints will return `400 Bad Request` if payload is invalid.
