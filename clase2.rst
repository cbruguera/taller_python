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

Introducci�n
------------

En la primera clase hemos cubierto lo b�sico para entender de manera formal las particularidades del lenguaje Python, 
sin embargo, a�n no ahondamos en las �reas de mayor aplicaci�n pr�ctica del lenguaje. En esta oportunidad exploraremos
las caracter�sticas m�s avanzadas de Python. Luego de este curso el estudiante estar� en plena capacidad para 
implementar sus propios proyectos con amplitud de poder aplicativo en el mundo real.


Funciones con n�mero variable de argumentos
-------------------------------------------

Hasta ahora s�lo hemos definido funciones con una cantidad fija de par�metros, sin embargo, en Python es posible definir
funciones sin conocer de antemano el n�mero de argumentos que �sta puede recibir. Para esto se usan los par�metros 
``*args`` y ``**kwargs``

.. code-block:: python

	def prueba_args(param1, *args):
	    print "param1 = %s" % param1
	    for a in args:
	        print "otro argumento = %s" % a

En este caso, viene en ``args`` una lista de valores sin ning�n nombre asociado. Para recibir un diccionario con un n�mero 
variable de argumentos con nombres, se utiliza ``**kwargs``:

.. code-block:: python

	def prueba_kwargs(**kwargs):
	    for k in kwargs:
	        print "%s = %s" % (k, kwargs[k])

	
Modelo de ejecuci�n: Todo es un objeto
--------------------------------------

Una de las particularidades de Python, es la idea de que *todo es un objeto*, y esto no significa que el usuario est� 
obligado a adoptar el paradigma de la Programaci�n Orientada a Objetos al momento de programar. 

Aunque no es un concepto f�cil de entender, para el int�rprete de Python todas las cosas (tipos, valores, funciones, 
m�dulos...) son objetos.

En la primera clase utilizamos la funci�n ``dir()`` para explorar los atributos del m�dulo ``math``, ya esto nos da 
una idea de que un m�dulo es tratado internamente como un objeto. Si escribimos esto en el int�rprete:

.. code-block:: python
	
	>>> n = 7
	>>> dir(n)

Nos daremos cuenta de que incluso un n�mero tiene asociado una cantidad de atributos y m�todos:

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

De igual manera, las funciones que definimos en nuestro programa, podemos explorarlas mediante el uso de ``dir``.
Incluso podemos explorar la misma funci�n ``dir``. Intent�moslo en el int�rprete:

.. code-block:: python

	>>> dir(dir)
	
	
...Podemos notar que realmente, hasta las funciones nativas son objetos.

Otra cosa que podemos probar, es que si invocamos la funci�n ``dir()`` sin argumentos, esto nos devolver� una lista de 
todos los nombres definidos en el �mbito actual.
	
.. code-block:: python

	>>> dir()
	['__builtins__', '__doc__', '__name__', '__package__', 'n']

En ``__builtins__`` se encuentran definidas todas las funciones nativas y variables globales del lenguaje 
(como ``dir``, ``help``, etc).

Hagamos esta prueba:

.. code-block:: python

	>>> help(__builtins__.help)


Nombres y asociaciones
~~~~~~~~~~~~~~~~~~~~~~

En Python, es importante entender que las "variables" son s�lo nombres, los cuales est�n asociados siempre a alg�n 
objeto. Para saber el identificador del objeto al cual una variable est� asociada, utilizamos la funci�n ``id()``.

.. code-block:: python
	
	>>> n = 7
	>>> id(n)
	36031448
	>>> id(7)
	36031448
	
Como podemos ver, la variable ``n`` es un nombre asociado al objeto ``7``, y ambos se refieren al mismo objeto en 
memoria.

Incluso los valores constantes como ``None``, ``True`` y ``False``, en lugar de ser palabras reservadas del lenguaje, 
son objetos globales.

.. code-block:: python

	>>> id(None)
	8696288
	>>> id(True)
	8696208
	>>> id(False)
	8696240

Para saber si dos nombres est�n asociados a un mismo objeto, se utiliza el operador ``is``. Para preguntar si un valor 
es distinto de nulo, por ejemplo, lo correcto es evaluar la expresi�n ``obj is not None``, en lugar de utilizar el 
operador de desigualdad (!=).

El siguiente experimento con listas nos explica un poco mejor la mec�nica de los nombres y las asociaciones:

