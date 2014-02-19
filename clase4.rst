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

Ahora bien, para que Django pueda resolver los URLs, cada uno debe corresponder con una vista, y el framework est� 
esperando una funci�n, no una clase. Para esto la clase ``View`` implementa el m�todo ``as_view``:

.. code-block:: python

    # urls.py
    from django.conf.urls import patterns
    from myapp.views import MyView

    urlpatterns = patterns('',
        (r'^ayuda/', AyudaView.as_view()),
    )


El m�todo ``as_view`` tambi�n puede recibir cualquier cantidad de argumentos. �stos sobreescribir�n cualquier 
atributo declarado en la clase de dicha vista.


Vistas gen�ricas
~~~~~~~~~~~~~~~~

Una de las principales ventajas de utilizar clases para definir las vistas, es que tenemos acceso a un considerable 
n�mero de *vistas gen�ricas*, definidas por defecto en el framework para satisfacer los casos de uso m�s comunes para 
comportamiento de vistas. Por ejemplo, Django incorpora las siguientes vistas b�sicas:


View
....

``View`` Es la clase padre de todas las dem�s vistas gen�ricas. Lo primero que esta vista hace al ser invocada, es 
llamar al m�todo ``dispatch()``, el cual se encarga de invocar al m�todo apropiado dependiendo del tipo de solicitud 
HTTP (GET, POST, HEAD, etc). En caso de recibir una solicitud de un tipo no soportado, invoca a 
``http_method_not_allowed()``. Todos estos m�todos, vale recordar, pueden ser sobrescritos en las clases hijas. 
Sin embargo, no es recomendado hacer esto a menos que se tenga conocimiento concreto de lo que se desea hacer.


TemplateView
............

Esta vista retorna un *render* de una plantilla en particular. Bastante �til cuando lo �nico que se requiere es 
mostrar un template. Un ``TemplateView`` se define de la siguiente manera:

.. code-block:: python

    from django.views.generic.base import TemplateView


    class HomePageView(TemplateView):

        template_name = "home.html"
        

La implementaci�n de la clase se encargar� de retornar el objeto ``HttpResponse`` adecuado con la renderizaci�n de la 
plantilla respectiva. Como podemos ver, el uso de esta vista gen�rica nos ahorra trabajo y ayuda a la legibilidad y 
organizaci�n del c�digo.

El orden de procesamiento de ``TemplateView`` es el siguiente:

1) Se invoca ``dispatch()``
2) ``http_method_not_allowed()`` en caso de no soportar el tipo de solicitud.
3) Se invoca ``get_context_data()``.

El m�todo ``get_context_data`` se encarga de preparar el *contexto* para la plantilla destino. Este contexto no es 
m�s que un diccionario de datos que es accesible desde el template. �sta es la manera de pasar informaci�n de las 
vistas a las plantillas. Si queremos que nuestro ``TemplateView`` procese o agregue ciertos datos espec�ficos al 
contexto de la plantilla, debemos sobrescribir el m�todo:

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

``RedirectView``, como su nombre lo indica, simplemente efect�a una redirecci�n a un URL dado.

Ejemplo:

.. code-block:: python

    from django.views.generic.base import RedirectView
    
    class GoogleRedirectView(RedirectView):
        
        url = "https://www.google.com/"


Sin embargo, no es necesario implementar una subclase de ``RedirectView`` si no es necesario, tambi�n podemos 
utilizar directamente la clase desde el archivo de URLs de la siguiente manera:

.. code-block:: python

    from django.conf.urls import patterns, url
    from django.views.generic.base import RedirectView


    urlpatterns = patterns('',

        url(r'^django-doc/$', RedirectView.as_view(url='http://djangoproject.com')),
    )


El flujo de ejecuci�n de ``RedirectView`` ocurre de la siguiente forma:

1) ``dispatch()``
2) ``http_method_not_allowed()``
3) ``get_redirect_url()``

El m�todo ``get_redirect_url`` es el que construye el URL destino de la redirecci�n. Si la construcci�n de este URL 
requiere de alg�n tipo de procesamiento, se necesita sobrescribir el m�todo:

.. code-block:: python

    from django.shortcuts import get_object_or_404
    from django.views.generic.base import RedirectView

    from libros.models import Libro

    class GoogleBookInfoRedirectView(RedirectView):
        
        url = "https://www.google.com/search"
        query_string = True
        
        def get_redirect_url(self, *args, **kwargs):
            libro = get_object_or_404(Libro, pk=int(kwargs['pk']))
            print "titulo = %s" % libro.titulo
            return super(GoogleBookInfoRedirectView, self).get_redirect_url(url="%s?q=%s" % (url, libro.titulo), 
                    *args, **kwargs)

.. hay un error con este ejemplo, no se est� construyendo bien el URL


DetailView
..........

Para obtener informaci�n de detalle sobre un objeto en particular, Django implementa ``DetailView``. Como atributo de 
la clase basta con definir ``model`` para indicar a qu� modelo pertenece el objeto que se requiere.

Por ejemplo, podemos reescribir nuestra vista-funci�n de la clase anterior, usando vistas gen�ricas esta vez:

.. code-block:: python

    class AutorDetailView(DetailView):
        
        model = Autor
        template_name = "libros/autor_detail.html"
        context_object_name = "autor"

        
Adicionalmente, necesitamos cambiar la l�nea de mapeo de URL en el archivo ``urls.py`` de la aplicaci�n de libros. 
Esta l�nea ahora quedar�a de la siguiente forma:

.. code-block:: python

    url(r'^autor/(?P<pk>\d+)/$', AutorDetailView.as_view(), name='autor_detail'),

El flujo de llamadas en un ``DetailView`` ocurre en el siguiente orden:

1) ``dispatch()``
2) ``http_method_not_allowed()``
3) ``get_template_names()``
4) ``get_slug_field()``
5) ``get_queryset()``
6) ``get_object()``
7) ``get_context_object_name()``
8) ``get_context_data()``
9) ``get()``
10) ``render_to_response()``


ListView
........

Para mostrar listados de objetos, Django implemente ``ListView``. Podemos sobrescribir la vista 
``libros.views.index`` utilizando la vista gen�rica en su lugar:

.. code-block:: python

    class AutorListView(ListView):
        
        model = Autor
        template_name = "libros/index.html"
        context_object_name = "autores_list"
        
Si hacemos los cambios correspondientes al archivo de URLs, deber�amos preservar el funcionamiento del sitio, pero 
esta vez con un c�digo un poco m�s elegante.

Como podemos ver, es una ventaja notable el uso de vistas gen�ricas basadas en clase. �sta es la manera recomendada 
de implementar vistas.

Adicional a las expuestas hasta ahora, Django implementa las siguientes vistas gen�ricas:

CreateView
..........

UpdateView
..........

DeleteView
..........

Managers
--------
            
Sistema de plantillas
---------------------

Formularios
-----------

Se�ales
-------


   

