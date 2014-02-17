.. Taller de Python documentation master file, created by
   sphinx-quickstart on Mon Jan 27 16:38:42 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

	
.. image:: _static/logo_posma.png
   :align: center
   
==========================
Django Framework: Parte II
==========================

.. contents:: Contenido
	:depth: 2
    


Introducción
------------

En el curso anterior implementamos un sencillo proyecto usando el framework Django, con el cual pudimos explorar
las características más básicas del framework: modelos, plantillas, vistas y la interfaz administrativa de Django.
En esta oportunidad estudiaremos más profundamente cada una de estas características, y expondremos con más detalle
el funcionamiento interno del framework.

    
Vistas basadas en clase
-----------------------

Hasta ahora hemos definido las vistas como funciones que reciben un objeto *HttpRequest* y retornan un *HttpResponse*.
Ésta, sin embargo, no es la única manera de definir vistas. Una manera alternativa de manejar las vistas es 
tratándolas como objetos, para esto utilizamos *Vistas basadas en clases*. Esta forma de definir vistas provee una
serie de ventajas

* Mejor organización del código referente a los diferentes métodos HTTP (GET, POST, etc)
* Uso de Programación Orientada a Objetos para estructurar y jerarquizar las vistas
* Uso de *vistas genéricas* definidas por el framework

Para definir el comportamiento de una vista en caso de recibir una solicitud de tipo ``GET``, utilizando funciones,
lo haríamos de la siguiente forma:

.. code-block:: python

    from django.http import HttpResponse

    def mi_vista(request):
        if request.method == 'GET':
            # lógica de la vista
            return HttpResponse('result')


En el caso de las vistas basadas en clases, se define un método ``get`` dentro de la clase, que maneje la solicitud:

.. code-block:: python

from django.http import HttpResponse
from django.views.generic.base import View

    class MiVista(View):
        def get(self, request):
            # lógica de la vista
            return HttpResponse('result')


Una vista basada en clase actúa de la misma forma que una vista normal, con la particularidad de que permite una mejor
manera de organización.

Para 


Managers
--------
            
Sistema de plantillas
---------------------

Formularios
-----------

Señales
-------


   