.. code-block:: python

	>>> L1 = [1, 2, 3]
	>>> L2 = L1
	>>> L3 = [1, 2, 3]
	>>> L1 is L2
	True
	>>> L1 is L3
	False
	>>> L1 == L3
	True

Adicionalmente, podemos probar que si modificamos el objeto asociado a ``L1``, estaremos afectando directamente a 
``L2``.

.. code-block:: python

	>>> L1.append(5000)
	>>> L2
	[1, 2, 3, 5000]
	

Funciones: objetos de primer orden
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Como ya hemos mencionado, incluso las funciones son consideradas objetos para el int�rprete de Python, esto significa 
que es posible pasar funciones como argumentos a otras funciones:

.. code-block:: python

	>>> def map(funcion, secuencia):
	...     r = []
	...     for e in secuencia:
	...         r.append(f(e))
	...     return r
	...
	>>> def incr(n):
	...     return n + 1
	...
	>>> map(incr, [1,2,3,4])
	[2, 3, 4, 5]
	
La funci�n ``map`` ya viene implementada en el lenguaje Python, por ser una caracter�stica com�n de los lenguajes 
funcionales.

Es incluso factible asociar el nombre de una funci�n a una nueva funci�n o a alg�n otro valor. Para el int�rprete s�lo 
se trata de nombres y objetos:

.. code-block:: python

	>>> def funcion_nula():
	...     pass
	...
	>>> funcion_nula = 42
	>>> incr = funcion_nula
	>>> incr
	42
	

Mutabilidad
~~~~~~~~~~~

Como hemos mencionado anteriormente, existen dos tipos de objetos: mutables e inmutables. Las cadenas de texto, por 
ejemplo, son inmutables:

.. code-block:: python
	
	>>> c = "hola mundo"
	>>> c[0] = "B"
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'str' object does not support item assignment

De igual manera son inmutables las tuplas y los n�meros. 

Sin embargo, podemos realizar la siguiente prueba:

.. code-block:: python

	>>> L = [1, 2, 3]
	>>> tup = (L, L)
	>>> tup
	([1, 2, 3], [1, 2, 3])
	>>> L.remove(3)
	>>> tup
	([1, 2], [1, 2])

La tupla ``tup`` no ha mutado en s�, ya que sigue constando de los mismos objetos (L, L). A�n as�, podemos afectarla 
indirectamente modificando L, que por ser una lista, es un objeto mutable.

.. getattr	??????????????????????????????????????????????????????

Estructura de un proyecto
-------------------------

Al momento de elaborar un proyecto de cierta complejidad, es indispensable organizar los archivos y sus dependencias 
de manera l�gica, eficiente e intuitiva. A pesar de que Python provee un sistema de m�dulos y dependencias bastante 
sencillo de utilizar, queda de parte del programador definir el proyecto con buenas pr�cticas de estructuraci�n.

M�dulos
~~~~~~~

Los m�dulos son la abstracci�n organizativa m�s b�sica del lenguaje, y corresponden al c�digo que se encuentra en un 
archivo con la extensi�n ".py" (esto no es requerido por el int�rprete, pero es una convenci�n altamente recomendable 
de seguir). El objetivo de un m�dulo es abarcar diversas funciones, clases y otros objetos conceptualmente 
relacionados, siguiendo siempre el principio b�sico de "alto acoplamiento, baja cohesi�n".

Es recomendable que los nombres de los m�dulos sean simples, completamente en min�scula y sin caracteres especiales 
de por medio.

Cuando hacemos ``import math``, por ejemplo, estamos importando el m�dulo ``math`` en nuestro archivo fuente. Esto no 
significa que el c�digo del m�dulo en cuesti�n es completamente copiado en nuestro c�digo, como ocurre con algunos 
lenguajes. M�s bien, el c�digo del m�dulo se mantiene aislado en su propio *espacio de nombres*, por lo que no es 
necesario preocuparnos de sobreescribir alg�n nombre que se encuentre definido en el archivo actual.

.. code-block:: python

	import math
	
	def sqrt():
	    print "hello world"
	
	def raiz_cuadrada(n):
	    return math.sqrt(n)	# se especifica el espacio de nombres
		

Si queremos importar una funci�n en particular sin necesitar del espacio de nombres, podemos hacer:

.. code-block:: python

	from math import sqrt
	
Pero hay que tener cuidado, porque en este caso s� se pueden sobreescribir los nombres definidos en el �mbito actual.

