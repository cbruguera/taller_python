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

Una de las particularidades de Python, es la idea de que *todo es un objeto*, y esto no significa que el usuario esté obligado a adoptar
el paradigma de la Programación Orientada a Objetos al momento de programar. 

Aunque no es un concepto fácil de entender, para el intérprete de Python todas las cosas (tipos, valores, funciones, módulos...) son objetos.

En la primera clase utilizamos la función ``dir()`` para explorar los atributos del módulo ``math``, ya esto nos da una idea de que un módulo
es tratado internamente como un objeto. Si escribimos esto en el intérprete:

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

De igual manera, las funciones que definimos en nuestro programa, podemos explorarlas mediante el uso de ``dir``.
Incluso podemos explorar la misma función ``dir``. Intentémoslo en el intérprete:

.. code-block:: python

	>>> dir(dir)
	
	
...Podemos notar que realmente, hasta las funciones nativas son objetos.

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

Incluso los valores constantes como ``None``, ``True`` y ``False``, en lugar de ser palabras reservadas del lenguaje, son objetos globales.

.. code-block:: python

	>>> id(None)
	8696288
	>>> id(True)
	8696208
	>>> id(False)
	8696240

Para saber si dos nombres están asociados a un mismo objeto, se utiliza el operador ``is``. Para preguntar si un valor es distinto de nulo, 
por ejemplo, lo correcto es evaluar la expresión ``obj is not None``, en lugar de utilizar el operador de desigualdad (!=).

El siguiente experimento con listas nos explica un poco mejor la mecánica de los nombres y las asociaciones:

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

Adicionalmente, podemos probar que si modificamos el objeto asociado a ``L1``, estaremos afectando directamente a ``L2``.

.. code-block:: python

	>>> L1.append(5000)
	>>> L2
	[1, 2, 3, 5000]
	
Funciones: objetos de primer orden
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Como ya hemos mencionado, incluso las funciones son consideradas objetos para el intérprete de Python, esto significa que es posible pasar funciones
como argumentos a otras funciones:

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
	
La función ``map()`` ya viene implementada en el lenguaje Python, por ser una característica común de los lenguajes funcionales.

Es incluso factible asociar el nombre de una función a una nueva función o a algún otro valor. Para el intérprete sólo se trata de nombres 
y objetos:

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

	>>> L = [1, 2, 3]
	>>> tup = (L, L)
	>>> tup
	([1, 2, 3], [1, 2, 3])
	>>> L.remove(3)
	>>> tup
	([1, 2], [1, 2])

La tupla ``tup`` no ha mutado en sí, ya que sigue constando de los mismos objetos (L, L). Aún así, podemos afectarla indirectamente modificando
L, que por ser una lista, es un objeto mutable.


Estructura de un proyecto
-------------------------

Al momento de elaborar un proyecto de cierta complejidad, es indispensable organizar los archivos y sus dependencias de manera lógica, eficiente e
intuitiva. A pesar de que Python provee un sistema de módulos y dependencias bastante sencillo de utilizar, queda de parte del programador 
definir el proyecto con buenas prácticas de estructuración.

Módulos
~~~~~~~

Los módulos son la abstracción organizativa más básica del lenguaje, y corresponden al código que se encuentra en un archivo con la extensión ".py"
(esto no es requerido por el intérprete, pero es una convención altamente recomendable de seguir). El objetivo de un módulo es abarcar diversas 
funciones, clases y otros objetos conceptualmente relacionados, siguiendo siempre el principio básico de "alto acoplamiento, baja cohesión".

Es recomendable que los nombres de los módulos sean simples, completamente en minúscula y sin caracteres especiales de por medio.

Cuando hacemos ``import math``, por ejemplo, estamos importando el módulo ``math`` en nuestro archivo fuente. Esto no significa que el código del
módulo en cuestión es completamente copiado en nuestro código, como ocurre con algunos lenguajes. Más bien, el código del módulo se mantiene
aislado en su propio *espacio de nombres*, por lo que no es necesario preocuparnos de sobreescribir algún nombre que se encuentre definido en
el archivo actual.

