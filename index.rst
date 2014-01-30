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

print
input
raw_input
interpretando scripts


Tipos de datos
--------------

Diccionarios
~~~~~~~~~~~~



