# CredentialCollector 🔐

A Python tool to recursively search for `Passwords.txt` files in a directory and extract stored credentials (URL, Username, Password).  
Extracted information is saved into a structured `credentials.json` file.

## 🧠 Use Case

This tool can help with:
- Recovering lost credentials
- Digital forensics
- Security audits on backup folders or exported data

> ⚠️ Use only on directories you **own** or have **explicit permission** to access.

---

## 🚀 Features

- Walks through all subdirectories
- Parses `Passwords.txt` files with known patterns
- Saves found credentials in a clean JSON format
- Handles file encoding errors gracefully

---

## 📦 Requirements

- Python 3.x (no external dependencies)

---

## 📂 Input Format

The tool looks for lines inside `Passwords.txt` that match this format:

URL: https://example.com
Username: myuser
Password: mypass123


Any file named exactly `Passwords.txt` found in any subdirectory will be parsed.

---

## ⚙️ Example Usage

```bash
$ python collect_credentials.py
Please enter the directory path: /Users/you/Desktop/backups

Information has been written to /Users/you/Desktop/credentials.json
```

Example credentials.json output:
```bash
[
  {
    "File_Name": "Dropbox_Backup",
    "URL": "https://example.com",
    "Username": "john_doe",
    "Password": "hunter2"
  }
]
```

## 📄 License

This project is licensed under the MIT License.

## 🔐 Legal Warning

❗ This tool is intended for educational, recovery, and authorized security testing only.
Unauthorized use on systems or files you do not own is strictly prohibited and may violate laws.
