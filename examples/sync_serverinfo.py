from palworld_restapi import PalworldClient, PalworldApiError


def main():
    server_url = "http://127.0.0.1:8212"
    password = "admin_password"

    try:
        # The sync client is great for simple scripting!
        with PalworldClient(server_url, password=password) as client:
            info = client.get_info()
            print("--- Sync Client Example ---")
            print(f"Server Name: {info.servername}")
            print(f"Version: {info.version}")
    except PalworldApiError as e:
        print(f"API Error: {e}")


if __name__ == "__main__":
    main()