Tambi�n es posible importar miembros de un m�dulo bajo un nombre nuevo, de la siguiente manera:

.. code-block:: python

	from math import sqrt as raiz

Adicionalmente, Python permite hacer ``from modulo import *``, lo cual importa todos los miembros de un m�dulo en el 
ambiente actual, pero esto es considerado una **muy** mala pr�ctica.


Paquetes
~~~~~~~~

Python provee un sistema sencillo de empaquetado, que es simplemente una extensi�n del mecanismo de m�dulos pero para 
directorios. La finalidad de un paquete es colocar en una carpeta uno o m�s m�dulos funcionalmente relacionados.

Para que una carpeta sea considerada un paquete, debe contener un archivo ``__init__.py``. En el cual pueden definirse 
los objetos que ser�n comunes al paquete. Es posible importar un paquete completo como espacio de nombres, como si 
�ste fuese un m�dulo:

.. code-block:: python

	import paquete
	
	def mi_funcion():
	    return paquete.modulo.otra_funcion()

Al momento de hacer ``import paquete.modulo``, primero se ejecuta el ``__init__.py``, y posteriormente se ejecutan las 
definiciones de m�s alto nivel en ``modulo.py``.

Es normal dejar en blanco el archivo ``__init__.py`` de un paquete, si no se necesitan definir nombres comunes.


Buenas pr�cticas
~~~~~~~~~~~~~~~~

Renombramiento din�mico
.......................

Es recomendable evitar en la medida de lo posible el anidamiento excesivo de paquetes dentro de otros paquetes. Como 
est� escrito en el Zen de Python: *"Es mejor plano que anidado"*. Sin embargo, algunos niveles de complejidad hacen 
inevitable el anidamiento de paquetes. En este caso, al momento de importar, podemos renombrar el m�dulo en cuesti�n, 
en beneficio de la legibilidad del c�digo.

.. code-block:: python

	import paquete.otropaquete.otropaquetemas.modulo as mod
	
De esta forma evitamos escribir toda la cadena estructural al momento de acceder a dicho m�dulo.


Evitar la dependencia circular
..............................

Si tenemos en nuestro m�dulo ``muebles.py`` una clase `Mesa` y ``Silla`` que importan la clase ``Carpintero`` para 
responder una pregunta como ``mesa.hecha_por()``, y simult�neamente la clase ``Carpintero`` necesita importar ``Mesa`` 
y ``Silla`` para satisfacer un m�todo ``carpintero.ha_fabricado()``, entonces tenemos una dependencia circular. Esto 
refleja un mal dise�o de las entidades de nuestro proyecto, y en este caso tendremos que recurrir a artima�as como 
hacer "imports" dentro de m�todos o funciones. Esta pr�ctica debe evitarse.

Para evitar las dependencias circulares, debemos dise�ar nuestro proyecto de forma jer�rquica y en capas. Esto es, 
agrupar en un m�dulo las funcionalidades de m�s bajo nivel, y sobre esa capa dise�ar otro m�dulo con un mayor nivel de 
abstracci�n, que utilice al m�dulo de bajo nivel pero no viceversa. Las dependencias en un proyecto deber�an ir hacia 
un �nico sentido, esto no s�lo evita las dependencias circulares, sino que hace el c�digo mucho m�s mantenible (bajo 
"acoplamiento").

Evitar el c�digo "Espagueti"
............................

Se conoce como "c�digo espagueti" a la pr�ctica de programar con exceso de cl�usulas anidadas y c�digo redundante, as� 
como llamadas de una funci�n a otra sin un orden coherente o intuitivo. El problema de la dependencia circular tambi�n 
es una forma de "c�digo espagueti".

En t�rminos generales, si nos tomamos en serio las proposiciones escritas en El Zen de Python, no deber�amos terminar 
escribiendo un c�digo complicado. En cualquier lenguaje es recomendable aprender a escribir de manera legible, pero en 
el caso de Python, la legibilidad es parte de la esencia del lenguaje.

PEP-8
.....

Otra referencia sobre el estilo de programaci�n que se requiere para programar en Python es un documento conocido como 
el PEP-8_, en el cual est�n descritas todas las convenciones b�sicas de legibilidad y buenas pr�cticas.

Leer el PEP-8 es considerado casi obligatorio para los programadores que desean aprender la forma correcta de 
programar en Python.

En este documento no cubriremos el alcance del PEP-8, as� que recomendamos al lector revisar por s� mismo la 
referencia.

