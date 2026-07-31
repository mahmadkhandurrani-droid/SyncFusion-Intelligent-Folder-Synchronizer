"""
SyncFusion - Intelligent Folder Synchronizer

Main entry point of the application.
"""

from core.config import load_config
from core.logger import setup_logger
from core.sync_engine import FolderSynchronizer
from core.profiler import Profiler


def main():
    """
    Run the Folder Synchronizer application.
    """
    try:
        # Load configuration
        config = load_config("config.json")

        # Configure logger
        logger = setup_logger(config["log_file"])

        logger.info("=" * 50)
        logger.info("SyncFusion started.")

        # Create synchronizer
        synchronizer = FolderSynchronizer(
            config=config,
            logger=logger
        )

        # Run with profiler
        profiler = Profiler()
        profiler.run(synchronizer.run)

        logger.info("Synchronization completed successfully.")
        logger.info("=" * 50)

    except FileNotFoundError as error:
        print(f"Configuration Error: {error}")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

    except Exception as error:
        print(f"Unexpected Error: {error}")


if __name__ == "__main__":
    main()
