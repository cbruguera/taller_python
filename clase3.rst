.. Taller de Python documentation master file, created by
   sphinx-quickstart on Mon Jan 27 16:38:42 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

	
.. image:: _static/logo_posma.png
   :align: center
   
========================
Python: Django Framework
========================

.. contents:: Contenido
   :depth: 2

   
Introducción
------------

En los talleres anteriores hemos expuesto las bases de la programación en Python. Sin embargo, es nuestro objetivo
adquirir suficiente conocimiento para desarrollar proyectos de aplicación web, para ello exploraremos de manera 
práctica las herramientas que nos provee el framework *Django*.


Preparando un ambiente de desarrollo
------------------------------------

Lo primero que haremos será crear un directorio dedicado al proyecto en el que vamos a trabajar.

.. code-block:: bash

    $ mkdir mi_proyecto
    $ cd mi_proyecto


Para comenzar a implementar cualquier proyecto, bien sea éste de naturaleza web o no, es necesario preparar un
entorno de trabajo que nos provea las herramientas necesarias, facilitándonos el desarrollo de manera ordenada y sin
conflictos con otros proyectos existentes. 

Para este fin, utilizaremos *virtualenv*.


virtualenv
~~~~~~~~~~

Virtualenv es una herramienta que nos permite definir entornos aislados para cada uno de nuestros proyectos Python.
Esto es de gran utilidad, ya que hace posible que en una misma máquina convivan diversos proyectos con versiones 
distintas de python, y con un espacio aislado para cada conjunto de bibliotecas externas.


Instalación
...........

Para saber si virtualenv está ya instalado en el sistema, ejecutamos la siguiente instrucción:

.. code-block:: bash

    $ virtualenv --version


Si no está instalado, en Debian puede hacerse de la siguiente forma:

.. code-block:: bash

    $ sudo apt-get install python-virtualenv


Una vez que está instalado, ya podemos crear un entorno virtual:

.. code-block:: bash

    $ virtualenv env --no-site-packages


La opción ``--no-site-packages`` significa que el nuevo entorno virtual no instalará los paquetes que se encuentran
instalados globalmente. Esto nos permite iniciar el entorno de manera limpia, e ir instalando sólo lo que sea
necesario.

Luego entramos al subdirectorio ``bin``, y activamos el entorno.

.. code-block:: bash

    $ cd env/bin
    $ source activate
    (env) $


Notaremos que el nombre de nuestro entorno virtual (``env``) aparece entre paréntesis al comienzo de cada línea del 
intérprete de comandos. Esto indica que nos encontramos dentro de dicho entorno. Toda biblioteca Python que instalemos 
o actualicemos sólo afectará al entorno actual, que es específico para el proyecto en el que estamos trabajando. Para 
salir del entorno, ejecutamos la instrucción ``deactivate``.


pip
~~~

Una vez que estamos "dentro" del entorno virtual deseado, podemos instalar paquetes externos de Python. Para esto 
usaremos la herramienta *pip*. 

*Pip* es un manejador de paquetes para Python, que hace posible la instalación y actualización de bibliotecas 
fácilmente desde la línea de comandos.

Para comenzar, instalaremos Django, que es el framework que vamos a utilizar.
	
.. code-block:: bash

    $ pip install django


Esto descarga e instala los paquetes necesarios para el funcionamiento del framework Django. Si queremos ver una lista 
de las bibliotecas instaladas en el entorno actual, ejecutamos:

.. code-block:: bash
	
    $ pip freeze


Si la instalación de Django se ha hecho correctamente, podemos importarlo desde el intérprete. Hagamos la siguiente 
prueba:

.. code-block:: python

    >>> import django
    >>> print(django.get_version())
    1.6


Ya estamos listos para comenzar a usar Django.
	

Django Framework
----------------

Python es un lenguaje conocido por tener "baterías incluidas", es decir, que no le hace falta nada para comenzar 
a trabajar con él. Sin embargo, existe una gran cantidad de herramientas externas y *frameworks* para el desarrollo
web. *Django* es uno de los frameworks más populares hoy en día, por ser bastante completo. Además, está 
diseñado para permitir el desarrollo de aplicaciones web de grandes dimensiones, en un tiempo relativamente corto.


¿Es Django un framework MVC?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En Django está claramente implementada la separación entre la lógica del negocio, la naturaleza de los datos y la 
manera en la que éstos se muestran. Algunos desarrolladores afirman que el framework cumple con el patrón MVC 
(*Model-View-Controller*), sin embargo, el diseño de Django implementa un patrón un poco distinto. El framework consta
principalmente de 3 capas:
 