.. code-block:: python

	import math
	
	def sqrt():
	    print "hello world"
	
	def raiz_cuadrada(n):
	    return math.sqrt(n)	# se especifica el espacio de nombres
		

Si queremos importar una función en particular sin necesitar del espacio de nombres, podemos hacer:

.. code-block:: python

	from math import sqrt
	
Pero hay que tener cuidado, porque en este caso sí se pueden sobreescribir los nombres definidos en el ámbito actual.

También es posible importar miembros de un módulo bajo un nombre nuevo, de la siguiente manera:

.. code-block:: python

	from math import sqrt as raiz

Adicionalmente, Python permite hacer ``from modulo import *``, lo cual importa todos los miembros de un módulo en el ambiente actual, pero esto es 
considerado una **muy** mala práctica.


Paquetes
~~~~~~~~

Python provee un sistema sencillo de empaquetado, que es simplemente una extensión del mecanismo de módulos pero para directorios. La finalidad de 
un paquete es colocar en una carpeta uno o más módulos funcionalmente relacionados.

Para que una carpeta sea considerada un paquete, debe contener un archivo ``__init__.py``. En el cual pueden definirse los objetos que serán comunes
al paquete. Es posible importar un paquete completo como espacio de nombres, como si éste fuese un módulo:

.. code-block:: python

	import paquete
	
	def mi_funcion():
	    return paquete.modulo.otra_funcion()

Al momento de hacer ``import paquete.modulo``, primero se ejecuta el ``__init__.py``, y posteriormente se ejecutan las definiciones de más alto nivel
en ``modulo.py``.

Es normal dejar en blanco el archivo ``__init__.py`` de un paquete, si no se necesitan definir nombres comunes.


Buenas prácticas de estructuración
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Renombramiento dinámico
.......................

Es recomendable evitar en la medida de lo posible el anidamiento excesivo de paquetes dentro de otros paquetes. Como está escrito en el Zen de Python:
*"Es mejor plano que anidado"*. Sin embargo, algunos niveles de complejidad hacen inevitable el anidamiento de paquetes. En este caso, al momento de
importar, podemos renombrar el módulo en cuestión, en beneficio de la legibilidad del código.

.. code-block:: python

	import paquete.otropaquete.otropaquetemas.modulo as mod
	
De esta forma evitamos escribir toda la cadena estructural al momento de acceder a dicho módulo.


Dependencia circular
....................

Si tenemos en nuestro módulo ``muebles.py`` una clase `Mesa` y ``Silla`` que importan la clase ``Carpintero`` para responder una pregunta
como ``mesa.hecha_por()``, y simultáneamente la clase ``Carpintero`` necesita importar ``Mesa`` y ``Silla`` para satisfacer un método 
``carpintero.ha_hecho()``, entonces tenemos una dependencia circular. Esto refleja un mal diseño de las entidades de nuestro proyecto,
y en este caso tendremos que recurrir a artimañas como hacer ``imports`` dentro de métodos o funciones. Esta práctica debe evitarse.

Para evitar las dependencias circulares, debemos diseñar nuestro proyecto de forma jerárquica y en capas. Esto es, agrupar en un módulo 
las funcionalidades de más bajo nivel, y sobre esa capa diseñar otro módulo con un mayor nivel de abstracción, que utilice al módulo de bajo 
nivel pero no viceversa. Las dependencias en un proyecto deberían ir hacia un único sentido, esto no sólo evita las dependencias 
circulares, sino que hace el código mucho más mantenible (bajo "acoplamiento").

Código "Espagueti"
..................

Se conoce como "código espagueti" a la práctica de programar con exceso de cláusulas anidadas y código redundante, así como llamadas de una función
a otra sin un orden coherente o intuitivo. El problema de la dependencia circular también es una forma de "código espagueti".

En términos generales, si nos tomamos en serio las proposiciones escritas en El Zen de Python, no deberíamos terminar escribiendo un código complicado.
En cualquier lenguaje es recomendable aprender a escribir de manera legible, pero en el caso de Python, la legibilidad es parte de la esencia 
del lenguaje.

