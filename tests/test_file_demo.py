from pathlib import Path
from scripts import file_demo


def test_file_write_and_append(tmp_path: Path, monkeypatch):
    # redirect DATA_FILE to temp dir
    demo_file = tmp_path / "demo.txt"
    monkeypatch.setattr(file_demo, "DATA_FILE", demo_file)

    # first run creates + appends
    file_demo.main()
    lines_first = demo_file.read_text(encoding="utf-8").splitlines()
    assert len(lines_first) == 2
    assert lines_first[0].startswith("Line 1:")

    # second run appends one more line
    file_demo.main()
    lines_second = demo_file.read_text(encoding="utf-8").splitlines()
    assert len(lines_second) == 3
