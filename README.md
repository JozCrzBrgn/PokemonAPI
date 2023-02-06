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

## **3) Método GET**

Antes de empezar con el método **GET**, debemos incluir las **_url_** que usarémos desde nuestra **api**. Iremos al archivo _urls.py_ que se encuetra en `PokemonAPI/restAPI/urls.py` e incluiremos la libreria _include_ y el _path_ que se muestra:

<p align="center">
<img src="/ghImg/img13.png">
</p>

El archivo donde se encuentran estas **api.urls** aun no existe. Haci que crearemos un archivo llamado **urls.py** en la dirección `PokemonAPI/api/urls.py` y ahi agregaremos el _path_:

```
path('entrenadores/', EntrenadorPokemonView.as_view(), name='entrenadores_list'),
```

que nos servira cuando se quieran consultar todos los entrenadores, y el _path_:

```
path('entrenadores/<int:id>', EntrenadorPokemonView.as_view(), name='entrenadores_procesos'),
```
que nos servirá cuando se quiere hacer una consulta GET para un _id_ especifico o para hacer un POST, PUT y DELETE. 

En este archivo tambien debemos incluir la clase **EntrenadorPokemonView** que importaremos de _views_, esta clase aun no existe.

En resumen, este archivo debe quedar por el momento, como se muestra a continuación:

<p align="center">
<img src="/ghImg/img14_1.png">
</p>

Para comenzar con el método **GET** debemos ir `PokemonAPI/api/views.py` en el archivo _views.py_. Aquí debemos crear la clase **EntrenadorPokemonView** con su método GET usando el siguiente código:
```
from django.shortcuts import render
from django.views import View
from .models import EntrenadorPokemon
from django.http.response import JsonResponse

# Create your views here.
class EntrenadorPokemonView(View):
    def get(self, request, id=0):
        if id>0:
            entrenadores = list(EntrenadorPokemon.objects.filter(id=id).values())
            if len(entrenadores)>0:
                entrenador=entrenadores[0]
                datos={'message':"Entrenador encontrado", 'entrenador':entrenador}
            else:
                datos={'message':"Entrenador no encontrado..."}
            return JsonResponse(datos)
        else:
            entrenadores = list(EntrenadorPokemon.objects.values())
            if len(entrenadores)>0:
                datos={'message':"Entrenador encontrado", 'entrenadores':entrenadores}
            else:
                datos={'message':"Entrenador no encontrado..."}
            return JsonResponse(datos)
```
Este método nos permite hacer una petición para consultar uno o todos los entrenadores pokemon que esten en nuestra base de datos. 

Para probar nuestro método GET, harémos usos del plugin **Thunder Client** que servirá como cliente REST. Para usarlo, damos click en _New Request_.

<p align="center">
<img src="/ghImg/img15.png">
</p>

Se nos desplegará una nueva pantalla y debemos ingresar la dirección:

```
http://127.0.0.1:8090/api/entrenadores/
```

y dar click en _Send_:

<p align="center">
<img src="/ghImg/img16_1.png">
</p>

esto nos devolverá una respuesta en formato JSON con todos los resultados que teniamos en la base de datos:

<p align="center">
<img src="/ghImg/img17.png">
</p>

Consultaremos ahora solo con un _id_:

```
http://127.0.0.1:8090/api/entrenadores/2
```

<p align="center">
<img src="/ghImg/img18.png">
</p>

Por último, harémos una consulta de un _id_ que no existe:

```
http://127.0.0.1:8090/api/entrenadores/99
```

<p align="center">
<img src="/ghImg/img19.png">
</p>

Esto demuestra que el método GET funciona muy bien.

## **4) Método POST**

Primero debemos crear un _crsf_ para poder autenticar que estamos haciendo las peticiones desde nuestro proyecto, esto lo evitamos con el decorador **csrf_exempt**. Y tambíen harémos uso de la librería para JSON, todo esto lo importamos como:

```
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
```

Para usar el **csrf_exempt** usarémos una función llamada **dispatch**:

```
@method_decorator(csrf_exempt)
def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
```

Ahora sí, nuestro método POST quedaría como:

```
def post(self, request):
    jd = json.loads(request.body)
    print(jd)
    EntrenadorPokemon.objects.create(
        region = jd['region'], 
        tipo = jd['tipo'], 
        numero_medallas = jd['numero_medallas']
        )
    datos={'message':"Entrenador creado !"}
    return JsonResponse(datos)
```

