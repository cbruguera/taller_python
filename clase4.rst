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

Ahora bien, para que Django pueda resolver los URLs, cada uno debe corresponder con una vista, y el framework está 
esperando una función, no una clase. Para esto la clase ``View`` implementa el método ``as_view``:

.. code-block:: python

    # urls.py
    from django.conf.urls import patterns
    from myapp.views import MyView

    urlpatterns = patterns('',
        (r'^ayuda/', AyudaView.as_view()),
    )


El método ``as_view`` también puede recibir cualquier cantidad de argumentos. Éstos sobreescribirán cualquier 
atributo declarado en la clase de dicha vista.


Vistas genéricas
~~~~~~~~~~~~~~~~

Una de las principales ventajas de utilizar clases para definir las vistas, es que tenemos acceso a un considerable 
número de *vistas genéricas*, definidas por defecto en el framework para satisfacer los casos de uso más comunes para 
comportamiento de vistas. Por ejemplo, Django incorpora las siguientes vistas básicas:


View
....

``View`` Es la clase padre de todas las demás vistas genéricas. Lo primero que esta vista hace al ser invocada, es 
llamar al método ``dispatch()``, el cual se encarga de invocar al método apropiado dependiendo del tipo de solicitud 
HTTP (GET, POST, HEAD, etc). En caso de recibir una solicitud de un tipo no soportado, invoca a 
``http_method_not_allowed()``. Todos estos métodos, vale recordar, pueden ser sobrescritos en las clases hijas. 
Sin embargo, no es recomendado hacer esto a menos que se tenga conocimiento concreto de lo que se desea hacer.


TemplateView
............

Esta vista retorna un *render* de una plantilla en particular. Bastante útil cuando lo único que se requiere es 
mostrar un template. Un ``TemplateView`` se define de la siguiente manera:

.. code-block:: python

    from django.views.generic.base import TemplateView


    class HomePageView(TemplateView):

        template_name = "home.html"
        

La implementación de la clase se encargará de retornar el objeto ``HttpResponse`` adecuado con la renderización de la 
plantilla respectiva. Como podemos ver, el uso de esta vista genérica nos ahorra trabajo y ayuda a la legibilidad y 
organización del código.

El orden de procesamiento de ``TemplateView`` es el siguiente:

1) Se invoca ``dispatch()``
2) ``http_method_not_allowed()`` en caso de no soportar el tipo de solicitud.
3) Se invoca ``get_context_data()``.

El método ``get_context_data`` se encarga de preparar el *contexto* para la plantilla destino. Este contexto no es 
más que un diccionario de datos que es accesible desde el template. Ésta es la manera de pasar información de las 
vistas a las plantillas. Si queremos que nuestro ``TemplateView`` procese o agregue ciertos datos específicos al 
contexto de la plantilla, debemos sobrescribir el método:

.. code-block:: python

    from django.views.generic.base import TemplateView

    from articles.models import Article

    class HomePageView(TemplateView):

        template_name = "home.html"

        def get_context_data(self, **kwargs):
            context = super(HomePageView, self).get_context_data(**kwargs)
            context['latest_articles'] = Article.objects.all()[:5]
            return context
            

RedirectView
............

DetailView
..........

ListView
........

CreateView

UpdateView

DeleteView

Managers
--------
            
Sistema de plantillas
---------------------

Formularios
-----------

Señales
-------


   

