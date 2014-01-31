.. Taller de Python documentation master file, created by
   sphinx-quickstart on Mon Jan 27 16:38:42 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==================
Aprendiendo Python
==================

.. contents:: Contenido
   :depth: 2

   
Introducción
------------

Python es un lenguaje de programación de propósito general muy fácil de aprender, con una sintaxis característica que 
hace que los programas escritos en él sean muy legibles, ampliamente utilizado por grandes empresas y programadores 
independientes; y además, libre. 

Python fue creado a finales de la década de los 80 por Guido van Rossum, un programador holandés.


¿Por qué Python?
~~~~~~~~~~~~~~~~

* Fácil de aprender
* Altamente expresivo
* Sintáxis legible
* Software libre
* Gran cantidad de bibliotecas para diversos propósitos

Python es un lenguaje que está diseñado para que sea elegante y sencillo de escribir, y a la vez provee herramientas 
de muy alto nivel para la manipulación de estructuras de datos. Existe, además, una gama muy amplia de bibliotecas
gratuitas para prácticamente cualquier propósito. Todo esto hace de Python un lenguaje muy versátil y práctico.


Características del lenguaje
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Multiparadigma:** Además de ser un lenguaje imperativo como muchos otros, Python provee la capacidad para programar según distintos paradigmas, como por ejemplo la *Programación Orientada a Objetos* (POO) o incluso el paradigma funcional.

* **Sistema de tipos:**
	+ Tipado dinámico (dynamic typing): El tipo de las variables y las expresiones es evaluado en tiempo de ejecución. No es necesario declarar las variables antes de usarlas.
	+ Tipado fuerte (strong typing): El intérprete no permite operaciones entre tipos de datos distintos sin convertirlos explícitamente.

* **Facilidad de extensión:** Se pueden escribir nuevos módulos fácilmente en C o C++. Y a su vez, es posible invocar al intérprete de Python desde C o C++.

El Zen de Python
~~~~~~~~~~~~~~~~
Los usuarios de Python se refieren a menudo a la Filosofía Python que es bastante análoga a la filosofía de Unix. 
El código que sigue los principios de Python de legibilidad y transparencia se dice que es "pitónico" (*pythonic* en inglés)". 
Contrariamente, el código opaco u ofuscado es bautizado como "no pitónico" (*unpythonic*). 
Estos principios fueron famosamente descritos por el desarrollador de Python Tim Peters en *El Zen de Python*.

::

	Bello es mejor que feo.
	Explícito es mejor que implícito.
	Simple es mejor que complejo.
	Complejo es mejor que complicado.
	Plano es mejor que anidado.
	Disperso es mejor que denso.
	La legibilidad cuenta.
	Los casos especiales no son tan especiales como para quebrantar las reglas.
	Aunque lo práctico gana a la pureza.
	Los errores nunca deberían pasar silenciosamente.
	A menos que hayan sido silenciados explícitamente.
	Frente a la ambigüedad, rechaza la tentación de adivinar.
	Debería haber una (y preferiblemente sólo una) manera obvia de hacerlo.
	Aunque esa manera puede no ser obvia al principio, a menos que seas holandés.
	Ahora es mejor que nunca.
	Aunque nunca es a menudo mejor que *ya mismo*.
	Si la implementación es difícil de explicar, es una mala idea.
	Si la implementación es fácil de explicar, puede que sea una buena idea.
	Los espacios de nombres (namespaces) son una gran idea ¡Hagamos más de eso!


El intérprete de Python
-----------------------

Python incluye un intérprete interactivo en el cual se escriben las instrucciones en una especie de línea de comandos; 
las expresiones pueden ser introducidas una a una, pudiendo verse el resultado de su evaluación inmediatamente, 
lo que da la posibilidad de probar porciones de código en el modo interactivo antes de integrarlo como parte de un 
programa. Esto resulta útil tanto para las personas que se están familiarizando con el lenguaje como para los 
programadores más avanzados.

Para abrir la consola interactiva de Python, basta con ejecutar:

.. code-block:: bash

	$ python

La cónsola interactiva de python puede evaluar expresiones del lenguaje python, incluyendo operaciones aritméticas.
Es también posible asignar valores a variables, y los valores permanecerán en memoria mientras el intérprete esté 
ejecutándose.
	
.. code-block:: bash

	Python 2.5.2 (r252:60911, Oct  5 2008, 19:29:17) 
	[GCC 4.3.2] on linux2
	Type "help", "copyright", "credits" or "license" for more information.
	>>> 1 + 1
	2
	>>> a = range(10)
	>>> print a
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	>>> type(a)
	<type 'list'>
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'a' is not defined

También es posible importar otros módulos desde el intérprete interactivo:

.. code-block:: bash

	>>> import math

Para explorar los atributos (incluyendo métodos) utilizamos la función ``dir()``