En resumen, nuestro archivo _views.py_ quedaría hasta ahora como:

```
from django.shortcuts import render
from django.views import View
from .models import EntrenadorPokemon
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class EntrenadorPokemonView(View):
    def get(self, request, id=0):
        if id>0:
            entrenadores = list(EntrenadorPokemon.objects.filter(id=id).values())
            if len(entrenadores)>0:
                entrenador=entrenadores[0]
                datos={'message':"Entrenador encontrado", 'entrenador':entrenador}
            else:
                datos={'message':"Entrenador no encontrado..."}
            return JsonResponse(datos)
        else:
            entrenadores = list(EntrenadorPokemon.objects.values())
            if len(entrenadores)>0:
                datos={'message':"Entrenador encontrado", 'entrenadores':entrenadores}
            else:
                datos={'message':"Entrenador no encontrado..."}
            return JsonResponse(datos)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        jd = json.loads(request.body)
        print(jd)
        EntrenadorPokemon.objects.create(
            region = jd['region'], 
            tipo = jd['tipo'], 
            numero_medallas = jd['numero_medallas']
            )
        datos={'message':"Entrenador creado !"}
        return JsonResponse(datos)
```

Para probar el método POST hacemos un nuevo request (cuadro verde) a la dirección (cuadro rojo):

```
http://127.0.0.1:8090/api/entrenadores/
```

pero mandando como parámetro el JSON en la sección del _body_ (cuadro azul):

```
{
  "region":"Alola",
  "tipo":"Maestro Pokémon",
  "numero_medallas":15
}
```

<p align="center">
<img src="/ghImg/img20.png">
</p>

y al dar click en _Send_, obtenemos que la respuesta fue exitosa:

<p align="center">
<img src="/ghImg/img21.png">
</p>

## **5) Método PUT**

El método PUT nos permitirá modificar los datos ingresados. 

Queda definido por la siguiente función:

```
def put(self, request, id):
    jd = json.loads(request.body)
    entrenadores = list(EntrenadorPokemon.objects.filter(id=id).values())
    if len(entrenadores)>0:
        entrenador = EntrenadorPokemon.objects.get(id=id)
        entrenador.region = jd['region']
        entrenador.tipo = jd['tipo']
        entrenador.numero_medallas = jd['numero_medallas']
        entrenador.save()
        datos={'message':"Entrenador editado!"}
    else:
        datos={'message':"entrenador no encontrado..."}
    return JsonResponse(datos)
```

Antes de modificar algun registro, usarémos el método GET para obtener el entrenador 2 y así poder comparar. 

El resultado de la consulta es:

<p align="center">
<img src="/ghImg/img22.png">
</p>

Para probar el método PUT hacemos un nuevo request (cuadro verde) a la dirección (cuadro rojo):

```
http://127.0.0.1:8090/api/entrenadores/2
```

pero mandando como parámetro el JSON en la sección del _body_ (cuadro azul):

```
{
  "region":"Sinnoh",
  "tipo":"Coordinador Pokémon",
  "numero_medallas":10
}
```

<p align="center">
<img src="/ghImg/img23.png">
</p>

y al dar click en _Send_, obtenemos que la respuesta fue exitosa:

<p align="center">
<img src="/ghImg/img24.png">
</p>

Usando el método GET para obtener el entrenador 2, vemos que ha sido editado:

<p align="center">
<img src="/ghImg/img25.png">
</p>

Por último, harémos una edición de un _id_ que no existe:

```
http://127.0.0.1:8090/api/entrenadores/99
```

<p align="center">
<img src="/ghImg/img26.png">
</p>

Esto demuestra que el método PUT funciona muy bien.

## **6) Método DELETE**

El método DELETE nos permitirá eliminar los datos ingresados. 

Queda definido por la siguiente función:

```
def delete(self, request, id):
    Entrenadores = list(EntrenadorPokemon.objects.filter(id=id).values())
    if len(Entrenadores)>0:
        EntrenadorPokemon.objects.filter(id=id).delete()
        datos={'message':"Entrenador eliminado!"}
    else:
        datos={'message':"Entrenador no encontrado..."}
    return JsonResponse(datos)
```

