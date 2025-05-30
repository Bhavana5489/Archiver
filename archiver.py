import os
import zipfile
import logging
from datetime import datetime


class FileArchiver:
    """
    A class to archive files from a specified directory into a zip file,
    filtering by specific file extensions.

    Attributes:
        base_dir (str): The root directory to search for files.
        extensions (list): List of file extensions to include in the archive.
        archive_name (str): Name of the output zip archive file.
    """

    def __init__(self, base_dir, extensions=None, archive_name="archive.zip"):
        """
        Initializes the FileArchiver instance.

        Args:
            base_dir (str): Path of the directory to archive files from.
            extensions (list, optional): List of file extensions to include. Defaults to ['.txt', '.py'].
            archive_name (str, optional): Name of the resulting archive file. Defaults to 'archive.zip'.
        """
        self.base_dir = base_dir
        self.extensions = extensions or [".txt", ".py"]
        self.archive_name = archive_name
        self._setup_logger()
        logging.info("\n\nProgram Started")

    def _setup_logger(self):
        """
        Sets up the logging configuration to write logs to a file
        located in a 'logs' directory with the current date in its filename.
        """
        os.makedirs("logs", exist_ok=True)
        logging.basicConfig(
            filename=f"logs/error{datetime.now().strftime('%Y%m%d')}.log",
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            force=True,
        )

    def _is_valid_extension(self, filename):
        """
        Checks if the file has a valid extension based on the provided list.

        Args:
            filename (str): Name of the file to check.

        Returns:
            bool: True if the file matches one of the allowed extensions, False otherwise.
        """
        return any(filename.lower().endswith(ext) for ext in self.extensions)

    def archive(self):
        """
        Archives all files with valid extensions from the base directory into a zip file.

        This method traverses the base directory recursively, identifies files
        that match the allowed extensions, and adds them to a zip archive.
        Logs each added file and any errors encountered.
        """
        try:
            with zipfile.ZipFile(
                self.archive_name, "w", zipfile.ZIP_DEFLATED
            ) as archive:
                for root, _, files in os.walk(self.base_dir):
                    for file in files:
                        if self._is_valid_extension(file):
                            file_path = os.path.join(root, file)
                            # Use relative path so folder structure inside zip is preserved
                            arcname = os.path.relpath(file_path, start=self.base_dir)
                            archive.write(file_path, arcname)
                            logging.info(f"{file} is added to zip")

            print(
                f"Archived files with extensions {self.extensions} into '{self.archive_name}'"
            )
            logging.info(
                f"Archived files with extensions {self.extensions} into '{self.archive_name}'"
            )
        except Exception as e:
            logging.error(f"Failed to archive files: {e}")
            print(
                "An error occurred during archiving. Check logs/error.log for details."
            )
