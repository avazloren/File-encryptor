# Encriptador de archivos ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## 📖​ Descripción

Este programa sirve para cifrar (`crypt.py`) y descifrar (`decrypt.py`) archivos en una carpeta.

Por defecto ambos scripts leen los archivos del directorio en el que están ubicados, si en ese directorio hay una carpeta los scripts se meterán en ella en busca de archivos.

Ambos scripts generan un archivo con registros `cipher.log`.

## ℹ️​ Sobre `key.salt`

Es un archivo binario que contiene 16 bytes de datos aleatorios. 

Se utiliza como entrada para el algoritmo `PBKDF2`, donde se mezcla con la contraseña del usuario para generar la clave de cifrado final. 

Su función es evitar que dos contraseñas iguales generen la misma clave y proteger contra ataques de diccionario o tablas de búsqueda (`Rainbow Tables`).

Es recomendable almacenar este archivo en una ubicación diferente para una mayor seguridad.

## 🛠️ Instalación y uso

```
sudo apt install python3 -y #ubuntu/debien based 


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


