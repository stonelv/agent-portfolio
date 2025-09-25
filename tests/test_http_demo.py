import json
from pathlib import Path
from unittest.mock import patch, MagicMock
from scripts import http_demo


def test_fetch_todo_success():
    fake_json = {"id": 1, "title": "Test", "completed": False}
    mock_resp = MagicMock()
    mock_resp.json.return_value = fake_json
    mock_resp.raise_for_status.return_value = None

    with patch("requests.get", return_value=mock_resp) as mock_get:
        data = http_demo.fetch_todo()
        mock_get.assert_called_once()
        assert data == fake_json


def test_main_prints_output(tmp_path, capsys):
    fake_json = {"id": 2, "title": "Another", "completed": True}
    mock_resp = MagicMock()
    mock_resp.json.return_value = fake_json
    mock_resp.raise_for_status.return_value = None

    with patch("requests.get", return_value=mock_resp):
        http_demo.main()
    captured = capsys.readouterr().out
    assert "Fetched TODO:" in captured
    assert "id: 2" in captured
    assert "completed: True" in captured
