import os
from cryptography.fernet import Fernet
from crypt import generate_key_from_password, writeLog
import getpass as gp #replacing 'input', to hide the text entered by the user
import datetime

def decrypt_directory(target_path: str, fernet_obj: Fernet):
    """
    Recursively searches for and decrypts all files
    with the .encrypted extension in the directory.
    """
    # Ignore system/environment folders to save time
    ignored_items = [
        "__pycache__", "venv", "main.py", "decrypt.py",
        "crypt.py", "crypt.exe", "decrypt.exe", ".git",
        "ignore", "key.salt", "compose.yaml", ".gitignore", ".idea",  "cipher.log"
    ]

    for file_name in os.listdir(target_path):
        # Skip folders in the ignored list
        if file_name in ignored_items:
            continue

        full_path = os.path.join(target_path, file_name)

        # If it is a directory, apply recursion
        if os.path.isdir(full_path):
            writeLog("./cipher.log", f"Entering directory: {file_name}")
            decrypt_directory(full_path, fernet_obj)  # Recursive call

        # If it is a file and ends with .encrypted, decrypt it
        elif os.path.isfile(full_path) and file_name.endswith(".encrypted"):
            try:
                # 1. Read the encrypted content
                with open(full_path, "rb") as file:
                    encrypted_data = file.read()

                # 2. Decrypt (raises error if password/key is incorrect)
                original_data = fernet_obj.decrypt(encrypted_data)

                # 3. Restore the original filename by removing ".encrypted"
                new_path = full_path.replace(".encrypted", "")

                # 4. Write original file
                with open(new_path, "wb") as file:
                    file.write(original_data)

                # 5. Remove the encryted file
                os.remove(full_path)
                print(f"Restored: {os.path.basename(new_path)}")
                writeLog("./cipher.log", f"Decrypted file: {os.path.basename(new_path)}")

            except Exception:
                print(f"Error: Incorrect password or corrupted data for {file_name}")
                writeLog("./cipher.log", f"Error while decrypting: {file_name}")

if __name__ == "__main__":
    dt = datetime.datetime.now()
    writeLog("./cipher.log", f"--- Logs from decrypting process - {dt.strftime('%Y-%m-%d %H:%M:%S')} ---")
    if not os.path.exists("./key.salt"):
        print("Error: 'key.salt' not found! Cannot decrypt without the original salt.")
        writeLog("./cipher.log", f"Error: 'key.salt' not found!")
        exit(3)

    user_pass = gp.getpass("Enter the password to decrypt: ")

    print("Generating key from user input... (This might take a second)")
    try:
        # Generate the key ONCE before traversing the folders.
        # Since key.salt exists, the imported function will load it automatically.

        key = generate_key_from_password(user_pass)
        fernet_instance = Fernet(key)

        target_dir = "./"
        decrypt_directory(target_dir, fernet_instance)

        print("\nDecryption process completed.")
    except Exception as e:
        print(f"Critical error initializing decryption: {e}")