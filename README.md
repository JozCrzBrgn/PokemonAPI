# PokemonAPI
Creacion de una api de pokemon

## **Paso a paso de la solución del proyecto:**

En una carpeta que llamarémos `pokedex` se creó un ambiente virtual con el comando:
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
