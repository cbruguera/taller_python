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

print
input
raw_input
interpretando scripts


Tipos de datos
--------------

Diccionarios
~~~~~~~~~~~~



