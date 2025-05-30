# Archiver
A robust Python-based directory archiving utility that scans and archives files with specific extensions (.txt, .py, etc.) from a given directory tree. Built using modern software engineering practices, including configuration-based design, logging, OOP principles, and error handling.


# FileArchiver

**FileArchiver** is a simple yet effective Python utility for archiving files from a specified directory into a `.zip` file.

It supports filtering files by extension and automatically logs actions and errors for traceability.

---

## 📂 Features

- ✅ Configurable file extensions and archive names
- 🧠 Graceful fallback to default settings if configuration is missing
- 📝 Automatic logging with timestamped log files
- 🧼 Clean and modular code structure
- 🕰️ Timestamped archive filenames

---

## 📁 Project Structure

```
FileArchiver/
│
├── main.py             # Main script to execute the archiving process
├── archiver.py         # Core FileArchiver class for zipping files
├── config.json         # Configuration file for paths, extensions, and archive name
└── logs/               # Logs directory (auto-generated)
```

---

## ⚙️ Configuration

Create a `config.json` file in the root directory:

```json
{
  "base_dir": "D:/New folder",
  "extensions": [".txt", ".py"],
  "archive_name": "Archive.zip"
}
```

If this file is not found, default values will be used:
- `base_dir`: Current working directory
- `extensions`: [".txt", ".py"]
- `archive_name`: "default_archive.zip"

---

## 🚀 Usage

1. Clone this repository or copy the files.
2. Place your `config.json` file in the project root (optional).
3. Run the script:

```bash
python main.py
```

4. Output will be a `.zip` archive in the same directory with a timestamped filename.

---

## 🧪 Example Output

```bash
Archived files with extensions ['.txt', '.py'] into '20250531_173045__Archive.zip'
```

---

## 🛠 Logging

All logs are stored in the `logs/` folder with a filename based on the current date (e.g., `logs/error20250531.log`).

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Contributing

Feel free to open issues or submit pull requests. Suggestions and improvements are always welcome!

---

## 👩‍💻 Author

**CodeBag Team**  
Instagram: [@codebag](https://instagram.com/codebag)  
YouTube: [Code Bag](https://youtube.com/@codebag)
