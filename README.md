# File Encryptor ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## 📖​ Description

This program is used to encrypt (`crypt.py`) and decrypt (`decrypt.py`) files within a folder.

By default, both scripts read files from the directory where they are located. If there is a subfolder within that directory, the scripts will enter it to search for more files.

Both scripts generate a log file named `cipher.log`.


## ℹ️​ About `key.salt`

This is a binary file containing 16 bytes of random data.

It is used as an input for the `PBKDF2` algorithm, where it is mixed with the user's password to generate the final encryption key.

Its purpose is to prevent identical passwords from generating the same key and to protect against dictionary attacks or lookup tables (`Rainbow Tables`).

For enhanced security, it is recommended to store this file in a separate location

## 🛠️ Installation and Usage

```
sudo apt install python3 -y #ubuntu/debian based


#PIP
sudo apt install python3-pip python3-venv -y
python3 -m venv myvenv
source myvenv/bin/activate
pip install cryptography

#OR

# APT
sudo apt install python3-cryptography -y


python3 crypt.py
python3 decrypt.py
```