Antes de usar el método DELETE, hacemos un GET para listar todos los cursos y así poder comparar:

<p align="center">
<img src="/ghImg/img27.png">
</p>

Para probar el método DELETE hacemos un nuevo request (cuadro verde) a la dirección (cuadro rojo) para eliminar el registro 2:

```
http://127.0.0.1:8090/api/entrenadores/2
```

<p align="center">
<img src="/ghImg/img28.png">
</p>

y al dar click en _Send_, obtenemos que la respuesta fue exitosa:

<p align="center">
<img src="/ghImg/img29.png">
</p>

Usando el método GET volvemos a listar todos los items y vemos que ha sido eliminado el registro 2:

<p align="center">
<img src="/ghImg/img30.png">
</p>

Por último, elimarémos un _id_ que no existe:

```
http://127.0.0.1:8090/api/entrenadores/99
```

<p align="center">
<img src="/ghImg/img31.png">
</p>

Esto demuestra que el método DELETE funciona muy bien.

## **7) Método GET de la clase PokemonView**

Para poder consumir la api de Pokémon debemos usar el método get para obtener toda la información de `https://pokeapi.co/` y transformala a un formato JSON para poder obtener las características que necesitemos del pokémon, que en este caso serán su **_id, nombre, peso y altura._**

Crearémos una clase nueva en nuestro archivo _views.py_, que se llamará **PokemonView** que quedará de la siguiente forma:

```
class PokemonView(View):
    def get(self, request, pokemon):  
        try:
            url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
            url_pokeapi.add_header('User-Agent', 'charmander')
            source = urllib.request.urlopen(url_pokeapi).read()
            jd = json.loads(source)
            datos={'id':jd['id'], 'nombre':jd['name'], 'altura':jd['height'], 'peso':jd['weight']}
            return JsonResponse(datos)
        except:
            datos={'message':"Pokemon no encontrado..."}
            return JsonResponse(datos)
```

Para que esta clase pueda funcionar importamos la librería que se muestra a continuación:

```
import urllib.request
```

Por último debemos incluir esta clase en el path, así que nos dirigimos a `PokemonAPI/api/urls.py`. Este archivo debe quedar como se muestra:

```
from django.urls import path
from .views import EntrenadorPokemonView, PokemonView

urlpatterns = [
    path('entrenadores/', EntrenadorPokemonView.as_view(), name='entrenadores_list'),
    path('entrenadores/<int:id>', EntrenadorPokemonView.as_view(), name='entrenadores_procesos'),
    path('pokemon/<str:pokemon>', PokemonView.as_view(), name='pokemon'),
]
```

Con esto también hemos terminado de editar el archivo _views.py_. A manera de resumen se muestra el código terminado:

```
from django.shortcuts import render
from django.views import View
from .models import EntrenadorPokemon
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import urllib.request

# Create your views here.
class EntrenadorPokemonView(View):
    def get(self, request, id=0):
        if id>0:
            entrenadores = list(EntrenadorPokemon.objects.filter(id=id).values())
            if len(entrenadores)>0:
                entrenador=entrenadores[0]
                datos={'message':"Entrenador encontrado", 'entrenador':entrenador}
            else:
                datos={'message':"Entrenador no encontrado..."}
            return JsonResponse(datos)
        else:
            entrenadores = list(EntrenadorPokemon.objects.values())
            if len(entrenadores)>0:
                datos={'message':"Entrenador encontrado", 'entrenadores':entrenadores}
            else:
                datos={'message':"Entrenador no encontrado..."}
            return JsonResponse(datos)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        jd = json.loads(request.body)
        print(jd)
        EntrenadorPokemon.objects.create(
            region = jd['region'], 
            tipo = jd['tipo'], 
            numero_medallas = jd['numero_medallas']
            )
        datos={'message':"Entrenador creado!"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        entrenadores = list(EntrenadorPokemon.objects.filter(id=id).values())
        if len(entrenadores)>0:
            entrenador = EntrenadorPokemon.objects.get(id=id)
            entrenador.region = jd['region']
            entrenador.tipo = jd['tipo']
            entrenador.numero_medallas = jd['numero_medallas']
            entrenador.save()
            datos={'message':"Entrenador editado!"}
        else:
            datos={'message':"Entrenador no encontrado..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        Entrenadores = list(EntrenadorPokemon.objects.filter(id=id).values())
        if len(Entrenadores)>0:
            EntrenadorPokemon.objects.filter(id=id).delete()
            datos={'message':"Entrenador eliminado!"}
        else:
            datos={'message':"Entrenador no encontrado..."}
        return JsonResponse(datos)


class PokemonView(View):
    def get(self, request, pokemon):  
        try:
            url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
            url_pokeapi.add_header('User-Agent', 'charmander')
            source = urllib.request.urlopen(url_pokeapi).read()
            jd = json.loads(source)
            datos={'id':jd['id'], 'nombre':jd['name'], 'altura':jd['height'], 'peso':jd['weight']}
            return JsonResponse(datos)
        except:
            datos={'message':"Pokemon no encontrado..."}
            return JsonResponse(datos)
```

