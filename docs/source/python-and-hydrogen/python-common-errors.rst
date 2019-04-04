.. _python-common-Errors:

***********************
Common Errors in Python
***********************

Syntax Errors
-------------

If you get an error when you run the code...

Attribute Error
---------------
This occurs if you call a method on the wrong type of object.

Example:

.. code-block:: python

  >>> number = 8
  >>> number.append(5)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  AttributeError: 'int' object has no attribute 'append'

Reasoning: different object types have different attributes, including functions you can perform on them. For example, lists have insert(), remove(), and sort(), etc. However, not all objects have these attributes. So if we try to access attributes on an object type that does not have these attributes, we may run into an error. Above, we use append on an integer and receive an AttributeError because integer types do not have that attribute.

What may help: calling the help() method on a type object returns what attributes are possible for that type.

.. code-block:: python

  >>> help(list)

Syntax Error
------------

Made a typo, such as:

- Forgot quotes around a string
- Forgot a colon at the end of a ``def``/``if``/``for`` line
- Different number of open and close brackets in a statement

For example:

.. code-block:: python

    whille x%2 == 0:
      print('You have entered an even number.')

Since the keyword whille is misspelled, the python interpreter will give the following error. Python often points to the first character after the actual syntax error. As seen below, the error is in the word "while", not the variable x.

.. code-block:: python

    File "filename.py", line 1
      whille x%2 == 0:
         ^
    SyntaxError: invalid syntax

Type Error
----------

- Object which you think has a value is actually None
- Used non-integer numbers in a list slice
- Called a method or function with the wrong number or type of arguments
- Used an operator on the wrong type of objects

Two examples of the last type of TypeError are shown below:

.. code-block:: python

  >>> 2 + "two"
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: unsupported operand type(s) for +:
  'int' and 'str'

Reasoning: plus operator (+) expects two numeric parameters. One parameter was the incorrect type.

.. code-block:: python

  >>> Number = 20
  >>> Number[1]
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: 'int' object is not subscriptable

Reasoning: can't access int type objects by index like with list, tuple, and string type objects.

Something that might help troubleshoot a TypeError is calling the type() function on an object.

.. code-block:: python

  >>> type("lovely")
  <type 'str'>

Indentation Error
-----------------

This happens if you use a mixture of tabs and spaces when trying to indent your lines, or if you haven't indented all lines in a block equally. Also, python is whitespace-sensitive, so you must indent lines in an if statement or a for loop to show they are in the body.

.. code-block:: python

  x = 2
  if x%2 == 0:
  print("even")

  File "<stdin>", line 2
    print("even")
        ^
  IndentationError: expected an indented block

Name Error
----------

- Misspelled variable function or method name
- Forgotten to import a module
- Forgotten to define a variable
- Uses a variable outside scope of where it's defined (See Scope in Writing Python Code)
- Code calls a function before it's defined
- Tries to print a single word and forgot the quotes

For example, try to print variable name ``hello`` in this file:

.. code-block:: python

  print hello
  NameError: global name 'hello' is not defined

Reasoning: the first part tells you what file had the error. In the example above, the file is filename.py and the error occurs on line 7. The next line shows the actual line of code where the error occurred, which executes the main() function. Then the next two lines say that the error occurred on line 5, within main, and that the line with the error is print hello. The error is that the global name 'hello' is not defined, which means that Python tried to use the variable name hello but it hasn't been defined at this point.

IO Error
--------

Tries to open a file that doesn't exist. Make sure the file in question exists and the file path is correct. The file path can be found in Folders.

Key Error
---------

Tries to look up a key that doesn't exist in a dict. One example is making this simple dictionary:

.. code-block:: python

  a_dict = {1:'Hello', 2:'World', 3:'Python'}

Try accessing the values by keys:

.. code-block:: python

  >>> a_dict[1]
  'Hello'
  >>> a_dict[4]
  Traceback (most recent call last):
    File "filename.py", line 1, in <module>
      a_dict[4]
  KeyError: 4


Reasoning: keys at index 1 and 3 exist so the respective values for those keys are displayed. Key 4 does not exist.

****************************************************
If you don't get an error while running the code...
****************************************************

If the code uses if statements:
--------------------------------

Two number which should be equal are not. For example: compare a number with a string representation of that number.

.. code-block:: python

  if 3=='3':

A complex condition is not giving the expected result. For example: the order of precedence in the condition is ambiguous, so it is important to add some parentheses. Like, in PEMDAS, if there is an addition operator before a multiplication operator, one would need some parentheses.

If the code uses loops:
-----------------------

=======================
List only has one value
=======================

For example: you defined the list inside the loop, so you should move it outside.

.. code-block:: python

  for x in newlist:
    newlist = [0, 1, 2]

If the list originally only has one value:

.. code-block:: python
  newlist = [0]
  for x in newlist:
     ## do something to the list

=======================================================
Loop that uses the range function misses the last value
=======================================================

Remember that the range function uses size, which starts at 1, but index starts at 0. For example, if you wanted to print numbers between 1 and 5, since index starts at 0, you would not be able to do range(5):

.. code-block:: python

  >>> for i in range(5):
  ...     print(i)
  0
  1
  2
  3
  4

You would have to do range(1, 6):

.. code-block:: python

  >>> for i in range(1, 6):
  ...     print(i)
  1
  2
  3
  4
  5

Also remember that for index, the last number is omitted.

If the code doesn't have for loops or if statements:
----------------------------------------------------

============================================
A variable that should have a value does not
============================================

You are storing the return value of a function which changes the variable itself:

.. code-block:: python

  def no_return(x, y):
    c = x + y

  res = no_return(4, 5)
  print(res)

None will be printed, because in the function body, there is no return statement.

A return statement is needed in the function body.

.. code-block:: python

  def empty_return(x, y):
      c = x + y
      return c

  res = return_sum(4, 5)
  print(res)