.. _PEP-8: http://www.python.org/dev/peps/pep-0008/


Programaci�n Orientada a Objetos
--------------------------------

Python es un lenguaje que provee todas las caracter�sticas del paradigma *Orientado a Objetos*, pero sin obligar al 
programador a adoptar dicho paradigma. De hecho, la manera en la que Python maneja los m�dulos y los espacios de 
nombres, hace posible el encapsulamiento y la separaci�n de capas de abstracci�n sin necesidad del uso de clases. Es 
por esto que muchos programadores de Python suelen no recurrir a la Programaci�n Orientada a Objetos a menos que sea 
absolutamente necesario. �ste es un punto que vale la pena tomar en cuenta para desarrolladores que est�n 
acostumbrados a lenguajes como *Java*, por ejemplo.

Clases
~~~~~~

Las clases en Python se definen con la palabra reservada ``class``, seguida de un nombre y opcionalmente las clases de 
las cuales �sta pueda heredar.

.. code-block:: python

	class MiClase:
	    pass

En este caso hemos definido una clase que no define ning�n miembro. Lo �nico que requiere una clase es un nombre. 
Sin embargo, en la pr�ctica, una clase probablemente heredar� de otras clases, y definir� una serie de atributos.

Si una clase no hereda de alguna otra clase conocida, es recomendable definirla al menos como una subclase de 
``object``.

Herencia
~~~~~~~~

Como es com�n en los lenguajes Orientados a Objetos, una clase puede "heredar" los atributos y m�todos de otra clase. 
El nombre de la clase "padre" debe ser accesible en el �mbito en el que se define la clase hija. En caso de que la 
clase padre se encuentre definida en un m�dulo distinto, se utiliza la ruta completa como argumento:

.. code-block:: python

	class ClaseHija(paquete.modulo.ClasePadre):
	    pass
		

La herencia de clases, como en la mayor�a de los lenguajes *OO*, hace que las instancias de las subclases tengan 
acceso a los atributos de las superclases. En caso de que la clase hija "sobrescriba" un m�todo, no implica que esta 
referencia se pierda; desde la subclase es posible invocar expl�citamente m�todos de la clase padre mediante la
funci�n ``super``, utilizando la siguiente sintaxis:

.. code-block:: python

	super(ClaseHija, self).metodoPadre(argumentos)



isinstance()
............

Para revisar que un objeto pertenezca a una clase dada, podemos utilizar la funciones ``isinstance()``:

.. code-block:: python

	>>> isinstance(c, Contador)
	True
	>>> isinstance(7, int)
	True

	
issubclass()
............

``issubclass()`` se utiliza para saber si una clase hereda de otra:

.. code-block:: python

	>>> class ContadorEspecial(Contador):
	...     pass
	...
	>>> issubclass(ContadorEspecial, Contador)
	True

	
Herencia m�ltiple
.................

En Python es posible heredar de m�s de una clase. Para esto, sencillamente se escriben los nombres de las clases base
como argumentos de la clase actual, separados por coma.

.. code-block:: python

	class MiClase(ClaseBase1, ClaseBase2, ClaseBase2):
		pass
		
Al momento de resolver la ubicaci�n de un nombre, el int�rprete primero busca en el �mbito local (MiClase), luego
busca la definici�n en ClaseBase1, luego ClaseBase2 y as� sucesivamente.


Constructor
~~~~~~~~~~~

En las clases de Python, llamamos "atributos" a todos los nombres definidos en el espacio de nombres de una clase, 
bien sea que �stos representen variables o m�todos. Un atributo particular en las clases es el m�todo ``__init__``, 
que funciona como una especie de "constructor" al momento de instanciar dicha clase. 

T�cnicamente, ``__init__`` no es un constructor, ya que la instancia ya se encuentra construida cuando este m�todo se 
ejecuta. Adem�s, no es obligatorio que una clase defina un m�todo ``__init__``. En caso de definirse, �ste se utiliza
para inicializar todos los atributos necesarios de una instancia.

.. code-block:: python

	class Usuario(Persona):
	    def __init__(self, nombre, edad):
			self.nombre = nombre
			self.edad = edad

Para crear un objeto instancia de la clase ``Usuario``, invocamos a la clase directamente, como si fuese una funci�n.

.. code-block:: python

	>>> u = Usuario("Carlos", 28)

Esto crea una instancia de ``Usuario``, y autom�ticamente ejecuta el cuerpo de ``__init__``, con los argumentos 
dados.

