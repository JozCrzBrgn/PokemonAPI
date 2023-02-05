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

## **2) Modificación del archivo _models.py_:**
Dentro de la carpeta `api` en el archivo _models.py_, creamos una clase para describir a los entrenadores pokemon:
```
from django.db import models

# Create your models here.
class EntrenadorPokemon(models.Model):
    region = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    numero_medallas = models.PositiveSmallIntegerField()
```
Para poder verlo desde el administrador que nos provee Django, primero iremos al archivo de _admin.py_ y escribimos el siguiente código:
```
from django.contrib import admin
from .models import EntrenadorPokemon

# Register your models here.
admin.site.register(EntrenadorPokemon)
```
En la terminal, debemos ejecutar el siguiente comando para crear las bases de datos que necesita Django:
```
python manage.py migrate
```
Como confirmación de que todo ha ido bien hasta aquí, nos debe mandar los siguientes mensajes de **OK**:
<p align="center">
<img src="/ghImg/img3.png">
</p>

Para poder acceder al panel de administración, debemos crear un _super usuario_, esto lo haremos escribiendo el siguiente comando en la terminal:

```
python manage.py createsuperuser
```
Nos pedirá un nombre de usuario, un correo, una contraseña y la confirmación de la contraseña. Por último creamos las migraciones del modelo, esto lo hacemos ingresando en la terminal 

```
python manage.py makemigrations
```

<p align="center">
<img src="/ghImg/img4.png">
</p>

Podemos visualizar estas migraciones dentro de `PokemonAPI/api/migrations/0001_initial.py`. Cabe resaltar que se nos ha creado por defecto un campo llamado **_id_** que es autoincremental y funcionará como llave primaria.

<p align="center">
<img src="/ghImg/img5.png">
</p>

Hacemos una migracion de nuevo, para que actualize los datos:

```
python manage.py migrate
```
Volvemos a ejecutar nuestro panel de administración con el comando:

```
python manage.py runserver 8090
```
Cambiamos la dirección a `127.0.0.1:8090/admin` como se muestra:

<p align="center">
<img src="/ghImg/img6.png">
</p>

Se nos desplegará un _LogIn_, donde debemos introducir nuestro usuario y contraseña creado anteriormente.

<p align="center">
<img src="/ghImg/img7.png">
</p>

Damos _click_ en **Log in** y podemos acceder al administrador de Django: 

<p align="center">
<img src="/ghImg/img8.png">
</p>

Damos _click_ en **+ add** y se nos desplegará el siguiente formulario: 

<p align="center">
<img src="/ghImg/img9.png">
</p>

Llenamos los campos y damos click en **_SAVE_** para guardar nuestro primer registro:

<p align="center">
<img src="/ghImg/img10.png">
</p>

y nos dará un mensaje de que se ha agregado:

<p align="center">
<img src="/ghImg/img11.png">
</p>

Cremos uno más:

<p align="center">
<img src="/ghImg/img12.png">
</p>

## **3) Peticiones GET, POST, PUT y DELETE:**
