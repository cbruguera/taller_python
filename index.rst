.. Taller de Python documentation master file, created by
   sphinx-quickstart on Mon Jan 27 16:38:42 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==================
Aprendiendo Python
==================

.. contents:: Contenido
   :depth: 2

   
Introducci�n
------------

Python es un lenguaje de programaci�n de prop�sito general muy f�cil de aprender, con una sintaxis caracter�stica que 
hace que los programas escritos en �l sean muy legibles, ampliamente utilizado por grandes empresas y programadores 
independientes; y adem�s, libre. 

Python fue creado a finales de la d�cada de los 80 por Guido van Rossum, un programador holand�s.


�Por qu� Python?
~~~~~~~~~~~~~~~~

* F�cil de aprender
* Altamente expresivo
* Sint�xis legible
* Software libre
* Gran cantidad de bibliotecas para diversos prop�sitos

Python es un lenguaje que est� dise�ado para que sea elegante y sencillo de escribir, y a la vez provee herramientas 
de muy alto nivel para la manipulaci�n de estructuras de datos. Existe, adem�s, una gama muy amplia de bibliotecas
gratuitas para pr�cticamente cualquier prop�sito. Todo esto hace de Python un lenguaje muy vers�til y pr�ctico.


Caracter�sticas del lenguaje
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Multiparadigma:** Adem�s de ser un lenguaje imperativo como muchos otros, Python provee la capacidad para programar seg�n distintos paradigmas, como por ejemplo la *Programaci�n Orientada a Objetos* (POO) o incluso el paradigma funcional.

* **Sistema de tipos:**
	+ Tipado din�mico (dynamic typing): El tipo de las variables y las expresiones es evaluado en tiempo de ejecuci�n. No es necesario declarar las variables antes de usarlas.
	+ Tipado fuerte (strong typing): El int�rprete no permite operaciones entre tipos de datos distintos sin convertirlos expl�citamente.

* **Facilidad de extensi�n:** Se pueden escribir nuevos m�dulos f�cilmente en C o C++. Y a su vez, es posible invocar al int�rprete de Python desde C o C++.

El Zen de Python
~~~~~~~~~~~~~~~~
Los usuarios de Python se refieren a menudo a la Filosof�a Python que es bastante an�loga a la filosof�a de Unix. 
El c�digo que sigue los principios de Python de legibilidad y transparencia se dice que es "pit�nico" (*pythonic* en ingl�s)". 
Contrariamente, el c�digo opaco u ofuscado es bautizado como "no pit�nico" (*unpythonic*). 
Estos principios fueron famosamente descritos por el desarrollador de Python Tim Peters en *El Zen de Python*.

::

	Bello es mejor que feo.
	Expl�cito es mejor que impl�cito.
	Simple es mejor que complejo.
	Complejo es mejor que complicado.
	Plano es mejor que anidado.
	Disperso es mejor que denso.
	La legibilidad cuenta.
	Los casos especiales no son tan especiales como para quebrantar las reglas.
	Aunque lo pr�ctico gana a la pureza.
	Los errores nunca deber�an pasar silenciosamente.
	A menos que hayan sido silenciados expl�citamente.
	Frente a la ambig�edad, rechaza la tentaci�n de adivinar.
	Deber�a haber una (y preferiblemente s�lo una) manera obvia de hacerlo.
	Aunque esa manera puede no ser obvia al principio, a menos que seas holand�s.
	Ahora es mejor que nunca.
	Aunque nunca es a menudo mejor que *ya mismo*.
	Si la implementaci�n es dif�cil de explicar, es una mala idea.
	Si la implementaci�n es f�cil de explicar, puede que sea una buena idea.
	Los espacios de nombres (namespaces) son una gran idea �Hagamos m�s de eso!


El int�rprete de Python
-----------------------

Python incluye un int�rprete interactivo en el cual se escriben las instrucciones en una especie de l�nea de comandos; 
las expresiones pueden ser introducidas una a una, pudiendo verse el resultado de su evaluaci�n inmediatamente, 
lo que da la posibilidad de probar porciones de c�digo en el modo interactivo antes de integrarlo como parte de un 
programa. Esto resulta �til tanto para las personas que se est�n familiarizando con el lenguaje como para los 
programadores m�s avanzados.

