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


El método ``as_view`` también puede recibir cualquier cantidad de argumentos. Éstos sobrescribirán cualquier 
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
            self.url +=  "?q=%s" % libro.titulo
            return super(GoogleBookInfoRedirectView, self).get_redirect_url(*args, **kwargs)


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

La secuencia de llamadas que ``Listview`` ejecuta es la siguiente:

1) ``dispatch()``
2) ``http_method_not_allowed()``
3) ``get_template_names()``
4) ``get_queryset()``
5) ``get_context_object_name()``
6) ``get_context_data()``
7) ``get()``
8) ``render_to_response()``

Adicionalmente, Django implementa muchas otras vistas genéricas, entre ellas ``CreateView``, ``UpdateView`` y 
``DeleteView``, las cuales estaremos estudiando más adelante.


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

    class ContactView(View):
        form_class = ContactanosForm
        template_name = 'contactanos.html'

        def get(self, request, *args, **kwargs):
            form = self.form_class()
            return render(request, self.template_name, {'form': form})

        def post(self, request, *args, **kwargs):
            form = self.form_class(request.POST)
            if form.is_valid():
                # procesar datos
                return HttpResponseRedirect('/gracias/')

            return render(request, self.template_name, {'form': form})


Se puede hacer aún más sencillo todavía, utilizando la vista genérica ``FormView``:

.. code-block:: python

    from django.views.generic.base import FormView

    from .forms import ContactanosForm

    class ContactView(FormView):
        form_class = ContactanosForm
        template_name = 'contactanos.html'
        success_url = '/gracias/'

        def form_valid(self, form):
            # procesar datos
            return super(ContactanosView, self).form_valid(form)


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

.. code-block:: python

    >>> f.errors
    {'asunto': [u'This field is required.']}


fields
......

A través del atributo ``fields``, el formulario guarda un diccionario con todos sus campos. En donde cada clave será 
el nombre del campo, y el valor será el objeto correspondiente de tipo ``Field``

.. code-block:: python

    >>> for campo in f.fields.values():
    ...     print campo
    ... 
    <django.forms.fields.CharField object at 0x24bb510>
    <django.forms.fields.CharField object at 0x24bb5d0>
    <django.forms.fields.EmailField object at 0x24bb650>
    <django.forms.fields.BooleanField object at 0x24bb6d0>


Ahora intentemos explorar usando ``dir()`` y ``help()`` en esos campos y sus atributos.

Cada campo también tiene un atributo ``errors``, así como un atributo ``label`` y ``label_tag``. Esto es útil si 
queremos desplegar el formulario de forma personalizada, sin estar restringido a los métodos ``Form.as_p``, 
``Form.as_ul``, etc.

.. code-block:: django

    <form action="/contactanos/" method="post">
        {% for field in form %}
            <div class="fieldWrapper">
                {{ field.errors }}
                {{ field.label_tag }} {{ field }}
            </div>
        {% endfor %}
        <p><input type="submit" value="Enviar" /></p>
    </form>


cleaned_data
............

Cada campo en un formulario no sólo es responsable de validar sus valores, sino además de normalizarlos en un formato 
consistente. Por ejemplo, un campo de tipo ``DateField`` se convierte a un objeto Python de tipo ``datetime.date``. 
Una vez que se ha creado un objeto de tipo ``Form`` y éste ha validado sus datos, es posible acceder al atributo 
``cleaned_data``:

.. code-block:: python

    >>> data = {'asunto': 'hola',
    ...         'mensaje': 'Todo bien?',
    ...         'remitente': 'yo@ejemplo.com',
    ...         'reenviar_remitente': True}
    >>> f = ContactanosForm(data)
    >>> f.is_valid()
    True
    >>> f.cleaned_data
    {'reenviar_remitente': True, 'mensaje': u'Todo bien?', 'remitente': u'yo@ejemplo.com', 'asunto': u'hola'}

Cada vez que se necesite procesar los datos de un formulario desde una vista, esto debe hacerse accediendo a 
``Form.cleaned_data``.

error_css_class, required_css_class
...................................

A veces es necesario especificar una clase de estilo para los mensajes de error o de campos requeridos:

.. code-block:: python

    class ContactanosForm(Form):
        error_css_class = 'error'
        required_css_class = 'required'


Widgets
~~~~~~~

