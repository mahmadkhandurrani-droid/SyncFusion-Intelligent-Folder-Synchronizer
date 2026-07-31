from unittest.mock import MagicMock

from core.sync_engine import FolderSynchronizer


def test_logger(sample_config):

    logger = MagicMock()

    synchronizer = FolderSynchronizer(
        sample_config,
        logger
    )

    synchronizer.run()

    assert logger.info.called
