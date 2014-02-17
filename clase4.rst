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
    


Introducci�n
------------

En el curso anterior implementamos un sencillo proyecto usando el framework Django, con el cual pudimos explorar
las caracter�sticas m�s b�sicas del framework: modelos, plantillas, vistas y la interfaz administrativa de Django.
En esta oportunidad estudiaremos m�s profundamente cada una de estas caracter�sticas, y expondremos con m�s detalle
el funcionamiento interno del framework.

    
Vistas basadas en clase
-----------------------

Hasta ahora hemos definido las vistas como funciones que reciben un objeto *HttpRequest* y retornan un *HttpResponse*.
�sta, sin embargo, no es la �nica manera de definir vistas. Una manera alternativa de manejar las vistas es 
trat�ndolas como objetos, para esto utilizamos *Vistas basadas en clases*. Esta forma de definir vistas provee una
serie de ventajas

* Mejor organizaci�n del c�digo referente a los diferentes m�todos HTTP (GET, POST, etc)
* Uso de Programaci�n Orientada a Objetos para estructurar y jerarquizar las vistas
* Uso de *vistas gen�ricas* definidas por el framework

Para definir el comportamiento de una vista en caso de recibir una solicitud de tipo ``GET``, utilizando funciones,
lo har�amos de la siguiente forma:

.. code-block:: python

    from django.http import HttpResponse

    def mi_vista(request):
        if request.method == 'GET':
            # l�gica de la vista
            return HttpResponse('result')


En el caso de las vistas basadas en clases, se define un m�todo ``get`` dentro de la clase, que maneje la solicitud:

.. code-block:: python

from django.http import HttpResponse
from django.views.generic.base import View

    class MiVista(View):
        def get(self, request):
            # l�gica de la vista
            return HttpResponse('result')


Una vista basada en clase act�a de la misma forma que una vista normal, con la particularidad de que permite una mejor
manera de organizaci�n.

Para 


Managers
--------
            
Sistema de plantillas
---------------------

Formularios
-----------

Se�ales
-------


   

