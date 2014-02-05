.. Taller de Python documentation master file, created by
   sphinx-quickstart on Mon Jan 27 16:38:42 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

	
.. image:: _static/logo_posma.png
   :align: center
   
===============
Python: Nivel 2
===============

.. contents:: Contenido
   :depth: 2

Introducción
------------

En la primera clase hemos cubierto lo básico para entender de manera formal las particularidades del lenguaje Python, sin embargo,
aún no ahondamos en las áreas de mayor aplicación práctica del lenguaje. En esta oportunidad exploraremos las características más
avanzadas de Python. Luego de este curso el estudiante estará en plena capacidad para implementar sus propios proyectos con amplitud
de poder aplicativo en el mundo real.

Modelo de ejecución: Todo es un objeto
----------------------------------------

Una de las particularidades de Python, es la idea de que *todo es un objeto*. Esto no significa que estemos hablando necesariamente de 
Programación Orientada a Objetos, o que todo el código que el usuario escribe esté encapsulado dentro de una clase (como en Java). 
Aunque no es un concepto fácil de entender, en Python todas las cosas (tipos, valores, funciones, módulos...) son objetos.

En la primera clase utilizamos la función ``dir()`` para explorar los atributos del módulo ``math``, ya esto nos da una idea de que un módulo
(o para fines prácticos, cualquier archivo ``.py`` es tratado internamente como un objeto. Incluso si escribimos esto en el intérprete:

.. code-block:: python
	
	>>> n = 7
	>>> dir(n)

Nos daremos cuenta de que incluso un número tiene asociado una cantidad de atributos y métodos:

.. code-block:: python

	['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', 
	'__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', 
	'__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', 
	'__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', 
	'__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', 
	'__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', 
	'__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', 
	'__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', 
	'__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 
	'__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']

De igual manera las funciones que definimos en nuestro programa, podemos explorarlas mediante la función ``dir``.
Incluso podemos explorar la misma función ``dir``! Intentémoslo en el intérprete:

.. code-block:: python

	>>> dir(dir)
	
	
...Y notaremos que realmente, hasta las funciones nativas son objetos.

Otra cosa que podemos probar, es que si invocamos la función ``dir()`` sin argumentos, esto nos devolverá una lista de todos los
nombres definidos en el ámbito actual.
	
.. code-block:: python

	>>> dir()
	['__builtins__', '__doc__', '__name__', '__package__', 'n']

En el módulo ``__builtins__`` se encuentran definidas todas las funciones nativas y variables globales del lenguaje (como ``dir``, ``help``, etc).
Hagamos esta prueba:

.. code-block:: python

	>>> help(__builtins__.help)

Nombres y asociaciones
~~~~~~~~~~~~~~~~~~~~~~

En Python, es importante entender que las "variables" son sólo nombres, los cuales están asociados siempre a algún objeto. 
Para saber el identificador del objeto al cual una variable está asociada, utilizamos la función ``id()``.

.. code-block:: python
	
	>>> n = 7
	>>> id(n)
	36031448
	>>> id(7)
	36031448
	
Como podemos ver, la variable ``n`` es un nombre asociado al objeto ``7``, y ambos se refieren al mismo objeto en memoria.

Incluso los valores constantes como ``None``, ``True`` y ``False``, en lugar de ser palabras reservadas del lenguaje, son objetos.

.. code-block:: python

	>>> id(None)
	8696288
	>>> id(True)
	8696208
	>>> id(False)
	8696240

Para saber si dos nombres están asociados a un mismo objeto, se utiliza el operador ``is``. Por eso, para preguntar si un valor es nulo, 
lo correcto evaluar la expresión ``obj is None``, en lugar de utilizar la comparación aritmética (==).

El siguiente experimento con listas nos explica un poco mejor el asunto de los nombres y las asociaciones:

.. code-block:: python

	>>> L1 = [1,2,3]
	>>> L2 = L1
	>>> L3 = [1,2,3]
	>>> L1 is L2
	True
	>>> L1 is L3
	False
	>>> L1 == L3
	True

Adicionalmente, podemos probar que si modificamos el objeto asociado a ``L1``, estaremos afectando directamente a ``L2``.

.. code-block:: python

	>>> L1.append(5000)
	>>> L2
	[1, 2, 3, 5000]

Mutabilidad
~~~~~~~~~~~

Como hemos mencionado anteriormente, existen dos tipos de objetos: mutables e inmutables. Las cadenas de texto, por ejemplo, son inmutables:

.. code-block:: python
	
	>>> c = "hola mundo"
	>>> c[0] = "B"
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'str' object does not support item assignment

De igual manera son inmutables las tuplas y los números. 

Sin embargo, podemos realizar la siguiente prueba:

.. code-block:: python

	>>> tup = (L3, L3)
	>>> tup
	([1, 2, 3], [1, 2, 3])
	>>> L3.remove(3)
	>>> tup
	([1, 2], [1, 2])

La tupla ``tup`` no ha cambiado en sí, ya que sigue constando de los mismos objetos (L3, L3). Aún así, podemos afectarla indirectamente modificando
L3, que por ser una lista, es un objeto mutable.


Estructura de un proyecto
-------------------------

Módulos
~~~~~~~

Paquetes
~~~~~~~~

.. Buenas prácticas de estructuración
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Programación Orientada a Objetos
--------------------------------

Módulos nativos
---------------

os, sys...
~~~~~~~~~~


json
~~~~

Decoradores
-----------

Iteradores y generadores
------------------------

Instalación de paquetes con pip / virtualenv
--------------------------------------------

Pruebas unitarias
-----------------