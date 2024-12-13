import os
import random

def secure_delete(file_path):
    """Securely delete a file by overwriting it with random data."""
    try:
        with open(file_path, 'r+b') as f:
            length = os.path.getsize(file_path)
            for _ in range(3):  # Overwrite 3 times
                f.seek(0)
                f.write(bytearray(random.getrandbits(8) for _ in range(length)))
        os.remove(file_path)
        print(f"File {file_path} securely deleted.")
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")
