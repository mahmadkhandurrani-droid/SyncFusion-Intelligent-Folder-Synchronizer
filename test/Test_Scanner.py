from core.scanner import FolderScanner


def test_scan_folder(sample_config):
    scanner = FolderScanner(sample_config["source"])

    files = scanner.scan()

    assert len(files) == 1