Un *widget*, en Django, implementa la manera de desplegar en HTML un elemento de entrada de un formulario.

Cada vez que se define un campo de un ``Form``, éste viene asociado con un widget por defecto, según su tipo de dato. 
Sin embargo, es posible especificar un widget en particular para algún campo:

.. code-block:: python

    from django import forms

    class CommentForm(forms.Form):
        name = forms.CharField()
        url = forms.URLField()
        comment = forms.CharField(widget=forms.Textarea)
      

Esto hará que el campo ``comment`` se muestre como un ``<textarea>``, en lugar del widget por defecto, que 
corresponde a un ``<input type='text'>``.

Como todos los widgets se definen como derivados de la clase ``django.forms.Widget``, es posible para el usuario 
implementar sus propios widgets, en el caso de ser necesario.

Django implementa, entre otros, los siguientes widgets básicos:

* TextInput
* NumberInput
* EmailInput
* URLInput
* PasswordInput
* HiddenInput
* DateInput
* DateTimeInput
* TimeInput
* TextArea
* CheckboxInput
* Select
* NullBooleanSelect
* SelectMultiple
* RadioSelect
* FileInput


Formularios en base a modelos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando queremos definir un formulario que corresponda a un modelo específico de nuestra aplicación, no necesitamos 
definir redundantemente los campos del modelo. Para esto, Django implementa la clase ``ModelForm``, que se encarga
automáticamente de hacer la correspondencia entre el formulario y su modelo respectivo.

Ahora definiremos formularios de edición que correspondan a nuestros modelos creados anteriormente: ``Autor`` y 
``Libro``. Para esto crearemos un archivo ``forms.py`` dentro de la aplicación ``libros``:

.. code-block:: python

    from django.forms import ModelForm
    from libros.models import Autor, Libro


    class AutorForm(ModelForm):
        class Meta:
            model = Autor
            

    class LibroForm(ModelForm):
        class Meta:
            model = Libro


Un ``ModelForm`` asume todos los campos de su modelo correspondiente. Si se quiere especificar un subconjunto de los 
campos del modelo en formulario, se define el atributo ``fields`` dentro de los atributos de ``Meta``, de la 
siguiente forma:

.. code-block:: python

    from django.forms import ModelForm
    from mi_app.models import Modelo
    
    
    class MiModeloForm(ModelForm):
        class Meta:
               model = Modelo
               fields ['campo1', 'campo2', 'otro_campo']



.. añadir información sobre Mixins para explicar cómo CreateView soporta formularios

               
CreateView
..........

Esta vez utilizaremos una vista genérica basada en clase para utilizar nuestro formulario de agregación de autores. 
Implementaremos para esto un ``CreateView``, que utilizará nuestro formulario definido para el modelo ``Autor``:

.. code-block:: python
    
    from django.views.generic.edit import CreateView
    from libros.forms import AutorForm
    
    class AutorCreateView(CreateView):
        
        form_class = AutorForm
        template_name = 'libros/autor_form.html'
        success_url = '/libros/'


``CreateView`` implementa el *Mixin* ``ModelFormMixin``, por lo cual está hecho para trabajar con un objeto ``Form``. 
No es necesario entonces implementar funciones que procesen los datos del formulario, sólo resta crear el template 
``autor_form.html`` y mapear los urls necesarios.

