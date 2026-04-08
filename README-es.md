# Encriptador de archivos ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Descripción

Este programa sirve para cifrar (`crypt.py`) y descifrar (`decrypt.py`) archivos en una carpeta.

Por defecto ambos scripts leen los archivos del directorio en el que están ubicados, si en ese directorio hay una carpeta los scripts se meterán en ella en busca de archivos.

Ambos scripts generan un archivo con registros `cipher.log`.

## Instalación y uso

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


