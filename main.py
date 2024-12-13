import sys
from encryption import encrypt_file, decrypt_file, generate_key
from secure_delete import secure_delete

def main():
    print("File Security Tool")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Securely delete a file")
    choice = input("Choose an option: ")

    if choice == '1':
        file_path = input("Enter the path of the file to encrypt: ")
        key = generate_key()  # In practice, save the key securely
        encrypt_file(file_path, key)
        print(f"File encrypted and saved as {file_path}.enc")

    elif choice == '2':
        file_path = input("Enter the path of the file to decrypt: ")
        key = input("Enter the encryption key: ")  # Ideally, get the key securely
        decrypt_file(file_path, key.encode())
        print(f"File decrypted and saved as {file_path.replace('.enc', '')}")

    elif choice == '3':
        file_path = input("Enter the path of the file to delete: ")
        secure_delete(file_path)

    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