Ahora vamos a probar el funcionamiento de la clase **PokemonView** usando **Thunder Client**, así que ingresamos la dirección (cuadro rojo):

```
http://127.0.0.1:8090/api/pokemon/squirtle
```

, seleccionamos el método GET (cuadro verde) y damos click en en _Send_ (cuadro azul):

<p align="center">
<img src="/ghImg/img32.png">
</p>

Esto nos retorna la siguente respuesta:

<p align="center">
<img src="/ghImg/img33.png">
</p>

Ingresaremos ahora un pokemón que no exista:

```
http://127.0.0.1:8090/api/pokemon/squirtle_XX
```

<p align="center">
<img src="/ghImg/img34.png">
</p>

Esto demuestra que el método GET de la clase **PokemonView** funciona muy bien.

## **8) Configuración de Django para su despliegue. **

Dentro de nuestro archivo `.gitignore` vamos a escribir:

```
db.sqlite3
my_venv
__pycache__
```

Esto para ignorar esos archivos. En la termial escribimos:

```
git add .
```

y damos enter. Despues escribimos:

```
git commit -m "archivos a ignorar"
```
y damos enter. 

Como ayuda para desplegar el proyecto me apoyaré de la documentación que viene en la sección de **Update Your App For Render** en la dirección `https://render.com/docs/deploy-django`.

Lo primero es ir a `PokemonAPI/restAPI/settings.py` e importar la libreria **os** y cambiar el **SECRET_KEY'**:

<p align="center">
<img src="/ghImg/img35.png">
</p>

luego nos pide cambiar el modo de DEBUG de **True** a `'RENDER' not in os.environ`:

<p align="center">
<img src="/ghImg/img36.png">
</p>

después debajo de ALLOWED_HOSTS nos pide escribir lo siguiente:

```
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
```

<p align="center">
<img src="/ghImg/img37.png">
</p>

en la terminal instalamos `dj-database-url psycopg2-binary` con el comando **pip install**:

<p align="center">
<img src="/ghImg/img40.png">
</p>

e importamos el modulo `dj-database-url` en el archivo _settings.py_:

<p align="center">
<img src="/ghImg/img41.png">
</p>

y lo asignamos a DATABASES de la siguiente forma:

<p align="center">
<img src="/ghImg/img42.png">
</p>

El siguiente paso es instalar `'whitenoise[brotli]'` con el comando **pip install**:

<p align="center">
<img src="/ghImg/img43.png">
</p>

Añadimos en MIDDLEWARE `'whitenoise.middleware.WhiteNoiseMiddleware',` como se muestra:

<p align="center">
<img src="/ghImg/img44.png">
</p>

Debajo de STATIC_URL pegamos lo siguiente:

```
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

<p align="center">
<img src="/ghImg/img45.png">
</p>

Antes de continuar, vamos a crear un archivo requirements.txt. En la terminal escribimos `pip freeze > requirements.txt`

<p align="center">
<img src="/ghImg/img46.png">
</p>

Nos pide crear un **Build Script**, haci que creamos un nuevo archivo llamado _build.sh_ y dentro de este archivo debe ir:

```
#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
```

<p align="center">
<img src="/ghImg/img47.png">
</p>

Este archivo **build.sh** debe tener permisos de ejecutable, así que abrimos el **Git Bash** dando click en la pestaña 

<p align="center">
<img src="/ghImg/img48.png">
</p>

Y escribimos `chmod a+x build.sh` en la consola y damos enter:

<p align="center">
<img src="/ghImg/img49.png">
</p>

Como vamos a correr la aplicación con **Gunicorn**, debemos añadir esta dependencia al poyecto. Escribimos `pip install gunicorn` en la termial y despues damos enter. 

Tambien debemos actualizar el archivo **requirements.txt**, asi que escribimos `pip freeze > requirements.txt` en la termial y despues damos enter.

Escribimos `git status` y damos enter. Tambien `git add .` y damos enter. Hacemos un comit, escribimos `git commit -m "configuración de Django lista"` y damos enter. Por último `git push -u origin main` y damos enter.

## **9) Desplegar en Render **

Nos dirigimos a la página de render: `https://render.com/` y nos creamos una cuenta, es gratis y no pide tarjeta de credito. 

Ahora debemos crear una base de datos en PostgreSQL, así que nos dirigimos a `https://dashboard.render.com/` y damos click para crear la base de datos:

<p align="center">
<img src="/ghImg/img38.png">
</p>

Ingresamos los datos correspondientes como se muestra, seleccionamos el plan gratuito, damos click en **Create Databse** y esperamos a que termine de crearlo:

<p align="center">
<img src="/ghImg/img39.png">
</p>

Cremos un nuevo proyecto, asi que vamos a `https://render.com/` y damos click en **New** y después en **Web Service**: 

<p align="center">
<img src="/ghImg/img50.png">
</p>

Damos click en nuestra cuenta:

<p align="center">
<img src="/ghImg/img51.png">
</p>

Y seleccionamos el repositorio que le queremos dar acceso a Render y damos click a **Save**:

<p align="center">
<img src="/ghImg/img52.png">
</p>

esto nos redirecciona a Render y le damos click en **Connect**:

<p align="center">
<img src="/ghImg/img53.png">
</p>

Se nos pedirán unos datos. 

En el campo de `Name:` ponemos el nombre del proyecto, en este caso **_PokemonAPI_**. 

En el campo de `Environment:` ponemos **_Python 3_**. 

En el campo de `Build Command:` ponemos **_./build.sh_**. 

En el campo de `Start Command:` ponemos **_gunicorn restAPI.wsgi_**. Seleccionamos el plan gratuito. Después damos click al botón **Advanced** para crear nuestras variables de entorno. Damos click derecho a **Dashboard** y así tendremos dos ventanas para copiar las variables que necesitamos.

<p align="center">
<img src="/ghImg/img54.png">
</p>

Damos click a **PokemonAPI**:

<p align="center">
<img src="/ghImg/img55.png">
</p>

Y copiamos de la seccion de **Connections** la **Internal Database URL** 

<p align="center">
<img src="/ghImg/img56.png">
</p>

La pegamos donde se muestra y le damos el nombre de **DATABASE_URL.**

<p align="center">
<img src="/ghImg/img57.png">
</p>

Damos click en **Add Environment Variable** y creamos la variable **SECRET_KEY**, esta variable es una clave aleatoria que podemos crear usando por ejemplo `https://www.allkeysgenerator.com/Random/Security-Encryption-Key-Generator.aspx`: 

<p align="center">
<img src="/ghImg/img58.png">
</p>

Damos click en **Add Environment Variable** y creamos la variable **PYTHON_VERSION**, esta variable es la version que estamos usando de python. La obtenemos desde la terminal con `python --version`:

<p align="center">
<img src="/ghImg/img59.png">
</p>

Y por útimo damos click en **Create Web Service**. Pero esto me botó un error en el despliegue:

<p align="center">
<img src="/ghImg/img60.png">
</p>

,debido a que en mi archivo **build.sh** tenia escrito:

```
poetry install -r requirements.txt
```

y debe de ser:

```
pip install -r requirements.txt
```

damos click en **Deploy** y esperamos a que termine.

<p align="center">
<img src="/ghImg/img61.png">
</p>

Una ves terminado, si todo ha salido bien se verá así:

<p align="center">
<img src="/ghImg/img62.png">
</p>

Para probar por ejemplo con el pokemon **electabuzz**, nos vamos a la dirección: `https://pokemonapi-wild.onrender.com/api/pokemon/electabuzz` y obtenemos:

<p align="center">
<img src="/ghImg/img63.png">
</p>



