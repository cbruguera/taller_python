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

``RedirectView``, como su nombre lo indica, simplemente efectúa una redirección a un URL dado.

Ejemplo:

.. code-block:: python

    from django.views.generic.base import RedirectView
    
    class GoogleRedirectView(RedirectView):
        
        url = "https://www.google.com/"


Sin embargo, no es necesario implementar una subclase de ``RedirectView`` si no es necesario, también podemos 
utilizar directamente la clase desde el archivo de URLs de la siguiente manera:

.. code-block:: python

    from django.conf.urls import patterns, url
    from django.views.generic.base import RedirectView


    urlpatterns = patterns('',

        url(r'^django-doc/$', RedirectView.as_view(url='http://djangoproject.com')),
    )


El flujo de ejecución de ``RedirectView`` ocurre de la siguiente forma:

1) ``dispatch()``
2) ``http_method_not_allowed()``
3) ``get_redirect_url()``

El método ``get_redirect_url`` es el que construye el URL destino de la redirección. Si la construcción de este URL 
requiere de algún tipo de procesamiento, se necesita sobrescribir el método:

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

.. hay un error con este ejemplo, no se está construyendo bien el URL

El atributo ``query_string`` indica que el URL puede recibir argumentos vía GET.


DetailView
..........

Para obtener información de detalle sobre un objeto en particular, Django implementa ``DetailView``. Como atributo de 
la clase basta con definir ``model`` para indicar a qué modelo pertenece el objeto que se requiere.

Por ejemplo, podemos reescribir nuestra vista-función de la clase anterior, usando vistas genéricas esta vez:

.. code-block:: python

    class AutorDetailView(DetailView):
        
        model = Autor
        template_name = "libros/autor_detail.html"
        context_object_name = "autor"

        
Adicionalmente, necesitamos cambiar la línea de mapeo de URL en el archivo ``urls.py`` de la aplicación de libros. 
Esta línea ahora quedaría de la siguiente forma:

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
``libros.views.index`` utilizando la vista genérica en su lugar:

.. code-block:: python

    class AutorListView(ListView):
        
        model = Autor
        template_name = "libros/index.html"
        context_object_name = "autores_list"
        
Si hacemos los cambios correspondientes al archivo de URLs, deberíamos preservar el funcionamiento del sitio, pero 
esta vez con un código un poco más elegante.

Como podemos ver, es una ventaja notable el uso de vistas genéricas basadas en clase. Ésta es la manera recomendada 
de implementar vistas.

Adicionalmente, Django implementa muchas otras vistas genéricas, entre ellas:

* CreateView
* UpdateView
* DeleteView

Éstas las estaremos estudiando más adelante.


Formularios
-----------

A pesar de que es posible procesar formularios únicamente utilizando la clase ``HttpRequest``, Django cuenta con
la biblioteca ``django.forms``, la cual implementa una serie de clases y funcionalidades para el manejo de formularios.

A través de la biblioteca de manejo de formularios, es posible:

* Desplegar un formulario HTML con *widgets* generados automáticamente.
* Validar automáticamente los datos introducidos en un formulario.
* Convertir los datos introducidos a sus respectivos tipos de datos esperados en Python.

Clase *Form*
~~~~~~~~~~~~

Un objeto de tipo ``Form`` encapsula una secuencia de campos y un conjunto de reglas de validación que deben cumplirse
para que el formulario sea aceptado. Todos los objetos de este tipo deben ser instancia de la clase 
``django.forms.Form`` o de una subclase de ésta, y sus campos se definen de manera similar a los modelos. 

Por ejemplo, podemos utilizar un ``Form`` para implementar una funcionalidad de "Contáctanos", de la siguiente 
forma:

.. code-block:: python

    from django import forms

    class ContactanosForm(forms.Form):
        asunto = forms.CharField(max_length=100)
        mensaje = forms.CharField()
        remitente = forms.EmailField()
        reenviar_remitente = forms.BooleanField(required=False)


Formularios desde la vista
~~~~~~~~~~~~~~~~~~~~~~~~~~

Para procesar un formulario como el que definimos en el ejemplo anterior, podemos definir una vista de la siguiente manera:

.. code-block:: python

    from django.shortcuts import render
    from django.http import HttpResponseRedirect

    def contact(request):
        if request.method == 'POST':
            form = ContactanosForm(request.POST)
            if form.is_valid():
                # Procesar datos
                return HttpResponseRedirect('/gracias/')
        else:
            form = ContactanosForm()

        return render(request, 'contactanos.html', {
            'form': form,
        })
        

Utilizando vistas basadas en clase, lo haríamos de esta forma:

