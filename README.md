# File Security Tool

A command-line tool for encrypting, decrypting, and securely deleting files.

## Features:
- **Encrypt files**: Encrypt any file with AES encryption.
- **Decrypt files**: Decrypt encrypted files.
- **Secure file deletion**: Overwrite and securely delete files to prevent recovery.

## Usage:
1. Run the executable.
2. Choose an option:
   - Encrypt a file
   - Decrypt a file
   - Securely delete a file

## Installation:
- Install dependencies: `pip install cryptography`
- Create the executable: `pyinstaller --onefile main.py`
