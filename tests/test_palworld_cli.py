import pytest
from unittest.mock import patch, MagicMock
from palworld_restapi.cli import main
from palworld_restapi import ServerInfo


@patch("palworld_restapi.cli.PalworldClient")
@patch(
    "sys.argv",
    ["palworld-cli", "--base-url", "http://test", "--password", "testpass", "info"],
)
def test_cli_info(mock_client_class):
    mock_instance = MagicMock()
    mock_client_class.return_value.__enter__.return_value = mock_instance
    mock_instance.get_info.return_value = ServerInfo(
        version="1.0",
        servername="Test",
        description="Test desc",
        worldguid="1234",
        raw={},
    )

    main()

    mock_instance.get_info.assert_called_once()


@patch("palworld_restapi.cli.PalworldClient")
@patch(
    "sys.argv",
    [
        "palworld-cli",
        "--base-url",
        "http://test",
        "--password",
        "testpass",
        "announce",
        "Hello!",
    ],
)
def test_cli_announce(mock_client_class):
    mock_instance = MagicMock()
    mock_client_class.return_value.__enter__.return_value = mock_instance

    main()

    mock_instance.announce.assert_called_once_with("Hello!")


@patch("sys.argv", ["palworld-cli", "info"])
def test_cli_missing_password(capsys):
    with pytest.raises(SystemExit) as exc:
        main()

    assert exc.value.code == 1
    captured = capsys.readouterr()
    assert "Error: Password is required" in captured.err