El m�todo ``__init__``, y cualquier otro m�todo a ser usado por las instancias de una clase, debe recibir al menos el 
par�metro ``self``, el cual es una referencia a la instancia en cuesti�n. Adicionalmente, es posible que un m�todo 
requiera de otros par�metros.

Las variables de instancia (o propiamente "atributos" como se les llama en otros lenguajes) no necesitan ser 
declarados, ya que una instancia de una clase se comporta din�micamente. Es suficiente con inicializarlos desde el 
``__init__``, como en el ejemplo anterior.

Podemos comprobar que los objetos son din�micos asignando a una instancia nuevos atributos en tiempo de ejecuci�n:

.. code-block:: python
	
	>>> u = Usuario("John", 42)
	>>> u.edad
	42
	u.direccion
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	AttributeError: Usuario instance has no attribute 'direccion'
	>>> u.direccion = "Chacao"
	>>> u.direccion
	'Chacao'
	

Destructor
~~~~~~~~~~

Lo mismo aplica para la destrucci�n de instancias en Python, no existe realmente un "destructor", pero contamos con
un m�todo similar a un destructor: ``__del__``.

``__del__`` es un m�todo que se ejecuta cuando un objeto est� apunto de eliminarse mediante una llamada a del().

.. code-block:: python

	class Saludo:
	    def __init__(self, nombre):
	        self.nombre = nombre
	    
		def __del__(self):
	        print "Adios!..."
	    
		def decir_hola(self):
	        print "Hola %s!" % self.nombre


Intentemos instanciar y destruir un objeto de la clase ``Saludo``:

..code-block:: python

	>>> s = Saludo("Bob")
	>>> s.decir_hola()
	'Hola Bob!'
	>>> del s
	'Adios!...'

.. super() ???????????????????????????????????????????????????????????????????


Atributos de clase
~~~~~~~~~~~~~~~~~~

Las variables declaradas expl�citamente en una clase sin estar ligadas a ``self`` son consideradas atributos propios 
de la clase, aunque tambi�n son accesibles desde las instancias.

.. code-block:: python

	class MiClase():
	    MAX_VALUE = 5000	# se puede utilizar para declarar constantes
		
.. code-block:: python

	>>> MiClase.MAX_VALUE
	5000
	>>> obj = MiClase()
	>>> obj.MAX_VALUE
	5000
	>>> obj.MAX_VALUE = "cadena"
	>>> obj.MAX_VALUE
	'cadena'
	>>> MiClase.MAX_VALUE
	5000
		

Es posible para una instancia modificar el valor de un atributo de la clase:

.. code-block:: python

	>>> class Contador():
	...     cont = 0
	...     def __init__(self):
	...         self.__class__.cont += 1
	...
	>>> Contador.cont
	0
	>>> c = Contador()
	>>> Contador.cont
	1
	>>> d = Contador()
	>>> Contador.cont
	2
	>>> c.cont
	2

Podemos notar que en el c�digo anterior se utiliza el atributo ``__class__``, el cual es una referencia a la clase
de la instancia actual. Las clases *tambi�n* son objetos.


Encapsulamiento
~~~~~~~~~~~~~~~

En Python no existe un mecanismo como tal para el encapsulamiento de atributos. Esto es posible mediante convenciones
de nombramiento. Por lo general, cualquier nombre precedido por un gui�n bajo o *underscore* (_) se considera un
atributo no p�blico (o lo que en muchos lenguajes se conoce como atributos "protegidos"), y todo atributo precedido por
doble gui�n bajo (__) es considerado privado. El correcto uso del encapsulamiento en Python, queda de parte de las 
pr�cticas concientes del programador.

.. code-block:: python

	class Encapsulamiento(object):
	    def __init__(self, a, b, c):
	        self.publico = a
	        self._protegido = b
	        self.__privado = c

De igual manera, no es una costumbre frecuente definir "getters" y "setters" por cada atributo de una clase. Es 
considerado completamente normal el acceso a los atributos directamente, en beneficio de la legibilidad.

M�dulos nativos
---------------

Una de las filosof�as de Python, es que es un lenguaje "con bater�as incluidas", esto quiere decir que sin necesidad
de instalar paquetes externos, ya el lenguaje provee una gama de funcionalidades de alta utilidad en diversas �reas.

