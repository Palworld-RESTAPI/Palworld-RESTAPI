import argparse
import json
import os
import sys
from typing import Any
from dataclasses import asdict

from dotenv import load_dotenv

from .client import PalworldClient
from .errors import PalworldApiError


def print_json(obj: Any) -> None:
    print(json.dumps(obj, indent=2, default=str))


def main() -> None:
    parser = argparse.ArgumentParser(description="Palworld REST API CLI")
    parser.add_argument("--env", type=str, help="Path to .env file", default=".env")
    parser.add_argument("--base-url", type=str, help="Base URL for Palworld API")
    parser.add_argument(
        "--username", type=str, help="Username for Basic Auth", default="admin"
    )
    parser.add_argument("--password", type=str, help="Password for Basic Auth")
    parser.add_argument(
        "--timeout", type=float, help="Request timeout in seconds", default=10.0
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("info", help="Get server info")
    subparsers.add_parser("players", help="Get player list")
    subparsers.add_parser("settings", help="Get server settings")
    subparsers.add_parser("metrics", help="Get server metrics")

    announce_parser = subparsers.add_parser(
        "announce", help="Announce a message to the server"
    )
    announce_parser.add_argument("message", type=str, help="Message to announce")

    kick_parser = subparsers.add_parser("kick", help="Kick a player")
    kick_parser.add_argument("userid", type=str, help="User ID to kick")
    kick_parser.add_argument("--message", type=str, help="Kick message")

    ban_parser = subparsers.add_parser("ban", help="Ban a player")
    ban_parser.add_argument("userid", type=str, help="User ID to ban")
    ban_parser.add_argument("--message", type=str, help="Ban message")

    unban_parser = subparsers.add_parser("unban", help="Unban a player")
    unban_parser.add_argument("userid", type=str, help="User ID to unban")

    subparsers.add_parser("save", help="Save the world state")

    shutdown_parser = subparsers.add_parser("shutdown", help="Shutdown the server")
    shutdown_parser.add_argument("waittime", type=int, help="Wait time in seconds")
    shutdown_parser.add_argument("--message", type=str, help="Shutdown message")

    subparsers.add_parser("stop", help="Stop the server immediately")

    args = parser.parse_args()

    # Load environment variables
    if os.path.exists(args.env):
        load_dotenv(args.env)

    base_url = args.base_url or os.environ.get(
        "PALWORLD_BASE_URL", "http://127.0.0.1:8212"
    )
    username = os.environ.get("PALWORLD_USERNAME", args.username)
    password = args.password or os.environ.get("PALWORLD_PASSWORD")
    timeout = float(os.environ.get("PALWORLD_TIMEOUT", args.timeout))

    if not password:
        print(
            "Error: Password is required. Set it via --password or PALWORLD_PASSWORD.",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        with PalworldClient(
            base_url, password=password, username=username, timeout=timeout
        ) as client:
            if args.command == "info":
                print_json(asdict(client.get_info()))
            elif args.command == "players":
                print_json(asdict(client.get_players()))
            elif args.command == "settings":
                print_json(asdict(client.get_settings()))
            elif args.command == "metrics":
                print_json(asdict(client.get_metrics()))
            elif args.command == "announce":
                client.announce(args.message)
                print("Announcement sent successfully.")
            elif args.command == "kick":
                client.kick_player(args.userid, message=args.message)
                print(f"Player {args.userid} kicked successfully.")
            elif args.command == "ban":
                client.ban_player(args.userid, message=args.message)
                print(f"Player {args.userid} banned successfully.")
            elif args.command == "unban":
                client.unban_player(args.userid)
                print(f"Player {args.userid} unbanned successfully.")
            elif args.command == "save":
                client.save()
                print("World saved successfully.")
            elif args.command == "shutdown":
                client.shutdown(args.waittime, message=args.message)
                print(f"Shutdown initiated with wait time {args.waittime}s.")
            elif args.command == "stop":
                client.stop()
                print("Server stopped.")
    except PalworldApiError as e:
        print(f"API Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