.. code-block:: python

    from django.http import HttpResponseRedirect
    from django.shortcuts import render
    from django.views.generic.base import View

    from .forms import ContactanosForm

    class ContactanosView(View):
        form_class = ContactanosForm
        initial = {'key': 'value'}
        template_name = 'contactanos.html'

        def get(self, request, *args, **kwargs):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})

        def post(self, request, *args, **kwargs):
            form = self.form_class(request.POST)
            if form.is_valid():
                # procesar datos
                return HttpResponseRedirect('/gracias/')

            return render(request, self.template_name, {'form': form})


Formularios desde el *template*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Del lado de las plantillas simplemente mostramos el objeto con nombre ``form`` que está siendo pasado desde la vista
a través del contexto:

.. code-block:: django

    <form action="/contact/" method="post">
    {{ form.as_p }}
    <input type="submit" value="Submit" />
    </form>

En el ejemplo estamos usando el método ``as_p`` para desplegar el formulario como una serie de etiquetas ``<p>`` 
en HTML. También es posible mostrar el formulario invocando los métodos ``as_ul()`` para una lista sin orden y 
``as_table()`` para mostrarlo como una tabla.

El API de la clase *Form*
~~~~~~~~~~~~~~~~~~~~~~~~~

Un objeto de la clase ``Form`` puede encontrarse asociado o no a un conjunto de datos. La terminología que se utiliza
en inglés para este concepto es el de *bound form* y *unbound form*. Un formulario con datos (*bound*) es capaz de
validar los datos, y puede mostrar un "render" en HTML con sus valores correspondientes en los campos. Un formulario 
sin datos (*unbound*) únicamente puede mostrar en HTML sus campos vacíos.

Para crear un formulario, se instancia la clase correspondiente:

.. code-block:: python

    >>> f = ContactanosForm()


Para asociar datos a un formulario, se le debe pasar un diccionario como primer argumento al constructor de la clase:

.. code-block:: python

    >>> data = {'asunto': 'Hola',
    ...         'mensaje': 'Hola, cómo estás?',
    ...         'recipiente': 'yo@ejemplo.com',
    ...         'reenviar_recipiente': True}
    >>> f = ContactanosForm(data)

La clase form cuenta con los siguientes métodos:

is_bound()
..........

Para distinguir entre un formulario asociado con datos y otro que no, se consulta el método ``is_bound()``:

.. code-block:: python

    >>> f = ContactanosForm()
    >>> f.is_bound
    False
    >>> f = ContactanosForm({'asunto': 'hola'})
    >>> f.is_bound
    True


is_valid()
..........

La principal funcionalidad de un formulario es la validación de datos, esto se hace invocando al método ``is_valid()``

.. code-block:: python

    >>> data = {'asunto': 'Hola',
    ...         'mensaje': 'Hola, todo bien?',
    ...         'recipiente': 'yo@ejemplo.com',
    ...         'reenviar_recipiente': True}
    >>> f = ContactanosForm(data)
    >>> f.is_valid()
    True

Si intentamos introducir un dato inválido, u omitir un campo requerido, el método retorna ``False``. Por defecto, 
todos los campos de un formulario se asumen como requeridos.

.. code-block:: python

    >>> data = {'asunto': '',
    ...         'mensaje': 'Hola, todo bien?',
    ...         'recipiente': 'yo@ejemplo.com',
    ...         'reenviar_recipiente': True}
    >>> f = ContactanosForm(data)
    >>> f.is_valid()
    False


errors
......

Todo objeto de tipo ``Form`` tiene un atributo ``errors``, en donde se obtiene un diccionario con los errores ocurridos
durante la validación.

.. .. code-block:: python


initial
.......

.. .. code-block:: python


fields
......

.. .. code-block:: python


cleaned_data
............

.. .. code-block:: python


label_suffix
............

.. .. code-block:: python



Formularios asociados a modelos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando queremos definir un formulario que corresponda a un modelo específico de nuestra aplicación, no necesitamos 
definir redundantemente los campos del modelo. Para esto, Django implementa la clase ``ModelForm``, que se encarga
automáticamente de hacer la correspondencia entre el formulario y su modelo respectivo.

Ahora definiremos un formulario que corresponda a nuestros modelos creados anteriormente: ``Autor`` y ``Libro``. Para
esto crearemos un archivo ``forms.py`` dentro de la aplicación ``libros``:

.. code-block:: python

    from django.forms import ModelForm
    from libros.models import Autor, Libro


    class AutorForm(ModelForm):
        class Meta:
            model = Autor
            

    class LibroForm(ModelForm):
        class Meta:
            model = Libro







.. CreateView
.. UpdateView
.. DeleteView

Managers
--------
            
Sistema de plantillas
---------------------

Señales
-------


   