Para abrir la consola interactiva de Python, basta con ejecutar:

.. code-block:: bash

	$ python

La c�nsola interactiva de python puede evaluar expresiones del lenguaje python, incluyendo operaciones aritm�ticas.
Es tambi�n posible asignar valores a variables, y los valores permanecer�n en memoria mientras el int�rprete est� 
ejecut�ndose.
	
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


Tambi�n es posible importar otros m�dulos desde el int�rprete interactivo:

.. code-block:: bash

	>>> import math

Para explorar los atributos (incluyendo m�todos) utilizamos la funci�n ``dir()``

.. code-block:: bash

	>>> dir(math)
	['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 
	'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 
	'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 
	'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 
	'sqrt', 'tan', 'tanh', 'trunc']
	>>> math.pi
	3.141592653589793

Tipos b�sicos
-------------

Python implementa los tipos de datos habituales en otros lenguajes, como los tipos num�ricos ``int`` y ``float``, 
as� como el tipo l�gico o ``bool``. Para los valores nulos, se utiliza el valor ``None``.

Es posible convertir de un tipo a otro invocando expl�citamente el tipo deseado, siempre que la conversi�n sea v�lida.

.. code-block:: bash

	>>> str(1)
	'1'
	>>> int('2')
	2
	>>> bool(1)
	True
	
Merecen especial atenci�n el tipo *string* y los tipos estructurados o "colecciones", 
dentro de los cuales existen *diccionarios*, *tuplas*, *listas* y conjuntos.

Cadenas de texto (``str``)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Los strings son cadenas de texto que pueden definirse de varias formas:

* Entre comillas simples: ``'hola mundo!'``
* Entre comillas dobles: ``"hola mundo!"``
* Entre comillas triples (cadenas multi-l�nea): 

::

	'''hola
	mundo'''
	
	"""todo 
	bien?"""
	
Concatenaci�n
.............

Es posible concatenar dos o m�s cadenas usando el operador ``+``, o usando el m�todo ``''.join()``. 
Para determinar la longitud de una cadena, se utiliza la funci�n ``len()``.

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

Tambi�n es posible "formatear" cadenas usando el operador ``%``:

.. code-block:: bash

	>>> "La respuesta es %s." % 42
	'La respuesta es 42.'

Repetici�n
..........

Una cadena puede repetirse utilizando el mismo operador de multiplicaci�n (``*``)

.. code-block:: bash

	>>> h = "hola"
	>>> h * 3
	'holaholahola'

Indexaci�n
..........

Para acceder a cualquiera de los caracteres de la cadena, se indexa de la misma manera que un "arreglo" en la mayor�a 
de los lenguajes. El primer caracter corresponde al �ndice ``0``.

.. code-block:: bash

	>>> "Venezuela"[5]
	'u'

Tambi�n pueden utilizarse �ndices negativos, los cuales comienzan a recorrer la cadena desde el �ltimo caracter.

.. code-block:: bash

	>>> "Venezuela"[-1]
	'a'
	>>> "Venezuela"[-2]
	'l'
	
"Slicing"
.........

Es posible obtener una sub-cadena de un string especificando un rango en el �ndice, a esto se le conoce como 
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

Para determinar si un caracter o subcadena est� contenido dentro de otra cadena, se utiliza el operador `in`:

.. code-block:: bash

	>>> "zuel" in "Venezuela"
	True
	>>> "b" in "Venezuela"
	False

Booleanos
~~~~~~~~~

Los datos de tipo *booleano* pueden tomar los valores ``True`` o ``False`` (as�, con la primera letra en may�scula). Y las expresiones 
l�gicas pueden evaluarse utilizando los operadores `and`, `or`, y `not` y los operadores usuales de comparaci�n 
(``<``, ``>``, ``<=``, ``>=``, ``==``, ``!=``).

.. code-block:: bash

	>>> a = "hola mundo"
	>>> a[:4] == "hola" and a[5:] == "mundo"
	True

Colecciones
-----------

Listas
~~~~~~

Las listas son uno de los tipos de datos fundamentales en Python. A diferencia de los arreglos en otros lenguajes,
las listas de Python son din�micas y permiten una serie de operaciones bastante �tiles.

