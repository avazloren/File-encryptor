import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import getpass as gp #replacing 'input', to hide the text entered by the user
import datetime

ignored_items = [
        "__pycache__", "venv", "main.py", "decrypt.py",
        "crypt.py", "crypt.exe", "decrypt.exe", ".git",
        "ignore", "key.salt", "compose.yaml", ".gitignore", ".idea", "cipher.log", ".venv", "myvenv", "LICENSE", "README.md", "README-es.md"
    ] #the script will ignore the items on this list


def generate_key_from_password(password: str) -> bytes:
    #Function to generate a key from a password (string).

    password_bytes = password.encode()
    salt = readSalt("./key.salt")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
    return key

def readSalt(salt_path):
    '''
    Function to read and returns the salt from a file.
    If the salt file does not exist, it will be created.

    '''
    if os.path.exists(salt_path):
        # LOAD the existing salt
        with open(salt_path, "rb") as file:
            salt = file.read()
        print(f"Using existing salt from {salt_path}")
        writeLog("./cipher.log",f"[LOG] Using existing salt from {salt_path}")
    else:
        print("Salt file not found. Generatinng new one...")
        writeLog("./cipher.log", f"[WARNING] Salt file not found. New one will be created")
        salt = newSalt("./key.salt")


    return salt

def newSalt(salt_path):
    # GENERATE a new salt file
    try:
        salt = os.urandom(16)
        with open(salt_path, "wb") as file:
            file.write(salt)
        print("Generated new salt and saved to ./key.salt")
        writeLog("./cipher.log", f"[LOG] Generated new salt and saved to ./key.salt")
    except Exception as e:
        print(f"Error generating new salt: {e}")
        writeLog("./chipher.log", f"[ERROR] Error generating new salt: {e}")
        exit(3)

    return salt


def writeLog(log_path, content):
    try:
        with open(log_path, "a", newline="") as file:
            file.write(content)
            file.write("\n")
    except Exception as e:
        print(f"Unexpected error: {e}")
        exit(2)

    return True


def encrypt_directory(target_path: str, fernet_obj: Fernet):
    #This function encrypts all files in the specified directory, using the key generated in the function generate_key_from_password

    for file_name in os.listdir(target_path):
        # Skip ignored files or folders or already encrypted files immediately
        if file_name in ignored_items or file_name.endswith(".encrypted"):
            continue

        full_path = os.path.join(target_path, file_name) #gets the full file/directory path

        if os.path.isfile(full_path):
            try:
                with open(full_path, "rb") as file:
                    data = file.read()

                encrypted_data = fernet_obj.encrypt(data)

                with open(full_path + ".encrypted", "wb") as file:
                    file.write(encrypted_data)

                os.remove(full_path)
                print(f"Encrypted: {file_name}")
                writeLog("./cipher.log", f"[LOG] Encrypted: {file_name}")
            except Exception as e:
                print(f"Error encrypting {file_name}: {e}")
                writeLog("./cipher.log", f"[ERROR] Error encrypting {file_name}: {e}")

        elif os.path.isdir(full_path):
            # Pass 'full_path' to recursively encrypt subdirectories
            writeLog("./cipher.log", f"[LOG] Searching the directory: {file_name}")
            encrypt_directory(full_path, fernet_obj)



def list_file_to_encrypt(target_path):
    #This function lists all the files that are going to be encrypted
    for file_name in os.listdir(target_path):
        if file_name in ignored_items or file_name.endswith(".encrypted"): #continues to the for loop with the next iteration
            continue

        full_path = os.path.join(target_path, file_name)
        if os.path.isfile(full_path):
            print(file_name)

        elif os.path.isdir(full_path):
            list_file_to_encrypt(full_path) #calls again the function with the new directory


if __name__ == "__main__":
    dt = datetime.datetime.now()
    writeLog("./cipher.log",f"--- Logs from encrypting process - {dt.strftime('%Y-%m-%d %H:%M:%S')} ---")
    user_pass = gp.getpass("Enter the encryption password: ")

    if len(user_pass) < 4:
        print("Password is too short.")
    else:
        target_dir = "./"

        # Display root directory files before confirming

        print("\nThe following files will be encrypted:")
        list_file_to_encrypt(target_dir)

        decision = input("\nDo you want to continue? (Y/N): ")

        if decision.lower() == "y":
            writeLog("./cipher.log","[LOG] User decision: Y")
            print("Encrypting...")
            # Generate key and initialize Fernet
            fernet_key = generate_key_from_password(user_pass)
            fernet_instance = Fernet(fernet_key)

            # Start the encryption process
            encrypt_directory(target_dir, fernet_instance)
            print("Encryption finished successfully.")
        else:
            writeLog("./cipher.log", "[LOG] User decision: N")
            print("Operation canceled.")
            exit(1)