"""
FileArchiver is a simple yet effective Python utility for archiving files from a specified directory into a .zip file.
It supports filtering files by extension and automatically logs actions and errors for traceability.

The project reads configuration settings from a config.json file (or uses sensible defaults if not found), and
generates a timestamped archive containing only the specified file types. This tool is especially useful for backing
up code, documents, or any other filtered content in a structured and repeatable way.

Features--
Configurable file extensions and archive names
Automatic logging with timestamped logs
Graceful fallback to default settings if configuration is missing
Clean and modular code structure

Main script to initialize and run the FileArchiver using parameters from a configuration file.
If `config.json` is not found in the current directory, default settings will be used.
"""

import json
import os
from archiver import FileArchiver
from datetime import datetime


def load_config(config_path="config.json"):
    """
    Loads configuration settings from a JSON file.

    Args:
        config_path (str): Path to the configuration file. Defaults to 'config.json'.

    Returns:
        dict: A dictionary containing 'base_dir', 'extensions', and 'archive_name' keys.
              If the config file is missing, defaults are returned.
    """
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return json.load(f)
    else:
        print("⚠️ config.json not found. Using default parameters.")
        return {
            "base_dir": os.getcwd(),  # Use current working directory as default
            "extensions": [".txt", ".py"],  # Default file types to archive
            "archive_name": "default_archive.zip",  # Default output archive name
        }


if __name__ == "__main__":
    try:
        # Load configuration from file or use default values
        config = load_config()

        # Initialize FileArchiver with loaded config and a timestamped archive name
        archiver = FileArchiver(
            base_dir=config["base_dir"],
            extensions=config["extensions"],
            archive_name=f"{datetime.now().strftime('%Y%m%d_%H%M%S')}__"
            + config["archive_name"],
        )

        # Run the archiving process
        archiver.archive()
    except Exception as e:
        print("Critical failure at program startup. Please check configuration.")
