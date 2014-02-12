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

   
Introducci�n
------------

En los talleres anteriores hemos expuesto las bases de la programaci�n en Python. Sin embargo, es nuestro objetivo
adquirir suficiente conocimiento para desarrollar proyectos de aplicaci�n web, para ello exploraremos de manera 
pr�ctica las herramientas que nos provee el framework *Django*.


Preparando un ambiente de desarrollo
------------------------------------

Lo primero que haremos ser� crear un directorio dedicado al proyecto en el que vamos a trabajar.

.. code-block:: bash

    $ mkdir mi_proyecto
    $ cd mi_proyecto


Para comenzar a implementar cualquier proyecto, bien sea �ste de naturaleza web o no, es necesario preparar un
entorno de trabajo que nos provea las herramientas necesarias, facilit�ndonos el desarrollo de manera ordenada y sin
conflictos con otros proyectos existentes. 

Para este fin, utilizaremos *virtualenv*.


virtualenv
~~~~~~~~~~

Virtualenv es una herramienta que nos permite definir entornos aislados para cada uno de nuestros proyectos Python.
Esto es de gran utilidad, ya que hace posible que en una misma m�quina convivan diversos proyectos con versiones 
distintas de python, y con un espacio aislado para cada conjunto de bibliotecas externas.


Instalaci�n
...........

Para saber si virtualenv est� ya instalado en el sistema, ejecutamos la siguiente instrucci�n:

.. code-block:: bash

    $ virtualenv --version


Si no est� instalado, en Debian puede hacerse de la siguiente forma:

.. code-block:: bash

    $ sudo apt-get install python-virtualenv


Una vez que est� instalado, ya podemos crear un entorno virtual:

.. code-block:: bash

    $ virtualenv env --no-site-packages


La opci�n ``--no-site-packages`` significa que el nuevo entorno virtual no instalar� los paquetes que se encuentran
instalados globalmente. Esto nos permite iniciar el entorno de manera limpia, e ir instalando s�lo lo que sea
necesario.

Luego entramos al subdirectorio ``bin``, y activamos el entorno.

.. code-block:: bash

    $ cd env/bin
    $ source activate
    (env) $


Notaremos que el nombre de nuestro entorno virtual (``env``) aparece entre par�ntesis al comienzo de cada l�nea del 
int�rprete de comandos. Esto indica que nos encontramos dentro de dicho entorno. Toda biblioteca Python que instalemos 
o actualicemos s�lo afectar� al entorno actual, que es espec�fico para el proyecto en el que estamos trabajando. Para 
salir del entorno, ejecutamos la instrucci�n ``deactivate``.


pip
~~~

Una vez que estamos "dentro" del entorno virtual deseado, podemos instalar paquetes externos de Python. Para esto 
usaremos la herramienta *pip*. 

*Pip* es un manejador de paquetes para Python, que hace posible la instalaci�n y actualizaci�n de bibliotecas 
f�cilmente desde la l�nea de comandos.

Para comenzar, instalaremos Django, que es el framework que vamos a utilizar.
	
.. code-block:: bash

    $ pip install django


Esto descarga e instala los paquetes necesarios para el funcionamiento del framework Django. Si queremos ver una lista 
de las bibliotecas instaladas en el entorno actual, ejecutamos:

.. code-block:: bash
	
    $ pip freeze


Si la instalaci�n de Django se ha hecho correctamente, podemos importarlo desde el int�rprete. Hagamos la siguiente 
prueba:

.. code-block:: python

    >>> import django
    >>> print(django.get_version())
    1.6


Ya estamos listos para comenzar a usar Django.
	

Django Framework
----------------

Python es un lenguaje conocido por tener "bater�as incluidas", es decir, que no le hace falta nada para comenzar 
a trabajar con �l. Sin embargo, existe una gran cantidad de herramientas externas y *frameworks* para el desarrollo
web. *Django* es uno de los frameworks m�s populares hoy en d�a, por ser bastante completo. Adem�s, est� 
dise�ado para permitir el desarrollo de aplicaciones web de grandes dimensiones, en un tiempo relativamente corto.