Para definir una lista, se colocan los elementos entre corchetes. Una lista puede contener cualquier tipo de datos, incluyendo otras listas.

.. code-block:: bash

	>>> a = [1, 2, 3, "hola", ['x', 'y']]

range()
.......

Una funci�n del lenguaje bastante �til es ``range(n)``, la cual genera una lista de enteros dentro del intervalo ``[0, n)``:

.. code-block:: bash

	>>> range(10)
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	
Tambi�n puede invocarse especificando ambos l�mites:

.. code-block:: bash

	>>> range(5, 10)
	[5, 6, 7, 8, 9]
	
E incluso el tama�o del incremento:

.. code-block:: bash

	>>> range(10, 20, 3)
	[10, 13, 16, 19]

Operaciones sobre listas
........................

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

Adicionalmente, se definen los siguientes m�todos espec�ficos para las listas:

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

	>>> li = ["a", "b", "c"]
	>>> li.index('c')
	2
	>>> li.index("f")
	Traceback (most recent call last)_
		File "<stdin>", line 1, in <module>
	ValueError: 'f' is not in list

	
``remove()``
............

.. code-block:: bash

	>>> li.remove('c')
	>>> li
	['a', 'b', 'd', 'e', 'f']

Listas por comprensi�n
......................

Una de las caracter�sticas m�s poderosas de Python es la posibilidad de definir *listas por comprensi�n*. �sta es una
caracter�stica muy propia de lenguajes funcionales.

La ventaja de las listas por comprensi�n radica en la posibilidad de definir una colecci�n de elementos de una manera
acorde a definiciones matem�ticas. Por ejemplo, para generar una lista con todos los enteros impares hasta 99:

.. code-block:: bash

	>>> L = [x for x in range(100) if x % 2 != 0]
	>>> L
	[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 
	33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 
	63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 
	93, 95, 97, 99]

	
Las listas por comprensi�n pueden contener expresiones complejas y funciones anidadas:

.. code-block:: bash

	>>> from math import pi
	>>> [str(round(pi, i)) for i in range(1, 6)]
	['3.1', '3.14', '3.142', '3.1416', '3.14159']
	
Tuplas
~~~~~~

Una tupla es una estructura parecida a una lista, con la diferencia de que �sta es *inmutable*, es decir, no pueden
eliminarse o agregarse elementos, ni �stos pueden cambiar una vez creada la tupla.

Las tuplas se definen como una secuencia de elementos separados por comas, y encerrados entre par�ntesis.

.. code-block:: bash

	>>> t = ("tuples", "are", "immutable")
	>>> t[0]
	'tuples'
	>>> t[0] = "assignment"
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'tuple' object does not support item assignment

Las operaciones de pertenencia, indexaci�n y "slicing" funcionan de igual forma que en las listas:

.. code-block:: bash

	>>> t = (10, 11, 12)
	>>> 10 in t
	True
	>>> t[-1]
	12
	>>> t[1:]
	(11, 12)

Una funcionalidad bastante �til en el caso de las tuplas, es la posibilidad de hacer asignaciones m�ltiples a un 
conjunto de variables.

.. code-block:: bash

	>>> (x, y, z) = (7, 8, 9)
	>>> x
	7
	>>> y
	8
	>>> z
	9

Las tuplas se usan en los casos en los que se sabe que los datos no necesitar�n modificarse. Sin embargo, siempre
es posible convertir de uno a otro tipo de dato con las funciones nativas ``list()`` y ``tuple()``.