A continuaci�n exploraremos algunos de los m�dulos nativos principales. La lista de m�dulos provistos por la 
biblioteca est�ndar de Python es extensa, para ver la lista y la documentaci�n completa de los m�dulos se recomienda
revisar este enlace_.

.. _enlace: http://docs.python.org/2/library/
 

datetime / time
~~~~~~~~~~~~~~~

El m�dulo ``datetime`` provee clases para manipular fechas y horas de diferentes maneras, incluyendo soporte para
aritm�tica de fechas y horas, entre otras cosas.

.. code-block:: python

	>>> import time
	>>> from datetime import date
	>>> hoy = date.today()
	>>> hoy
	datetime.date(2007, 12, 5)
	>>> mi_cumple = date(hoy.year, 6, 24)
	>>> if mi_cumple < hoy:
	...     mi_cumple = mi_cumple.replace(year=hoy.year + 1)
	>>> mi_cumple
	datetime.date(2008, 6, 24)
	>>> tiempo_hasta_cumple = abs(mi_cumple - hoy)
	>>> print "Quedan %s d�as para mi cumplea�os" % tiempo_hasta_cumple.days
	'Quedan 202 d�as para mi cumplea�os'


os
~~

El m�dulo ``os`` provee funcionalidades referentes al sistema operativo, como exploraci�n y manipulaci�n de rutas en
el sistema de archivos, y manejo de procesos.

.. code-block:: python

	import os
	for root, dirs, files in os.walk(top, topdown=False):
	    for name in files:
	        os.remove(os.path.join(root, name))
	    for name in dirs:
	        os.rmdir(os.path.join(root, name))
			
El c�digo anterior, elimina todos los archivos y subdirectorios desde el �mbito de ``topdown``. Esto es sumamente 
peligroso!


json
~~~~

Este m�dulo permite la codificaci�n de estructuras de Python en formato JSON (*Javascript Object Notation*)

.. code-block:: python

	>>> import json
	>>> L = ['foo', {'bar': ('baz', None, 1.0, 2)}]
	>>> json.dumps(L)
	'["foo", {"bar": ["baz", null, 1.0, 2]}]'
	

random
~~~~~~

En el m�dulo ``random`` est�n implementadas varias funcionalidades concernientes a generaci�n de aleatoriedad.

.. code-block:: python

	>>> import random
	>>> random.randrange(100)
	72
	>>> random.randrange(100)
	7
	>>> random.randrange(100)
	40
	
Podemos incluso aleatorizar el orden de una lista:

.. code-block:: python

	>>> L = range(10)
	>>> L
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	>>> random.shuffle(L)
	[1, 4, 3, 0, 7, 5, 6, 9, 2, 8]
		
	
Decoradores
-----------

El lenguaje Python provee un sintaxis simple pero bastante poderosa llamada "decoradores". Un decorador no es m�s que 
una funci�n o una clase que envuelve (o decora) otra funci�n o m�todo. La funci�n decorada reemplaza la funci�n 
original. Esto es posible debido a que en Python las funciones son objetos de primer orden. La sintaxis de los 
decoradores la siguiente:

.. code-block:: python

	def mi_decorador(func)
	    # manipular func
	    return func

	@mi_decorador
	def funcion():
	    # Hacer algo
	# funcion() ha sido decorada

Este mecanismo es �til para separar comportamientos que son ajenos a la l�gica de la funci�n como tal, 

Una funci�n puede ser objeto de m�s de un decorador:

.. code-block:: python

	@decorador3
	@decorador2
	@decorador1
	def function():
	    # Hacer algo
	    pass

En este caso, el orden de aplicaci�n es desde abajo hacia arriba, comenzando por ``@decorador1``.

Un decorador puede implementarse como una funci�n, o como una clase siempre y cuando �sta implemente el m�todo 
``__call__``.

Un ejemplo pr�ctico puede ser implementar un decorador que funcione como *cache* de los resultados de una funci�n.
De esta manera, si una funci�n se invoca m�s de una vez con los mismo argumentos, los resultados ya se encuentran 
guardados en memoria.

.. code-block:: python

	class cached(object):
	    def __init__(self, func):
	        self.func = func
	        self.cache = {}
			
	    def __call__(self, *args):
	        if args in self.cache:
	            return self.cache[args]
	        else:
	            value = self.func(*args)
	            self.cache[args] = value
	            return value
  
	@cached
	def fibonacci(n):
	    if n in (0, 1):
	        return n
	    return fibonacci(n-1) + fibonacci(n-2)

   
