# PokemonAPI
Creacion de una api de pokemon

# **Paso a paso de la solución del proyecto:**

## **1) Inicialización:**

Se abrió **Visual Studio** en una carpeta que llamarémos `PokemonAPI` y se creó un ambiente virtual desde la terminal con el comando:
```
py -m venv my_venv
```
Para poder usar el ambiente virtual, se procedio a activarlo:
```
.\my_venv\Scripts\activate
```
En el `my_venv` se instalaron las librerias a usar con el comando *pip*:
```
pip install django
```
Se creó un nuevo projecto en Django:
```
django-admin startproject restAPI .
```
Para comprobar que no hay algún error se ejecutó la aplicación:
```
python manage.py runserver 8090
```
<p align="center">
<img src="/ghImg/img1.png">
</p>

A continuación, creamos la _**app**_ para nuestra _**api**_ con la instrucción:
```
django-admin startapp api
```
Dentro de la carpeta `restAPI` en el archivo _settings.py_, agregamos el nombre de nuestra app, llamada _**api**_ en la lista _INSTALLED_APPS_ como se muestra:
<p align="center">
<img src="/ghImg/img2.png">
</p>

## **2) Modificación del archivo _models_:**
