# 🗂️ HR File Automation Tool

Automate your repetitive HR file tasks like renaming, format conversion, and file management with this Python-based offline toolkit.

**Created by:** Abdur Rahman Khan  
🔗 [LinkedIn – @seark](https://www.linkedin.com/in/seark)  
🗓️ July 13, 2025

---

## 📁 Directory Structure

```
HR_File_Automation_Tool/
├── scripts/              # Python automation scripts
├── input/
│   ├── sample_files/     # Drop your files here for processing
│   └── errors/           # Invalid or unrecognized files
├── output/
│   ├── renamed/          # Successfully renamed files
│   └── converted/        # Successfully converted files
├── logs/                 # Logs for rename & conversion tasks
├── documentation/
│   ├── user_guide.docx   # This user manual
│   └── screenshots/      # Before/after images
├── requirements.txt      # List of Python dependencies
├── README.md             # This file
└── LICENSE.txt           # Project license (MIT)
```

---

## 🛠️ Tools & Requirements

- **Python 3.8+** (Windows 10 Pro compatible)
- Works 100% offline after setup
- Dependencies listed in `requirements.txt`
- Optional: use a Python virtual environment for portability

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🚀 Features

### ✅ 1. Bulk File Renamer
- Prompts user for folder path
- Renames files using consistent HR-style format
- Moves invalid files to `input/errors/`
- Supports dry-run preview before renaming
- Logs all actions in `logs/rename_log.txt`

### ✅ 2. Document Converter
- Converts `.csv`, `.xlsx`, `.docx`, `.txt`, `.pdf` into `.csv`, `.json`, or `.txt`
- Batch processes entire folders
- Moves failed files to `input/errors/`
- Logs conversion actions in `logs/conversion_log.txt`

---

## 🧾 Manual Usage Guide

1. Download or clone this repo from GitHub.
2. Extract the ZIP (if applicable).
3. Open terminal in the main folder.
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run a script:
   ```bash
   python scripts/rename_files.py
   python scripts/convert_documents.py
   ```
6. Optionally use an IDE like VS Code or PyCharm to run scripts directly.
7. Input paths and options when prompted.

---

## 📸 Screenshots

Screenshots showing before/after renaming and conversion are located in:
```
/documentation/screenshots/
```

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE) — free to use, share, and modify with attribution.

---

## 🙋‍♂️ About the Author

**Abdur Rahman Khan**  
Python Automation & IT Support Specialist  
🔗 [LinkedIn – @seark](https://www.linkedin.com/in/seark)