Iterables e iteradores
----------------------

Hemos visto anteriormente que en los ciclos ``for`` somos capaces de recorrer cierto tipo de objetos, como las listas
o las cadenas. Esto es posible porque se trata de objetos *iterables*.

Para que un objeto sea iterable, �ste debe implementar el m�todo ``__iter__``, el cual retorna un tipo de objeto 
llamado *iterador*. 

Un *iterador* es un objeto que cumple con dos caracter�sticas:

* Implementa el m�todo ``__iter__``, en el cual se retorna a s� mismo.
* Implementa el m�todo ``next``, el cual se encarga de retornar el pr�ximo elemento de la colecci�n cada vez que es invocado. En el caso de no haber m�s pr�ximos elementos, �ste levanta una excepci�n del tipo ``StopIteration``.


Cuando utilizamos un objeto secuencial en un ``for``, en realidad el int�rprete est� obteniendo un iterador del objeto 
que queremos recorrer.

Consideremos una lista L, esta lista es un *iterable*, mas ella misma no es un iterador:

.. code-block:: python

	>>> a = [1, 2, 3, 4]
	>>> a.__iter__
	<method-wrapper '__iter__' of list object at 0x014E5D78>
	>>> it = a.__iter__()
	>>> it
	<listiterator object at 0x011E3DF0>

Si quisi�ramos implementar una clase que sea iterable, debemos implementar el protocolo descrito anteriormente:

.. code-block:: python

	import random

	class MiLista(list):
	    def __iter__(self):
	        return MiRandomIter(self)
		
	class MiRandomIter(object):
	    def __init__(self, lst):
	        self.lst = lst
	        self.indexes = range(len(lst))
	        random.shuffle(self.indexes)
	        self.i = 0

	    def __iter__(self):
	        return self

	    def next(self):
	        if self.i < len(self.lst):
	            self.i += 1         
	            return self.lst[self.indexes[self.i - 1]]
	        else:
	            raise StopIteration


Originalmente, son iterables las cadenas de texto y todas las colecciones nativas del lenguaje (listas, tuplas, 
conjuntos y diccionarios). Un n�mero entero, por ejemplo, no es iterable.

.. code-block:: python

	>>> n = 50
	>>> for i in n:
	...     print i
	...
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'int' object is not iterable


**Ejercicio pr�ctico:** implementar un tipo de entero que sea iterable, y que vaya retornando cada vez el siguiente entero
m�s cercano a cero.

Generadores
~~~~~~~~~~~

Un generador es un tipo de iterador especial, que se utiliza para generar ciertas secuencias. Para entender generadores
es necesario entender primero la instrucci�n ``yield``. 

``yield`` es una instrucci�n que puede utilizarse �nicamente dentro de una funci�n, y act�a de manera similar a 
``return``, s�lo que en este caso la funci�n retorna un *generador*, y conserva el estado de ejecuci�n de dicha funci�n.

Veamos el siguiente ejemplo:

.. code-block:: python

	>>> def uno_dos_tres():
	...     yield 1
	...     yield 2
	...     yield 3
	...
	>>> uno_dos_tres()
	<generator object uno_dos_tres at 0x014E5D78>

Ahora intentemos recorrer ``uno_dos_tres()`` con un ciclo ``for``. �Qu� sucede?...

La instrucci�n ``yield`` permite retornar progresivamente valores sin necesidad de ejecutar el c�digo completo de la 
funci�n que los genera. Esto es de bastante utilidad cuando queremos trabajar con secuencias muy grandes o incluso
infinitas.

Podemos implementar, por ejemplo, una funci�n que sea capaz de generar la secuencia fibonacci:

.. code-block:: python

	>>> def fib():
	...     a, b = 0, 1
	...     while True:
	...         yield a
	...         a, b = b, a + b
	...
	>>> cont = 0
	>>> for i in fib():
	...     print i
	...     if cont > 10:
	...         break
	...
	
Tambi�n podemos utilizar el m�dulo ``itertools`` para operar sobre iteradores y generadores:

.. code-block:: python
	
	>>> import itertools
	>>> list(itertools.islice(fib(), 10))
	[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
	
Existe tambi�n ``xrange``, que es una versi�n de ``range`` que funciona como un generador.

.. code-block:: python

	>>> for i in xrange(10):
	...     print i
		

.. Instalaci�n de bibliotecas con pip
.. ----------------------------------