PEP-8
.....

Otra referencia sobre el estilo de programación que se requiere para programar en Python es un documento conocido como el PEP-8_, en el cual
están descritas todas las convenciones básicas de legibilidad y buenas prácticas.

Leer el PEP-8 es considerado casi obligatorio para los programadores que desean aprender la forma correcta de programar en Python.

En este documento no cubriremos el alcance del PEP-8, así que recomendamos al lector revisar por sí mismo la referencia.

.. _PEP-8: http://www.python.org/dev/peps/pep-0008/


Programación Orientada a Objetos
--------------------------------

Python es un lenguaje que provee todas las características del paradigma *Orientado a Objetos*, pero sin obligar al programador a 
adoptar dicho paradigma. De hecho, la manera en la que Python maneja los módulos y los espacios de nombres, hace posible el 
encapsulamiento y la separación de capas de abstracción sin necesidad del uso de clases. Es por esto que muchos programadores de
Python suelen no recurrir a la Programación Orientada a Objetos a menos que sea absolutamente necesario. Éste es un punto
que vale la pena tomar en cuenta para desarrolladores que están acostumbrados a lenguajes como Java, por ejemplo.

Clases
~~~~~~

Las clases en Python se definen con la palabra reservada ``class``, seguida de un nombre y opcionalmente las clases de las cuales ésta
pueda heredar.

.. code-block:: python

	class MiClase:
		pass

En este caso hemos definido una clase que no define ningún miembro. Lo único que requiere una clase es un nombre. Sin embargo, en la 
práctica, una clase probablemente heredará de otras clases, y definirá una serie de atributos.

En las clases de Python, llamamos "atributos" a todos los nombres definidos en el espacio de nombres de una clase, bien sea que
éstos representen variables o métodos. Un atributo particular en las clases es el método ``__init__`` que funciona como "constructor"
al momento de instanciar dicha clase.

.. code-block:: python

	class Usuario(Persona):
	    def __init__(self, nombre, edad):
			self.nombre = nombre
			self.edad = edad

Para crear un objeto instancia de la clase ``Usuario``, invocamos a la clase directamente, como si fuese una función.

.. code-block:: python

	>>> u = Usuario("Carlos", 28)

Esto crea una instancia de Usuario, y automáticamente ejecuta el cuerpo de ``__init__()``, con los argumentos dados.

El método ``__init__``, y cualquier otro método a ser usado por las instancias de una clase, debe recibir al menos el parámetro ``self``,
el cual es una referencia a la instancia en cuestión. Adicionalmente, es posible que un método requiera de otros parámetros.

Las variables de instancia (o propiamente "atributos" como se les llama en otros lenguajes) no necesitan ser declarados, ya que una
instancia de una clase se comporta dinámicamente. Es suficiente con inicializarlos desde el ``__init__``, como en el ejemplo anterior.

Podemos comprobar que los objetos son dinámicos asignando a una instancia nuevos atributos en tiempo de ejecución:

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

Las variables declaradas explícitamente en una clase sin estar ligadas a ``self`` son consideradas atributos propios de la clase, aunque
también son accesibles desde las instancias.

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
		


Herencia
~~~~~~~~

Como muestran los ejemplos anteriores, una clase puede "heredar" los atributos de otra clase. El nombre de la clase padre debe ser
accesible en el ámbito en el que se define la clase hija. En caso de que la clase padre se encuentre definida en un módulo distinto,
se utiliza la ruta completa como argumento:

.. code-block:: python

	class ClaseHija(paquete.modulo.ClasePadre):
		pass
		
La herencia de clases, como en la mayoría de los lenguajes *OO*, hace que las instancias de las subclases tengan acceso a los atributos 
de las superclases. En caso de que la clase hija "sobrescriba" un método, no implica que esta referencia se pierda; desde la subclase es 
posible invocar explícitamente métodos de la clase padre mediante ``ClasePadre.nombre_metodo(self, argumentos)``.



isinstance()
............

issubclass()
............

Herencia múltiple
.................

Encapsulamiento
~~~~~~~~~~~~~~~

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