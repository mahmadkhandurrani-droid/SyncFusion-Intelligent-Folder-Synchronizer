# SyncFusion – Intelligent Folder Synchronizer

# Overview

SyncFusion is a modular Python automation project that keeps two folders synchronized. It detects newly added, modified, and deleted files while preserving the folder structure. The project follows software engineering best practices, including clean architecture, testing, logging, configuration management, concurrency, and performance profiling.

# Features

- Synchronize files between source and destination folders
- Detect new, modified, and deleted files
- Preserve directory structure
- JSON-based configuration
- Regular expression include/exclude filters
- Multithreaded synchronization using "ThreadPoolExecutor"
- Logging to console and file
- Performance profiling with "cProfile"
- Synchronization report generation
- Modular and maintainable codebase
- Comprehensive pytest test suite
- Fixtures, mocking, and parameterized tests
- Git-friendly project structure

# Technologies

- Python 3
- pathlib
- shutil
- json
- logging
- re
- concurrent.futures
- cProfile
- pytest
- unittest.mock

# Project Structure

folder_synchronizer/
├── main.py
├── config.json
├── core/
├── tests/
├── logs/
├── reports/
├── source/
└── destination/

# How It Works

1. Load configuration from "config.json".
2. Scan the source and destination folders.
3. Compare files to identify changes.
4. Apply regex filters.
5. Copy or update files using multiple threads.
6. Optionally remove extra files.
7. Write logs and generate a synchronization report.
8. Profile application performance.

$ python main.py
# Sample Output 
Starting synchronization...

Scanning source folder...
Scanning destination folder...

New files found: 3
Modified files: 1
Deleted files: 0

Copying report.pdf...
Copying notes.txt...
Copying image.jpg...
Updating data.csv...

Synchronization completed successfully.

Summary
-------------------------
Files Copied : 3
Files Updated: 1
Files Deleted: 0
Time Taken   : 0.21 seconds

Report saved to: reports/sync_report.txt
Log file saved to: logs/app.log

# Running the Project

python main.py

# Running Tests

pytest

# Learning Outcomes

This project demonstrates:

- Modular Python development
- File system automation
- Object-oriented programming
- Configuration management
- Unit testing with pytest
- Fixtures and mocking
- Parameterized testing
- Regular expressions
- Multi threading
- Performance profiling
- Git workflow and project organization

# License

MIT License