* Modelos (models)
* Vistas (views)
* Plantillas (templates)

En los **Modelos** se define la fuente y la estructura de los datos que la aplicación maneja. Esta capa se implementa 
en la forma de un ORM (*Object Relational Mapping*), con el cual se simplifica de manera considerable el acceso a los
datos. 

En las **Vistas**, a pesar de lo que podría pensarse, no se define la manera en que los datos son mostrados al 
usuario, sino más bien cuáles son los datos a mostrar. Ésta es la capa que se comunica con los modelos del ORM 
de Django y entrega los datos al *template*.

Las **Plantillas** definen la interfaz última entre el usuario y el sistema. Es en los *templates* en donde se define
la forma en que se muestran los datos.

Podría considerarse que lo descrito anteriormente es una implementación particular de MVC, en donde los *templates* 
representan la vista, y los *views* corresponden a los controladores. Sin embargo, esto no es técnicamente correcto,
ya que el controlador de las solicitudes realmente está implícito en el framework en sí, y en el modelo es válido 
implementar parte de la lógica del negocio.

De cualquier forma, lo importante es facilitar el desarrollo sin importar las terminologías que mejor describan el 
framework. Si es necesario asociarle un nombre, podríamos decir que Django implementa el patrón *Model-Template-View*.

Adicionalmente, Django provee las siguientes funcionalidades:

* Clases para el manejo de formularios
* Autenticación
* Interfaz adminstrativa
* Internacionalización
* Cache

... Entre otras.


Creando un nuevo proyecto
~~~~~~~~~~~~~~~~~~~~~~~~~

Para crear un proyecto en django, ejecutamos el script ``django-admin.py`` con la opción ``startproject``, de la 
siguiente manera:

.. code-block:: bash

    $ django-admin.py startproject mi_sitio


Esto debió crear una carpeta ``mi_sitio`` dentro de la carpeta actual, con una serie de archivos necesarios para el
funcionamiento de Django.

**Nota:** Es importante evitar el uso de nombres que puedan generar conflictos con Python o los componentes de Django.
Por ejemplo, se recomienda no utilizar palabras como "django" o "test".


Servidor de desarrollo
~~~~~~~~~~~~~~~~~~~~~~

Por los momentos, prestaremos particular atención al archivo ``manage.py``, el cual sirve como interfaz con diversas 
opciones para el manejo del proyecto. Por ejemplo, podemos ejecutar ``manage.py`` con la opción ``runserver`` para 
iniciar el servidor de prueba.

.. code-block:: bash

    $ manage.py runserver
    Validating models...

    0 errors found
    February 10, 2014 - 16:54:57
    Django version 1.6.2, using settings 'mi_sitio.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.


Esto ha iniciado un servidor de desarrollo que viene incluido dentro de Django para poder probar fácilmente, sin 
necesidad de configurar un servidor de producción, como Apache.

Ahora podemos probar ingresar el URL ``http://127.0.0.1:8000/`` en algún navegador. Esto nos mostrará una página
de bienvenida de Django, indicando que la aplicación está ejecutándose exitosamente.

**Nota:** Es importante aclarar que el comando ``python manage.py runserver`` inicia un servidor *de prueba*. Bajo
ninguna circunstancia debe utilizarse para correr el proyecto en un ambiente de producción.


Configuración
~~~~~~~~~~~~~

En el archivo ``settings.py`` se encuentran definidos todos los parámetros de configuración del proyecto, como por
ejemplo las opciones de conexión a la base de datos.


Base de datos
.............

Los parámetros de configuración de la base de datos los define la varible global ``DATABASES``. La configuración por 
defecto luce de esta manera:

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


Por defecto, Django utiliza *SQLite*, que es una base de datos ligera (la BD completa se almacena en un archivo). Para
utilizar algún otro manejador de base de datos, hay que cambiar el parámetro ``ENGINE``. Las opciones inicialmente 
soportadas por el framework son:

* ``'django.db.backends.postgresql_psycopg2'``
* ``'django.db.backends.mysql'``
* ``'django.db.backends.sqlite3'``
* ``'django.db.backends.oracle'``

Sin embargo, es posible implementar o instalar otros motores de conexión a base de datos.

En el parámetro ``NAME`` se especifica el nombre de la base de datos. En el caso de SQLite, esto corresponde al nombre
del archivo en disco duro, con la ruta completa en el sistema de archivos.

