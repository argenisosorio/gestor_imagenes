# Gestor de imágenes que permite subir recuros digitales a un servidor y luego listarlos para descargarlos.

Desarrollado por: Ing. Argenis Osorio en la Fundación CENDITEL.

## Paquetes requeridos

De GNU/Linux Debian
```
sqlite3
```

De Python
```
Django==1.8.8
Python==2.7
```

Usaremos $ para describir los comandos que se usaran con usuario regular.

Usaremos # para describir los comandos que se usaran con superusuario. 

## Instalación de paquetes para crear entornos virtuales
```
# apt-get install install python-setuptools python-dev python-pip

# apt-get install python-virtualenv virtualenvwrapper
```
## Crear un entorno virtual de python
```
$ virtualenv mi_env

$ source mi_env/bin/activate
```

## Instalación de requerimientos del proyecto
```
$ pip install -r gestor_imagenes/requirements.txt 
```

## Probar el proyecto
```
$ cd gestor_imagenes

$ cp gestor_imagenes/settings.py_example gestor_imagenes/settings.py
```

## Ejecutar las migraciones y correr el servidor de desarrollo
```
$ bash reset_db.sh

$ python manage.py runserver
```

## Capturas

![captura-1.png](captura-1.png "captura-1.png")
