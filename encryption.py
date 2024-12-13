from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def generate_key():
    """Generate a random 256-bit key."""
    return os.urandom(32)

def encrypt_file(file_path, key):
    """Encrypt a file using AES CBC mode."""
    with open(file_path, 'rb') as f:
        data = f.read()
    
    # Padding data to make it a multiple of block size
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    iv = os.urandom(16)  # Initialization vector
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Save the encrypted file with the IV at the beginning
    with open(file_path + '.enc', 'wb') as f:
        f.write(iv + encrypted_data)

def decrypt_file(file_path, key):
    """Decrypt a file using AES CBC mode."""
    with open(file_path, 'rb') as f:
        iv = f.read(16)
        encrypted_data = f.read()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Unpadding the decrypted data
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Save the decrypted file
    with open(file_path.replace('.enc', ''), 'wb') as f:
        f.write(data)