Si se está utilizando un motor de base de datos distinto de SQLite, es necesario definir los parámetros ``USER``, 
``PASSWORD`` y ``HOST``. Además, es necesario crear la base de datos previamente a esta configuración.


Zona horaria
............

Para especificar la zona horaria en la que habita nuestra aplicación, configuramos el parámetro ``TIME_ZONE``.
En el caso de Venezuela, el valor correcto es ``'America/Caracas'``.


Aplicaciones
............

Otra parte fundamental de la configuración es la variable ``INSTALLED_APPS``. En esta tupla están definidas todas las
aplicaciones con las que podrá interactuar el framework. Por defecto vienen instaladas las aplicaciones básicas como 
``django.contrib.admin`` y ``django.contrib.auth``, para el manejo de la interfaz administrativa y el sistema de 
autenticación respectivamente. A medida que vayamos creando aplicaciones dentro de nuestro proyecto, o instalando
bibliotecas de terceros, deben agregarse en esta sección como aplicaciones instaladas.


Iniciando la base de datos
..........................

A continuación, ejecutaremos la siguiente instrucción:

.. code-block:: bash

    $ python manage.py syncdb


La instrucción ``syncdb`` recorre ``INSTALLED_APPS`` y crea la tablas necesarias en la base de datos, de acuerdo a los
parámetros de configuración establecidos en el archivo ``settings.py``.

La primera vez que se ejecuta, el sistema preguntará al usuario si desea crear un usuario con permisos 
administrativos. Es recomendable hacerlo.

Una vez realizados los pasos anteriores, el proyecto está creado y debidamente configurado para iniciar su desarrollo.

Para explorar la base de datos SQLite, podemos utilizar `SQLite Manager`_.

.. _SQLite Manager: https://addons.mozilla.org/es/firefox/addon/sqlite-manager/


Aplicaciones
~~~~~~~~~~~~

Un proyecto en Django consta de un conjunto de aplicaciones, éstas no son más que paquetes de Python que siguen una
convención determinada.

Para crear una aplicación, ejecutamos la instrucción ``startapp``:

.. code-block:: bash

    $ python manage.py startapp encuestas


Esto creará un directorio "encuestas", con la siguiente estructura:

.. code-block:: bash

    encuestas/
        __init__.py
        admin.py
        models.py
        tests.py
        views.py


Vistas
~~~~~~

Para comenzar, implementaremos una vista de prueba. Para esto editaremos el archivo ``views.py`` e insertaremos 
el siguiente código:

.. code-block:: python

    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Hola mundo")


Modelos
~~~~~~~

Lo primero que haremos con nuestra aplicación será definir los modelos. Para esto editaremos el archivo ``models.py``
y copiaremos el siguiente código:

.. code-block:: python

    from django.db import models

    class Encuesta(models.Model):
        pregunta = models.CharField(max_length=200)
        fecha_pub = models.DateTimeField('Fecha de publicacion')

    class Opcion(models.Model):
        encuesta = models.ForeignKey(Encuesta)
        texto = models.CharField(max_length=200)
        votos = models.IntegerField(default=0)


Cada modelo se define como una clase que hereda de ``django.db.models.Model``, definiendo a su vez una serie de 
atributos de clase. Cada uno de estos atributos representa un campo en la base de datos.

Cada campo es una instancia de la clase ``django.db.models.Field``, cuyas subclases implementan los distintos tipos
de datos. En el ejemplo podemos ver el uso de ``CharField`` para cadenas de texto, ``IntegerField`` para números 
enteros, ``DateTimeField`` para fechas con horas, y ``ForeignKey`` para relaciones directas con otros modelos.

Un ``ForeignKey`` puede verse como una relación "muchos a uno", ya que distintos modelos pueden definir la misma 
*llave foránea* con un modelo dado.

El siguiente paso es agregar nuestra aplicación ``encuestas`` a la lista de aplicaciones intaladas en el 
``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'encuestas',
    )


Ahora necesitamos sincronizar la base de datos con la instrucción ``syncdb``, para que Django cree las tablas y los
campos correspondientes a nuestro modelo.

.. code-block:: bash

    $ python manage.py syncdb


Es necesario ejecutar esta instrucción cada vez que hacemos cambios en el modelo, ``syncdb`` sólo hará los cambios 
necesarios en la base de datos, sin perder los datos ya almacenados. 





.. Fuentes
.. ~~~~~~~

.. * http://www.djangoproject.com (sitio oficial)
.. * http://effectivedjango.com/ (guía detallada)