�Es Django un framework MVC?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En Django est� claramente implementada la separaci�n entre la l�gica del negocio, la naturaleza de los datos y la 
manera en la que �stos se muestran. Algunos desarrolladores afirman que el framework cumple con el patr�n MVC 
(*Model-View-Controller*), sin embargo, el dise�o de Django implementa un patr�n un poco distinto. El framework consta
principalmente de 3 capas:
 
* Modelos (models)
* Vistas (views)
* Plantillas (templates)

En los **Modelos** se define la fuente y la estructura de los datos que la aplicaci�n maneja. Esta capa se implementa 
en la forma de un ORM (*Object Relational Mapping*), con el cual se simplifica de manera considerable el acceso a los
datos. 

En las **Vistas**, a pesar de lo que podr�a pensarse, no se define la manera en que los datos son mostrados al 
usuario, sino m�s bien cu�les son los datos a mostrar. �sta es la capa que se comunica con los modelos del ORM 
de Django y entrega los datos al *template*.

Las **Plantillas** definen la interfaz �ltima entre el usuario y el sistema. Es en los *templates* en donde se define
la forma en que se muestran los datos.

Podr�a considerarse que lo descrito anteriormente es una implementaci�n particular de MVC, en donde los *templates* 
representan la vista, y los *views* corresponden a los controladores. Sin embargo, esto no es t�cnicamente correcto,
ya que el controlador de las solicitudes realmente est� impl�cito en el framework en s�, y en el modelo es v�lido 
implementar parte de la l�gica del negocio.

De cualquier forma, lo importante es facilitar el desarrollo sin importar las terminolog�as que mejor describan el 
framework. Si es necesario asociarle un nombre, podr�amos decir que Django implementa el patr�n *Model-Template-View*.

Adicionalmente, Django provee las siguientes funcionalidades:

* Clases para el manejo de formularios
* Autenticaci�n
* Interfaz adminstrativa
* Internacionalizaci�n
* Cache

... Entre otras.


Creando un nuevo proyecto
~~~~~~~~~~~~~~~~~~~~~~~~~

Para crear un proyecto en django, ejecutamos el script ``django-admin.py`` con la opci�n ``startproject``, de la 
siguiente manera:

.. code-block:: bash

    $ django-admin.py startproject mi_sitio


Esto debi� crear una carpeta ``mi_sitio`` dentro de la carpeta actual, con una serie de archivos necesarios para el
funcionamiento de Django.

**Nota:** Es importante evitar el uso de nombres que puedan generar conflictos con Python o los componentes de Django.
Por ejemplo, se recomienda no utilizar palabras como "django" o "test".


Servidor de desarrollo
~~~~~~~~~~~~~~~~~~~~~~

Por los momentos, prestaremos particular atenci�n al archivo ``manage.py``, el cual sirve como interfaz con diversas 
opciones para el manejo del proyecto. Por ejemplo, podemos ejecutar ``manage.py`` con la opci�n ``runserver`` para 
iniciar el servidor de prueba.

.. code-block:: bash

    $ manage.py runserver
    Validating models...

    0 errors found
    February 10, 2014 - 16:54:57
    Django version 1.6.2, using settings 'mi_sitio.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.


Esto ha iniciado un servidor de desarrollo que viene incluido dentro de Django para poder probar f�cilmente, sin 
necesidad de configurar un servidor de producci�n, como Apache.

Ahora podemos probar ingresar el URL ``http://127.0.0.1:8000/`` en alg�n navegador. Esto nos mostrar� una p�gina
de bienvenida de Django, indicando que la aplicaci�n est� ejecut�ndose exitosamente.

**Nota:** Es importante aclarar que el comando ``python manage.py runserver`` inicia un servidor *de prueba*. Bajo
ninguna circunstancia debe utilizarse para correr el proyecto en un ambiente de producci�n.


Configuraci�n
~~~~~~~~~~~~~

En el archivo ``settings.py`` se encuentran definidos todos los par�metros de configuraci�n del proyecto, como por
ejemplo las opciones de conexi�n a la base de datos.


Base de datos
.............

Los par�metros de configuraci�n de la base de datos los define la varible global ``DATABASES``. La configuraci�n por 
defecto luce de esta manera:

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


Por defecto, Django utiliza *SQLite*, que es una base de datos ligera (la BD completa se almacena en un archivo). Para
utilizar alg�n otro manejador de base de datos, hay que cambiar el par�metro ``ENGINE``. Las opciones inicialmente 
soportadas por el framework son:

* ``'django.db.backends.postgresql_psycopg2'``
* ``'django.db.backends.mysql'``
* ``'django.db.backends.sqlite3'``
* ``'django.db.backends.oracle'``

Sin embargo, es posible implementar o instalar otros motores de conexi�n a base de datos.

En el par�metro ``NAME`` se especifica el nombre de la base de datos. En el caso de SQLite, esto corresponde al nombre
del archivo en disco duro, con la ruta completa en el sistema de archivos.

Si se est� utilizando un motor de base de datos distinto de SQLite, es necesario definir los par�metros ``USER``, 
``PASSWORD`` y ``HOST``. Adem�s, es necesario crear la base de datos previamente a esta configuraci�n.


Zona horaria
............

Para especificar la zona horaria en la que habita nuestra aplicaci�n, configuramos el par�metro ``TIME_ZONE``.
En el caso de Venezuela, el valor correcto es ``'America/Caracas'``.


Aplicaciones
............

Otra parte fundamental de la configuraci�n es la variable ``INSTALLED_APPS``. En esta tupla est�n definidas todas las
aplicaciones con las que podr� interactuar el framework. Por defecto vienen instaladas las aplicaciones b�sicas como 
``django.contrib.admin`` y ``django.contrib.auth``, para el manejo de la interfaz administrativa y el sistema de 
autenticaci�n respectivamente. A medida que vayamos creando aplicaciones dentro de nuestro proyecto, o instalando
bibliotecas de terceros, deben agregarse en esta secci�n como aplicaciones instaladas.


Iniciando la base de datos
..........................

A continuaci�n, ejecutaremos la siguiente instrucci�n:

.. code-block:: bash

    $ python manage.py syncdb


La instrucci�n ``syncdb`` recorre ``INSTALLED_APPS`` y crea la tablas necesarias en la base de datos, de acuerdo a los
par�metros de configuraci�n establecidos en el archivo ``settings.py``.

La primera vez que se ejecuta, el sistema preguntar� al usuario si desea crear un usuario con permisos 
administrativos. Es recomendable hacerlo.

Una vez realizados los pasos anteriores, el proyecto est� creado y debidamente configurado para iniciar su desarrollo.

Para explorar la base de datos SQLite, podemos utilizar `SQLite Manager`_.

.. _SQLite Manager: https://addons.mozilla.org/es/firefox/addon/sqlite-manager/


Aplicaciones
~~~~~~~~~~~~

Un proyecto en Django consta de un conjunto de aplicaciones, �stas no son m�s que paquetes de Python que siguen una
convenci�n determinada.

Para crear una aplicaci�n, ejecutamos la instrucci�n ``startapp``:

.. code-block:: bash

    $ python manage.py startapp encuestas


Esto crear� un directorio "encuestas", con la siguiente estructura:

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
el siguiente c�digo:

.. code-block:: python

    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Hola mundo")


Modelos
~~~~~~~

Lo primero que haremos con nuestra aplicaci�n ser� definir los modelos. Para esto editaremos el archivo ``models.py``
y copiaremos el siguiente c�digo:

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
de datos. En el ejemplo podemos ver el uso de ``CharField`` para cadenas de texto, ``IntegerField`` para n�meros 
enteros, ``DateTimeField`` para fechas con horas, y ``ForeignKey`` para relaciones directas con otros modelos.

Un ``ForeignKey`` puede verse como una relaci�n "muchos a uno", ya que distintos modelos pueden definir la misma 
*llave for�nea* con un modelo dado.

El siguiente paso es agregar nuestra aplicaci�n ``encuestas`` a la lista de aplicaciones intaladas en el 
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


Ahora necesitamos sincronizar la base de datos con la instrucci�n ``syncdb``, para que Django cree las tablas y los
campos correspondientes a nuestro modelo.

.. code-block:: bash

    $ python manage.py syncdb


Es necesario ejecutar esta instrucci�n cada vez que hacemos cambios en el modelo, ``syncdb`` s�lo har� los cambios 
necesarios en la base de datos, sin perder los datos ya almacenados. 





.. Fuentes
.. ~~~~~~~

.. * http://www.djangoproject.com (sitio oficial)
.. * http://effectivedjango.com/ (gu�a detallada)