.. code-block:: django

    <!-- templates/libros/autor_form.html -->
    
    <h2>Agregar Autor</h2>

    <form action="" method="post">{% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Guardar" />
    </form> 


Agregaremos la siguiente línea a los patrones del archivo ``libros/urls.py`` (es necesario importar 
``AutorCreateView`` al comienzo del archivo):

.. code-block:: python

    url(r'^autor/create/$', AutorCreateView.as_view(), name='autor_form')


Y ahora agregaremos un enlace desde el índice para hacer referencia a este URL:

.. code-block:: django

    <!-- templates/libros/index.html -->
    
    <h1>Autores destacados</h1>
    {% if autores_list %}
        <ul>
        {% for autor in autores_list %}
            <li><a href="/libros/autor/{{ autor.id }}/">{{ autor.nombre }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No hay autores definidos en el sistema.</p>
    {% endif %}

    <a href="/libros/autor/create/">Agregar autor</a>

Esto es todo, ya tenemos una vista para creación de autores.


UpdateView
~~~~~~~~~~

Entre las vistas genéricas de edición, Django implementa ``UpdateView``, el cual muestra un formulario asociado a un 
modelo para editar y actualizar los campos de un objeto dado.

Primero haremos la plantilla que mostrará el formulario de edición, y la nombraremos ``autor_edit.html``:

.. code-block:: django

    <h2>Editar Autor</h2>

    <form action="" method="post">{% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Guardar" />
    </form>


Ahora agreguemos la siguiente vista al archivo ``libros/views.py``:

.. code-block:: python

    class AutorUpdateView(UpdateView):
        
        model = Autor
        template_name = 'libros/autor_edit.html'
        success_url = '/libros/'
        
        def form_valid(self, form):
            self.success_url = '/libros/autor/%s/' % self.get_object().id
            return super(AutorUpdateView, self).form_valid(form)


``form_valid()`` es un método que se ejecuta una vez que se ha validado el formulario, y se puede utilizar para 
introducir comportamiento específico. En este caso se ha utilizado para concatenar al URL el id del objeto que se 
está tratando, el cual es accesible mediante el método ``get_object()``.

Agregaremos ahora un enlace desde la plantilla de detalle del autor, con el fin de poder editar su información:

.. code-block:: django

    <h1>{{ autor.nombre }}</h1>

    <a href="/libros/autor/edit/{{ autor.id }}/">Editar información de autor</a>

    {% if autor.libro_set.all %}
        Obras escritas:
        <ul>
        {% for libro in autor.libro_set.all %}
            <li>{{ libro.titulo }} ({{ libro.fecha_pub|date:"Y" }}) <a href="/libros/search/{{ libro.id }}/">[buscar 
        info]<a/></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>Este autor no tiene obras asociadas.</p>
    {% endif %}

    <a href="/libros/">Volver al inicio</a>


Y su respectivo patrón en el archivo ``libros/urls.py``. Es necesario importar la clase ``AutorUpdateView``.

.. code-block:: python

    url(r'^autor/edit/(?P<pk>\d+)/$', AutorUpdateView.as_view(), name='autor_edit'),
    

...Si hemos hecho todo correctamente, tenemos un formulario de edición de autores, que se encarga de  crear un 
``ModelForm`` correspondiente al modelo especificado (Autor), validar automáticamente los datos de entrada y 
redirigir a la plantilla respectiva.


DeleteView
~~~~~~~~~~

Para finalizar con las vistas genéricas de edición, implementaremos una vista ``DeleteView``, que nos permita eliminar 
al autor desde su vista de edición.

En el archivo ``views.py``, luego de importar ``DeleteView``, agregaremos la siguiente vista:

.. code-block:: python
   
    class AutorDeleteView(DeleteView):
        
        model = Autor
        success_url = '/libros/'

Agregaremos la siguiente línea a la lista de patrones en ``urls.py``:

.. code-block:: python

    url(r'^autor/delete/(?P<pk>\d+)/$', AutorDeleteView.as_view(), name='autor_delete'),

Pondremos un enlace al final de ``autor_detail.html`` para eliminar al autor:

.. code-block:: django

    <h1>{{ autor.nombre }}</h1>

    <a href="/libros/autor/edit/{{ autor.id }}/">Editar información de autor</a>

    {% if autor.libro_set.all %}
        Obras escritas:
        <ul>
        {% for libro in autor.libro_set.all %}
            <li>{{ libro.titulo }} ({{ libro.fecha_pub|date:"Y" }}) <a href="/libros/search/{{ libro.id }}/">[buscar 
        info]<a/></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>Este autor no tiene obras asociadas.</p>
    {% endif %}

    <p><a href="/libros/autor/delete/{{ autor.id  }}/">[Eliminar autor]</a></p>

    <p><a href="/libros/">Volver al inicio</a></p>

Y finalmente crearemos un nuevo template llamado ``autor_confirm_delete.html`` con el siguiente código:

.. code-block:: django

    <form action="" method="post">{% csrf_token %}
        <p>Está seguro de que desea eliminar a "{{ autor.nombre }}"?</p>
        <input type="submit" value="Sí" />
    </form> 

    <a href="/libros/">Volver al inicio</a>

Ahora probemos. Ya es posible eliminar autores desde su vista de detalle.

**Ejercicio práctico:** Implementar lo necesario para poder agregar, editar y eliminar libros desde la plantilla de 
detalle del autor.


Sistema de plantillas
---------------------

Hasta ahora hemos estado usando los plantillas de Django de una manera superficial, aunque ya debemos entender 
ciertos conceptos, es el momento de exponer con más detalle el el sistema de *templates* de Django.

Un template es sencillamente cualquier archivo de texto como HTML, XML, CSV, etc. El cual permite la inclusión de 
ciertas etiquetas y acceso a variables.. Por ejemplo:

.. code-block:: django

    {% block titulo %}{{ seccion.titulo }}{% endblock %}

    {% block contenido %}
    <h1>{{ seccion.titulo }}</h1>
    
    {% for articulo in lista_articulo %}
        <h2>
        <a href="{{ articulo.get_url }}">
            {{ articulo.headline|upper }}
        </a>
        </h2>
        
        <p>{{ articulo.preview|truncatewords:"100" }}</p>
    {% endfor %}
        
    {% endblock %}


Variables
~~~~~~~~~

Las variables se denotan de esta forma: ``{{ variable }}``. Cuando el motor de plantillas encuentra una variable, 
evalúa esa variable y la reemplaza por su resultado. Los nombres de variables consisten en cualquier combinación de 
caracteres alfanuméricos y underscore ("_"). Puede accederse a cualquier atributo de la variable utilizando el punto 
("."):

.. code-block:: django

    <ul>
    {% for articulo in lista_articulo %}
        <li>{{ articulo.titulo }}</li>
    {% endfor %}
    </ul>
    

La invocación de métodos se hace sin paréntesis, como si fuese un atributo, y los condicionales y ciclos no están 
precedidos de dos puntos ":".

.. code-block:: django

    {% if autor.libro_set.all %}
        Obras escritas:
        <ul>
        {% for libro in autor.libro_set.all %}
            <li>{{ libro.titulo }} <a href="/libros/search/{{ libro.id }}/"></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>Este autor no tiene obras asociadas.</p>
    {% endif %}


Filtros
~~~~~~~

Los filtros se aplican para modificar el valor de una variable, y lucen de esta forma: ``{{ nombre|lower }}``. En 
este caso, se convierten todos los caracteres de la cadena en minúscula. Django implementa una serie de filtros por 
defecto:

add
...

Suma una valor adicional al existente. Por ejemplo:

.. code-block:: django

    {{ cantidad|add:"2" }}


addslashes
..........

"Escapa" los caracteres de comilla antes de ponerlos en el template:

.. code-block:: django

    {{ cadena|addslashes }}


date
....

Muestra una variable de tipo fecha dado un formato específico:

.. code-block:: django

    {{ fecha|date:"D d M Y" }}


default
.......

Si una variable es ``False`` o vacía, se usa la expresión dada por defecto.

.. code-block:: django

    {{ email|default:"Ingrese su email" }}

    
length
......

Retorna la longitud del valor. Funciona para cadenas o listas. Por ejemplo:

.. code-block:: django

    {{ autor.libro_set.all|length }}

    
striptags
.........

Suprime todas las etiquetas HTML o XML de una cadena de texto.

.. code-block:: django

    {{ valor|striptags }}


random
......

Retorna un elemento aleatorio de una colección:

.. code-block:: django

    {{ lista|random }}


Template tags
~~~~~~~~~~~~~

Un *template tag* se define como ``{% tag %}``, y definen comportamientos complejos del sistema de templates, como 
los ciclos y condicionales que hemos visto hasta ahora. Django implementa las siguientes etiquetas:

{% comment %}
.............

Comenta un segmento del texto:

.. code-block:: django

    <p>Publicado el {{ pub_date|date:"DD-MM-YY" }}</p>
    {% comment %}
        <p>eliminar <input type="button"></p>
    {% endcomment %}


{% csrf_token %}
................

Esta etiqueta existe para proteger el sitio de ataques de csrf (*Cross Site Request Forgeries*). Con los cuales se 
intenta acceder a un URL desde un huesped remoto, a través de algún código *javascript* por ejemplo. Se coloca en los 
formularios que utilicen método POST, para evitar efectos secundarios indeseados.

.. code-block:: django

    <form action="." method="post">{% csrf_token %}
    

{% cycle %}
...........

``cycle`` va retornando secuencialmente los elementos de una tupla cada vez que la etiqueta aparece. Esto es muy útil 
para alternar entre valores para modificar el template:

.. code-block:: django

    {% for obj in una_lista %}
        <tr class="{% cycle 'dark' 'light' %}">
            ...
        </tr>
    {% endfor %}


Existe una lista bastante extensa de *template tags* implementadas en Django, para una información más amplia, debe 
consultarse la `documentación oficial <https://docs.djangoproject.com/en/dev/ref/templates/builtins/>`_.


{% autoescape %}
................

Controla la interpretación de caracteres HTML dentro de una cadena de texto. Si la opción está en ``on``, las etiquetas 
HTML no serán interpretadas como tal.

.. code-block:: django

    {% autoescape on %}
        {{ body }}
    {% endautoescape %}


{% url %}
.........

Devuelve un URL dado una vista definida en algún archivo de URLs.

.. code-block:: django

    {% url 'nombre_de_una_vista' arg1=v1 arg2=v2 %}
    

Herencia de templates
~~~~~~~~~~~~~~~~~~~~~

Una de las particularidades del sistema de plantillas de Django, es que éstas pueden diseñarse jerárquicamente, a 
través de la herencia y sobrescritura de templates. Esto se hace mediante las etiquetas ``{% extends %}`` y 
``{% block %}``. Usualmente se define un template base que contenga la estructura más externa del HTML, y que se 
encargue de incluir todos los archivos de estilo y javascript necesarios globalmente. Y entonces los demás templates 
heredan de éste.

Crearemos un nuevo archivo html en la carpeta de templates:

.. code-block:: django

    <!DOCTYPE html>
    <html lang="es">
    <head>
        <link rel="stylesheet" href="style.css" />
        <title>{% block titulo %}Bienvenidos a libronline{% endblock %}</title>
    </head>

    <body>
        <div id="sidebar">
            {% block menu %}
            <ul>
                <li><a href="/libros/">Índice de autores</a></li>
                <li><a href="#">Blog</a></li>
                <li><a href="#">Contactenos</a></li>
            </ul>
            {% endblock %}
        </div>

        <h1>Libronline, tu red de lectura</h1>
        <div id="content">
            
            {% block contenido %}{% endblock %}
        </div>
    </body>
    </html>

A este template lo llamaremos ``base.html``. Y sobrescribiremos el template que está en ``libros/index.html`` para 
que herede de éste.

.. code-block:: django

    {% extends "base.html" %}

    {% block titulo %}Bienvenidos a libronline - Autores {% endblock %}

    {% block contenido %}
    <h1>Autores destacados</h1>
    {% if autores_list %}
        <ul>
        {% for autor in autores_list %}
            <li><a href="/libros/autor/{{ autor.id }}/">{{ autor.nombre }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No hay autores definidos en el sistema.</p>
    {% endif %}

    <a href="/libros/autor/create/">Agregar autor</a>
    {% endblock %}


De esta forma cada template derivado de ``base.html``, se encarga de sobrescribir los bloques que necesite, 
refiriéndose a ellos por sus mismos nombres en el template base. 

La herencia de templates permite una estructuración ordenada y funcional de las plantillas en el proyecto, 
promoviendo el reciclaje y la legibilidad del código HTML.


Managers
--------

Todos los modelos de Django incluyen un ``Manager`` que se encargará de implementar las conexiones a la base de 
datos. Por defecto, cada modelo tiene un atributo llamado ``objects``, el cual es un objeto de tipo ``Manager``. 
Podríamos querer que el Manager se llame de otra forma, o implementar varios managers distintos para un mismo modelo.

.. code-block:: python

    from django.db import models

    class Persona(models.Model):
        #...
        gente = models.Manager()
        
Luego de definir un modelo como el de este ejemplo, podemos acceder a un listado de todas las instancias existentes a 
través de el atributo ``gente``, en lugar del habitual ``objects``:

.. code-block:: python

    Persona.gente.all()
    

Es posible extender la clase ``Manager`` creando nuevos manejadores. Esto permite al programador manipular los 
queries en SQL directamente, añadiendo al modelo funcionalidad a nivel de tablas. Para añadir funcionalidad a nivel 
de una fila, no es necesario personalizar un Manager, basta con implementar un método en el modelo.

Por ejemplo, podemos definir un ``AcademicBookManager``, que retorne los libros de una vez filtrando por género, 
únicamente aquellos libros académicos. Para esto definimos la siguiente clase en ``models.py``:

.. code-block:: python
    
    from django.db import models

    class AcademicBookManager(models.Manager):
        
        def get_queryset(self):
            return super(AcademicBookManager, self).get_queryset().filter(genero=4)


Y agregamos los atributos de los manejadores al comienzo de la clase ``Libro``:

.. code-block:: python

    class Libro(models.Model):
    
        objects = models.Manager()
        academic = AcademicBookManager()
        # ...
        

Ahora tenemos nuestro modelo con su manejador ``objects`` como es lo normal, pero adicionalmente podemos invocar el 
otro Manager:

.. code-block:: python

    Libro.academic.all()
    

SQL en los modelos
~~~~~~~~~~~~~~~~~~

Otra característica útil de definir nuestros propios Managers, es la posibilidad de lidiar directamente con los 
queries a BD. 

La clase ``Manager`` cuenta con el método ``raw()`` para ejecutar *queries* a la base de datos directamente:

.. code-block:: python

    >>> from libros.models import Autor
    >>> for a in Autor.objects.raw('Select * from libros_autor'):
    ...     print a
    ... 
    Herman Hesse
    Paulo Coelho
    Serafin Mazparrote
    Milan Kundera
    

Por supuesto, esto no es nada interesante, obtenemos lo mismo invocando a ``all()``, pero hemos podido ver que aunque 
Django ofrece una capa de abstracción entre el programador y la base de datos, ésta sigue estando accesible 
fácilmente a través del *Manager* de un modelo.

Pase de parámetros a raw()
..........................

Es posible pasar cualquier cantidad de parámetros a la función ``raw()`` como una lista o un diccionario de 
argumentos. Por ejemplo:

.. code-block:: python

    >>> apellido = 'Perez'
    >>> Persona.objects.raw('SELECT * FROM myapp_persona WHERE last_name = %s', [apellido])
    

Este mecanismo protege las consultas a base de datos de posibles ataques de *SQL injection*. Por esto no se 
recomienda formatear directamente el texto del query con los parámetros necesarios.


SQL directo
~~~~~~~~~~~

A veces es necesario efectuar instrucciones en SQL sin atarlas necesariamente a un modelo. A través de la biblioteca 
``django.db`` pueden efectuarse muchas operaciones referentes a la base de datos. Por lo general, utilizamos el 
objeto ``django.db.connection``, sobre el cual ejecutamos el método ``cursor()`` para obtener un cursor, y sobre éste 
ejecutamos los *queries* necesarios:

.. code-block:: python

    from django.db import connection

    def my_custom_sql(self):
        cursor = connection.cursor()

        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        
        row = cursor.fetchone()
        return row
        
        
También existe el método ``cursor.fetchall()`` para obtener todas las filas de una consulta con varios resultados.

Es posible utilizar un *cursor* como un manejador de contexto, de la siguiente forma:

.. code-block:: python

    with connection.cursor() as c:
        c.execute(...)
       

Esto, como con los archivos, nos permite cierta legibilidad, nos evita la necesidad de cerrarlo, y encapsula 
secciones del código para evitar efectos secundarios.


Stored Procedures
.................

El objeto cursor, además de ``execute`` para hacer las consultas, tiene un método ``callproc``, para invocar *stored 
procedures* en la base de datos:

.. code-block:: python

    from django.db import connection
    
    with connection.cursor() as cur:
        cur.callproc('proc_name')


Si necesitamos definir un modelo cuya fuente de datos utilice *stored procedures*, lo más adecuado es definir un 
``Manager`` específico para que implemente las llamadas necesarias:

.. code-block:: python

   from django.db import models, connection

    class StoredProcedureManager(models.Manager):
        
        def get_queryset(self):
            cur = connection.cursor()
            return cur.execute('SELECT store_proc')
            # return cur.callproc('store_proc')


Django es un framework bastante extenso, por lo cual es difícil cubrir todas sus funcionalidades desde un principio. 
Sin embargo, hemos cubierto lo suficiente para tener una concepción integral acerca de las herramientas que este 
framework provee, así como la posibilidad de modificar y extender dichas herramientas.