.. code-block:: bash

	>>> t = ("x", "y", "hola")
	>>> list(t)
	['x', 'y', 'hola']
	>>> tuple(range(10))
	(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


Diccionarios
~~~~~~~~~~~~

Un diccionario define una relaci�n 1 a 1 entre claves y valores, algo muy parecido a los objetos de la clase Hashtable
en Java. Se define utilizando llaves, de manera similar a javascript.

.. code-block:: bash

	>>> d = {"server":"mpilgrim", "database":"master"}
	>>> d
	{'server': 'mpilgrim', 'database': 'master'}
	>>> d["server"]
	'mpilgrim'
	>>> d["database"]
	'master'
	>>> d["mpilgrim"]
	
Los valores de los diccionarios pueden ser de cualquier tipo, incluso otros diccionarios. De igual forma, un diccionario
puede contener simult�neamente valores de distintos tipos. Las claves deben ser de alg�n tipo *inmutable*, como n�meros, 
cadenas o incluso tuplas.

Es importante acotar que los diccionarios en Python no siguen ning�n tipo de orden entre sus elementos.

.. code-block:: bash

	>>> dict = {1: "uno", 2: "dos", 2.5: "dos punto cinco"}
	>>> dict[2.5]
	'dos punto cinco'
	
Para eliminar un registro en el diccionario se utiliza la funci�n ``del(k)``:

.. code-block:: bash
	
	>>> del(dict[2.5])
	>>> dict
	{1: "uno", 2: "dos"}
	
Para limpiar el contenido completo de un diccionario, se utiliza el m�todo ``clear()``.

.. code-block:: bash

	>>> dict.clear()
	>>> dict
	{}

Un par de funciones nativas de considerable utilidad son ``zip()`` y ``dict()``. La funci�n ``zip(L1, L2)`` retorna
una lista de tuplas correspondiendo los valores de L1 y L2 respectivamente, y la funci�n dict(L) recibe una lista
de tuplas y retorna un diccionario que corresponde a dichas tuplas. Por ejemplo:

.. code-block:: bash

	>>> ciudades = ["Caracas", "Berlin", "Buenos Aires", "Lima"]
	>>> paises = ["Venezuela", "Alemania", "Argentina", "Peru"]
	>>> parejas = zip(paises, ciudades)
	>>> parejas
	[('Venezuela', 'Caracas'), ('Alemania', 'Berlin'), ('Argentina', 'Buenos Aires'), 
	('Peru', 'Lima')]
	>>> capitales = dict(parejas)
	>>> capitales
	{'Argentina': 'Buenos Aires', 'Venezuela': 'Caracas', 'Peru': 'Lima', 'Alemania': 'Berlin'}

		
Conjuntos
~~~~~~~~~

Python tiene la particularidad de implementar ``set`` como tipo de dato nativo, el cual corresponde al concepto
matem�tico de conjunto, e implementa todas sus funciones b�sicas.

Un conjunto se define como una secuencia de elementos entre llaves, o mediante la funci�n ``set(L)`` a partir de una
lista de elementos ``L``.

.. code-block:: bash

	>>> pares = {2, 4, 6, 8, 10}
	>>> pares
	set([8, 10, 4, 2, 6])
	type(pares)
	<type 'set'>
	>>> impares = set([n for n in range(10) if n % 2 != 0])
	>>> impares
	set([1, 3, 9, 5, 7])

	
Correspondiendo con el principio matem�tico de los conjuntos, ning�n elemento se repite.

.. code-block:: bash

	>>>set([1, 2, 3, 2, 1])
	set([1, 2, 3])

Un conjunto puede definirse a partir de una cadena de texto, y es �til para saber cu�les caracteres existen en un string.

.. code-block:: bash

	>>> zen = "If the implementation is hard to explain, it's a bad idea."
	>>> set(zen)
	set(['a', ' ', 'b', 'e', 'd', "'", 'f', 'I', 'h', 'm', 'l', 'p', 'n', 'i', 's', 
	'r', 't', 'x', '.', ',', 'o'])

El tipo ``set`` implementa los siguientes m�todos:

``add()``
.........

.. code-block:: bash

	>>> conj = {1, 2, 3}
	>>> conj.add(4)
	>>> conj
	set([1, 2, 3, 4])

``clear()``
...........

.. code-block:: bash

	>>> conj.clear()
	>>> conj
	set([])

``copy()``
..........

.. code-block:: bash

	>>> conj.add(1)
	>>> conj.add(42)
	>>> conj2 = conj.copy()
	>>> conj2
	set([1, 42])

Copiar un conjunto no es lo mismo que asign�rselo a otra variable, ya que en la asignaci�n ambas variables se refieren
a un mismo objeto, por lo que modificaciones a uno afectar�an el valor del otro y viceversa.

``difference()``
................

.. code-block:: bash

	>>> x = {"a","b","c","d","e"}
	>>> y = {"b","c"}
	>>> z = {"c","d"}
	>>> x.difference(y)
	set(['a', 'e', 'd'])
	>>> x.difference(y).difference(z)
	set(['a', 'e'])

En lugar de usar el m�todo ``difference()``, podemos utilizar el operador ``-``:

.. code-block:: bash

	>>> x - y
	set(['a', 'e', 'd'])
	>>> x - y - z
	set(['a', 'e'])
	
``discard()``
.............

Si un elemento se encuentra en un conjunto, este m�todo lo elimina, y si el elemento no existe, no sucede nada.

.. code-block:: bash

	>>> x = {"a","b","c","d","e"}
	>>> x.discard("a")
	>>> x
	set(['c', 'b', 'e', 'd'])
	>>> x.discard("z")
	>>> x
	set(['c', 'b', 'e', 'd'])


``remove()``
............

A diferencia de ``discard()``, ``remove()`` elimina un elemento dado, y si �ste no existe ocurre un ``KeyError``.

.. code-block:: bash

	>>> x = {"a","b","c","d","e"}
	>>> x.remove("a")
	>>> x
	set(['c', 'b', 'e', 'd'])
	>>> x.remove("z")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: 'z'

	
``intersection()``
..................

.. code-block:: bash

	>>> x = {"a","b","c","d","e"}
	>>> y = {"c","d","e","f","g"}
	>>> x.intersection(y)
	set(['c', 'e', 'd'])


``union()``
...........

.. code-block:: bash

	>>> c1 = {"Carlos", "Jorge", "Luis"}
	>>> c2 = {"Oscar", "Antonio"}
	>>> c1.union(c2)
	set(['Luis', 'Antonio', 'Jorge', 'Carlos', 'Oscar'])

``isdisjoint()``
................

Retorna ``True`` si la intersecci�n entre dos conjuntos es nula.

.. code-block:: bash

	>>> set1 = {"a", "b", "c"}
	>>> set2 = {"c", "d", "e"}
	>>> set3 = {"d", "e", "f"}
	>>> set1.isdisjoint(set2)
	False
	>>> set1.isdisjoint(set3)
	True

	
``issubset()`` / ``issuperset()``
.................................

.. code-block:: bash

	>>> x = {"a", "b", "c", "d", "e"}
	>>> y = {"c", "d"}
	>>> x.issubset(y)
	False
	>>> y.issubset(x)
	True
	>>> x.issuperset(y)
	True
	
Tambi�n es posible utilizar los operadores de comparaci�n para evaluar subconjuntos:

.. code-block:: bash

	>>> set1 = {1, 2, 3}
	>>> set2 = {2}
	>>> set3 = set2.copy()
	>>> set2 < set1
	True
	set2 == set3
	True
	set1 <= set2
	False

``pop()``
.........

El m�todo ``pop()`` retorna un elemento (el primero que encuentra) y lo elimina del conjunto. Se produce un ``KeyError``
cuando el conjunto se encuentra vac�o.

.. code-block:: bash

	>>> x = {"a","b","c","d","e"}
	>>> x.pop()
	'a'
	>>> x.pop()
	'c'

Usando un archivo fuente
------------------------

El int�rprete interactivo es bastante �til para hacer pruebas y entender el lenguaje, pero para el desarrollo de 
software es necesario ejecutar *scripts*. Para esto necesitamos escribir nuestro c�digo en un archivo fuente, el cual
llamaremos *script.py*. La extensi�n ``.py`` no es necesaria, pero es parte de una convenci�n.

Para editar un archivo de texto podemos utilizar cualquier aplicaci�n. En Linux, por ejemplo, podemos utilizar *vim*.

.. code-block:: bash

	$ vim script.py
	
Esto abre la interfaz del editor de texto. Para comenzar a insertar texto, presionamos la tecla "i". Para m�s informaci�n
sobre los comandos de vim, revisar la documentaci�n_ oficial.

Comenzaremos escribiendo un programa de prueba en el editor:

.. code-block:: python
	
	# -*- coding: utf-8 -*-
	import math
	
	""" De esta manera definimos los 
	comentarios multil�nea"""
	print "el valor de pi es %s" % math.pi

El caracter numeral (``#``) para insertar comentarios de una l�nea. En el caso de utilizar caracteres especiales 
dentro del archivo (como la palabra "multil�nea" que est� acentuada), se coloca un comentario en la primera l�nea
que le indica al int�rprete la codificaci�n a utilizar (utf-8).

Para salir del modo de inserci�n, guardar el archivo y salir del editor, presionamos secuencialmente: 
*Esc*, *:*, ``wq`` y *Enter*.

Para ejecutar el script, llamamos al int�rprete pas�ndole el nombre del archivo a ejecutar.

.. code-block:: bash

	$ python script.py
	el valor de pi es 3.14159265359

.. _documentaci�n: http://vimdoc.sourceforge.net/htmldoc/usr_toc.html 

Funciones
~~~~~~~~~

Las funciones en python se definen con la palabra reservada ``def``, de la siguiente manera:

.. code-block:: python

	def factorial(n):
	    if n <= 1:
	        return 1
	    else:
	        return n * factorial(n - 1)


Indentaci�n
...........

En Python la indentaci�n de bloques de c�digo es obligatoria, ya que no se utilizan las llaves (``{}``) ni ning�n
otro delimitador para determinar el comienzo y fin de los bloques. Esta es una de las caracter�sticas que garantizan
la legibilidad del c�digo. La convenci�n recomienda que en lugar del caracter de tabulaci�n, se configure el editor
para que inserte 4 espacios por indentaci�n.

Como podemos ver, tampoco se terminan las instrucciones con punto y coma ni ning�n otro caracter especial. 


Docstring
.........

Para documentar una funci�n, colocamos un comentario multil�nea al comienzo del cuerpo de una funci�n. Abriremos nuevamente
el archivo ``script.py`` y definimos la funci�n ``factorial`` con su respectiva documentaci�n.

.. code-block:: python

	# -*- coding: utf-8 -*-

	def factorial(n):
	    """
	    Definici�n recursiva de factorial
	    =================================
		
	    Retorna el factorial de un entero n
	    si n == 1 retorna 1
	    sino retorna n * fact(n-1)
	    """
	    if n <= 1:
	        return 1
	    else:
	        return n * factorial(n-1)

Si guardamos los cambios y abrimos el int�rprete interactivo (llamada a ``python`` sin argumentos), podemos importar
nuestro m�dulo (script.py):

.. code-block:: bash

	>>> import script
	
Ahora con la funci�n ``help()`` podemos revisar la documentaci�n de la funci�n factorial.

.. code-block:: bash

	>>> help(script.factorial)
	
Si queremos poder invocar ``factorial()`` sin el prefijo del m�dulo, debemos
importar la funci�n expl�citamente.

.. code-block:: bash

	>>> from script import factorial
	>>> factorial(7)
	5040
	
Estructuras de control de flujo
-------------------------------

Python cuenta con las estructuras de control de flujo usuales: if, while, for.

``if``
~~~~~~

El condicional ``if`` se utiliza como en la mayor�a de los lenguajes imperativos. Tambi�n se utiliza ``elif`` para 
encadenar condicionales.

.. code-block:: python

	def taxes(income):
	    """Calculation of taxes to be paid for a taxable income x"""
	    if income <= 8004:
	        tax = 0
	    elif income <= 13469:
	        y = (income -8004.0)/10000.0
	        tax = (912.17 * y + 1400)*y
	    elif income <= 52881:
	        z = (income -13469.0)/10000.0
	        tax = (228.74 * z +2397.0)*z +1038.0
	    elif income <= 250730:
	        tax = income * 0.42 - 8172.0
	    else:
	        tax = income * 0.44 - 15694
	    return tax 
		
``while``
~~~~~~~~~

El siguiente c�digo lee un caracter por teclado y se sale del ciclo (usando ``break``) cuando el caracter le�do es
un salto de l�nea.

.. code-block:: python

	import sys 

	text = ""
	while True:
	    c = sys.stdin.read(1)
	    text = text + c
	    if c == '\n':
	        break

	print "Input: %s" % text

Esta lectura de caracteres, sin embargo, puede efectuarse utilizando la funci�n nativa ``raw_input()``.

Una particularidad de los ciclos en python, es que pueden incluir un bloque ``else``, el cual se ejecuta si el programa
sale limpiamente (sin usar break).

.. code-block:: python

	while condition:
	    if error_occurred():
	        # manejar error
	        break    # salir del ciclo
	    handle_true()
	else:
	    # la condici�n ya es falsa, se ejecuta el siguiente bloque
	    handle_false()

``for``
~~~~~~~

El ciclo ``for`` en python, a diferencia de lenguajes como C o Java, es m�s bien una iteraci�n entre los elementos
de una secuencia (conocido en otros lenguajes como *foreach*). Tambi�n acepta opcionalmente un bloque ``else`` que
se ejecuta cuando no ocurri� un ``break`` dentro del ciclo:

.. code-block:: python

	def contiene_par(lista):
	    for n in lista:
	        if n % 2 == 0:
	            # se encontr� un n�mero par
	            return True
	else:
		# no se encontr� un n�mero par
		return False
			
Para implementar un ``for`` con un contador entero como es usual en los lenguajes imperativos, se utiliza ``range(n)``.

.. code-block:: python

	for n in range(10):
	    print n

Es posible recorrer cualquier objeto secuencial en un ciclo ``for``, incluyendo diccionarios, de la siguiente manera:

.. code-block:: python

	for key,val in dict:
	    print "dict[%s] => %s" % (key, val)


Excepciones y manejo de archivos
--------------------------------

Excepciones
~~~~~~~~~~~

Las excepciones son un elemento fundamental del lenguaje Python, y su uso es fuertemente aconsejado en 
*El Zen de Python*: "Los errores nunca deber�an pasar silenciosamente."

Otra de las filosof�as de Python es que "es mejor pedir disculpas que pedir permiso". Es decir, es recomendable asumir
que un bloque de c�digo puede generar excepciones y atajarlas, en lugar de hacer verificaciones antes de ejecutar el bloque.

Algunos ejemplos de excepciones comunes son:

* Acceder a una clave inexistente en un diccionario genera un ``KeyError``.
* Buscar el �ndice de un elemento inexistente en una lista genera un ``ValueError``
* Invocar un m�todo inexistente genera un ``AttributeError``.
* Hacer referencia a una variable inexistente genera un ``NameError``.
* Tratar de operar sobre tipos de datos mezclados sin conversi�n expl�cita genera un ``TypeError``.

Para prever y manejar excepciones, se coloca el c�digo dentro de un bloque ``try-except`` de la siguiente manera:

.. code-block:: python

	while True:
	    try:
	        n = raw_input("Introduzca un entero: ")
	        n = int(n)
	        break
	    except ValueError:
	        print("El valor introducido es inv�lido, por favor intente de nuevo")


Archivos
~~~~~~~~

Para esta secci�n, podemos intentar abrir el mismo archivo ``script.py`` sobre el cual est�bamos trabajando,
e intentemos imprimir cada una de sus l�neas en el int�rprete interactivo:

.. code-block:: bash

	>>> fobj = open("script.py", "r")
	>>> for line in fobj:
	... 	print line.rstrip()

El segundo argumento ``"r"`` indica que el archivo se est� abriendo en modo lectura.
Una vez terminamos de utilizar un archivo, es necesario cerrarlo:

.. code-block:: bash

	>>> fobj.close()

Para escribir sobre un archivo utilizamos el m�todo ``write()``. El siguiente c�digo toma el archivo ``script.py`` y 
copia cada una de las l�neas escribi�ndolas sobre otro archivo precedido del n�mero de l�nea:

.. code-block:: python

	try:
	    fobj_in = open("script.py", "r")
	    fobj_out = open("lineas.txt","w")
	    i = 1
	    for line in fobj_in:
	        print line.rstrip()
	        fobj_out.write(str(i) + ": " + line)
	        i = i + 1
	    fobj_in.close()
	    fobj_out.close()
	except IOError:
	    print "Error en manejo de archivo: %s" % IOError


Ejercicio pr�ctico
------------------

Implementar un script que lea un archivo en donde en cada l�nea habr� una cadena de bits, y escriba en un 
archivo de salida su correspondiente entero decimal en cada l�nea.