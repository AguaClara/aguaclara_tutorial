.. _python-common-errors:

***********************
Common Errors in Python
***********************

Syntax Error
------------

A **syntax error** is an error in the syntax of a command, much like a typo. Python will refuse to even attempt compiling (preparing to run) code that contains syntax errors.

Some common syntax errors are:

- Missing colon at the end of a ``def``, ``if``, or ``for`` statement
- Missing quotation marks, either both single (``''``) or both double (``""``), around a string
- Different number of open and closed brackets in a statement

For example:

.. code-block:: python

    whille x % 2 == 0:
      print('You have entered an even number.')

Since the keyword ``whille`` is misspelled, the Python interpreter will give the following error. Python often points to the first character after the actual syntax error. As seen below, the error is in the ``whille``, not the variable ``x``.

.. code-block:: python

    File "filename.py", line 1
      whille x % 2 == 0:
             ^
      SyntaxError: invalid syntax

Attribute Error
---------------
In Python, all values are *objects* with associated data types, attributes, and functions. These attributes and functions can be accessed or assigned with the dot (``.``) operator. An **attribute error** occurs if we try to access or assign an attribute that a particular value doesn't have.

For instance, suppose the variable ``t`` represents a triangle that has attributes ``base`` and ``height``. To calculate the triangle's area, we could write ``t.base * t.height / 2``, where the ``.`` allows us to access ``t``'s predefined attributes. Similarly, if ``t`` has a function called ``scale(factor)`` to scale its base and height by a given factor, we could double its base and height by writing ``t.scale(2)``.

Below is a common mistake:

.. code-block:: python

    # Importing u for its unit attributes
    from aguaclara.core.units import u
    flow_rate = 10 * u.meter**3 / u.second
    area = 5 * u.meter**2
    # Naming another variable u
    u = flow_rate/area
    # Trying to use u again for units
    time = 20 * u.second

The last line of code gives two errors:

.. code-block:: python

    AttributeError: 'float' object has no attribute 'second'
    AttributeError: Neither Quantity object nor its magnitude (2.0) has attribute 'second'

In the second line of code, we could use ``u.second`` because ``u`` (a unit registry object) contained an attribute representing seconds. However, after reassigning ``u`` to another value, the variable name now refers to a float (number) or Quantity object (number associated with units), which do not have the same attributes as the unit registry object.

Other attribute errors may arise from misspelling attribute or function names or calling functions that belong to similar but distinct data types (e.g. NumPy arrays and lists). Calling the ``help()`` method on a data type or searching an online API reference can show you what attributes actually belong to that type.

.. code-block:: python

  >>> help(list)

Type Error
----------

A type error arises from applying an operation or function to a value of an inappropriate type. This can occur when

- Working with an object or variable whose value is None
- Using non-integer values to index a list
- Calling a function using the wrong number or type of inputs
- Using an operator on the wrong type(s) of value(s)

Some examples are shown below:

.. code-block:: python

  def sum(x, y):
    z = x + y

  sum(3, 4)/2

  TypeError: unsupported operand type(s) for /: 'NoneType' and 'int'

Any function **without a return statement** will output a value of type None. This problem could be solved by adding the line ``return z`` at the end of the ``sum()`` function.

.. code-block:: python

  x = 20
  x[1]

  TypeError: 'int' object is not subscriptable

The ``[]`` operator can only be called on objects that are "subscriptable", meaning they are containers for other objects. Elements in lists, tuples, dictionaries, and strings can be accessed using this operator, but an integer is not compatible.

.. code-block:: python

    x = 3(1+4)

    TypeError: 'int' object is not callable

Unlike in math, multiplication in Python must *always* be represented with the ``*`` operator. If you accidentally use parentheses for multiplication, Python will interpret the value preceding the parentheses a function and tell you the object is not "callable", i.e. it is not a function.

One tip for troubleshooting a TypeError is to call the ``type()`` function on an object.

.. code-block:: python

  type("lovely")

  <type 'str'>

Indentation Error
-----------------

This happens if you use a mixture of tabs and spaces when trying to indent your lines, or if you haven't indented all lines in a block equally. Also, Python is whitespace-sensitive, so all lines in the body of an ``if`` statement or a ``for`` must be indented.

.. code-block:: python

  x = 2
  if x % 2 == 0:
  print("even")

  IndentationError: expected an indented block

Name Error
----------
A name error occurs when a local or global variable, function, or module name is not found. This can occur due to

- Misspelling a variable or function name
- Using an un-imported module
- Using an undefined variable
- Using a variable outside the scope it is defined in
- Calling a function before it is defined

For example, if instead of ``print("hello")``, we forget the quotation marks for a string and write the following, we get a name error:

.. code-block:: python

  print(hello)

  NameError: name 'hello' is not defined

Since ``hello`` is not a string, Python looks for a variable of that name, but it has not been defined at this point.

IO Error
--------

An IO error occurs from trying to open or write to a file that does not exist. Make sure the file in question exists and the file path is correct. The file path can be found in Folders, File Manager, or Finder.

Key Error
---------

A Key Error arises from looking up a nonexistent key in a Python dictionary. For example:

.. code-block:: python

  a_dict = {1:'Hello', 2:'World', 3:'Python'}
  a_dict[1]
  a_dict[4]

  'Hello'
  KeyError: 4


A key of ``1`` exists, so its associated values is displayed. A key of ``4`` does not exist.
