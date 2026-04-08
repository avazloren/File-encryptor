# File Encryptor ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## Description

This program is used to encrypt (`crypt.py`) and decrypt (`decrypt.py`) files within a folder.

By default, both scripts read files from the directory where they are located. If there is a subfolder within that directory, the scripts will enter it to search for more files.

Both scripts generate a log file named `cipher.log`.

## Installation and Usage

```
sudo apt install python3 -y 


#PIP
sudo apt install python3-pip python3-venv -y
python3 -m venv myvenv
source myvenv/bin/activate
pip install cryptography

#OR

# APT / DNF
sudo apt install python3-cryptography -y
sudo dnf install python3-cryptography -y


python3 crypt.py
python3 decrypt.py
```