.. code-block:: bash

	>>> dir(math)
	['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 
	'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 
	'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 
	'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
	>>> math.pi
	3.141592653589793

Tipos de datos
--------------

Python implementa los tipos de datos habituales en otros lenguajes, como los tipos numéricos ``int`` y ``float``, 
así como el tipo lógico o ``bool``. Merecen especial atención el tipo *string* y los tipos estructurados o 
"colecciones", dentro de los cuales existen *diccionarios*, *tuplas*, *listas* y conjuntos.

Cadenas de texto (``str``)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Los strings son cadenas de texto que pueden definirse de varias formas:

* Entre comillas simples: ``'hola mundo!'``
* Entre comillas dobles: ``"hola mundo!"``
* Entre comillas triples (cadenas multi-línea): 

::

	'''hola
	mundo'''
	
	"""todo 
	bien?"""
	
Concatenación
.............

Es posible concatenar dos o más cadenas usando el operador ``+``, o usando el método ``''.join()``. 
Para determinar la longitud de una cadena, se utiliza la función ``len()``.

.. code-block:: bash

	>>> a = "hola"
	>>> a += " mundo!"
	>>> a
	'hola mundo!'
	>>> len(a)
	10
	>>> b = ''.join(["x", "y", "z", a])
	>>> b
	'xyzhola mundo'
	>>> '_'.join(["cadena", "compuesta", "con", "delimitador"])
	'cadena_compuesta_con_delimitador'


Formateo
........

También es posible "formatear" cadenas usando el operador ``%``:

.. code-block:: bash

	>>> "La respuesta es %s." % 42
	'La respuesta es 42.'

Repetición
..........

Una cadena puede repetirse utilizando el mismo operador de multiplicación (``*``)

.. code-block:: bash

	>>> h = "hola"
	>>> h * 3
	'holaholahola'

Indexación
..........

Para acceder a cualquiera de los caracteres de la cadena, se indexa de la misma manera que un "arreglo" en la mayoría 
de los lenguajes. El primer caracter corresponde al índice ``0``.

.. code-block:: bash

	>>> "Venezuela"[5]
	'u'

También pueden utilizarse índices negativos, los cuales comienzan a recorrer la cadena desde el último caracter.

.. code-block:: bash

	>>> "Venezuela"[-1]
	'a'
	>>> "Venezuela"[-2]
	'l'
	
"Slicing"
.........

Es posible obtener una sub-cadena de un string especificando un rango en el índice, a esto se le conoce como 
"rebanado" o *slicing*.

.. code-block:: bash
	
	>>> a = "Venezuela"
	>>> a[2:4]
	'ne'
	>>> a[:4]
	'Vene'
	>>> a[4:]
	'zuela'

Pertenencia (``in``)
....................

Para determinar si un caracter o subcadena está contenido dentro de otra cadena, se utiliza el operador lógico `in`:

.. code-block:: bash

	>>> "zuel" in "Venezuela"
	True
	>>> "b" in "Venezuela"
	False

Booleanos
~~~~~~~~~

Los datos de tipo *booleano* pueden tomar los valores ``True`` o ``False`` (así, con la primera letra en mayúscula). Y las expresiones 
lógicas pueden evaluarse utilizando los operadores `and`, `or`, y `not` y los operadores usuales de comparación 
(``<``, ``>``, ``<=``, ``>=``, ``==``, ``!=``).

.. code-block:: bash

	>>> a = "hola mundo"
	>>> a[:4] == "hola" and a[5:] == "mundo"
	True

Listas
~~~~~~

Las listas son uno de los tipos de datos fundamentales en Python. A diferencia de los arreglos en otros lenguajes,
las listas de Python son dinámicas y permiten una serie de operaciones bastante útiles.

Para definir una lista, se colocan los elementos entre corchetes. Una lista puede contener cualquier tipo de datos, incluyendo otras listas.

.. code-block:: bash

	>>> a = [1, 2, 3, "hola", ['x', 'y']]

Una función del lenguaje bastante útil es ``range(n)``, la cual genera una lista de enteros dentro del intervalo ``[0, n)``:

.. code-block:: bash

	>>> range(10)
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Todas las operaciones previamente definidas para el tipo ``str`` aplican para las listas:

.. code-block:: bash

	>>> a = [1, 2, 3, "hola", ['x', 'y']]
	>>> len(a)
	5
	>>> ['x', 'y'] in a
	True
	>>> a[1]
	2
	>>> a[2:4]
	[3, 'hola']
	>>> a * 2
	[1, 2, 3, 'hola', ['x', 'y'], 1, 2, 3, 'hola', ['x', 'y']]
	>>> [1, 2, 3] + [4, 5] + ["string"]
	[1, 2, 3, 4, 5, 'string']

Adicionalmente, se definen los siguientes métodos específicos para las listas:

``append()``
............

.. code-block:: bash

	>>> li = ["a", "b", "c"]
	>>> li.append("d")
	>>> li
	['a', 'b', 'c', 'd']
	

``extend()``
............

.. code-block:: bash

	>>> st = ["e", "f"]
	>>> li.extend(st)
	>>> li
	['a', 'b', 'c', 'd', 'e', 'f']


``index()``
...........

.. code-block:: bash

	>>> li.index('c')
	2

	
``remove()``
............

.. code-block:: bash

	>>> li.remove('c')
	>>> li
	['a', 'b', 'd', 'e', 'f']

Listas por comprensión
......................

Una de las características más poderosas de Python es la posibilidad de definir *listas por comprensión*. Ésta es una
característica muy propia de lenguajes funcionales como Haskell y Scheme.


Tuplas
~~~~~~
.. in, indexación, slicing
.. asignación a tuplas de variables (x, y, z) = (1, 2, 3)

Diccionarios
~~~~~~~~~~~~

.. - del d[42]
.. - clear()
.. - zip()
		
Conjuntos
~~~~~~~~~

.. - add()
.. - clear()
.. - copy()
.. - difference()
.. - difference_update()
.. - discard()
.. - remove()
.. - intersection()
.. - isdisjoint()
.. - issubset()
.. - issuperset()
.. - pop()

Usando un archivo fuente
------------------------
.. + Comentarios: simples y multilínea
.. + Funciones
.. 	- indentación
.. 	- docstring
.. 		· help()
.. + Estructuras de control de flujo

Manejo de archivos
------------------
.. open()
.. read??
.. write()
.. close()

.. Ejercicio práctico??