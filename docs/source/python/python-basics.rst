.. _python-basics:

*************
Python Basics
*************

**NOTE: This is not a comprehensive guide to writing Python code!** We've only put the basics that would be useful in the context of an AguaClara research report. To continue learning Python, review these :ref:`python-and-hydrogen-introduction-external-resources`.

How this tutorial works
-----------------------

Some code examples will look like this:

.. code-block:: python

   >>> print('Hydrate or diedrate')
   Hydrate or diedrate

The triple greater-than symbols ``>>>`` indicate that that line of Python code is being run in the **interactive Python interpreter** in the command line. The next line is what that line of Python code would output.

The **interactive Python interpreter** will be explained later on.

Basic Operations
================

Printing
--------

.. code-block:: python

   >>> print('You can keep strings in single quotes,')
   You can keep strings in single quotes,
   >>> print("or double quotes!")
   or double quotes!

Comments
--------

.. code-block:: python

   print('This code will run,') # but this will not.

   """
   Here's a
   block comment!
   """

Math
----

.. code-block:: python

   >>> 5 + 2
   7
   >>> 5 - 2
   3
   >>> 5 * 2
   10
   >>> 5 / 2 # Dividing integers will round floats (decimals) down.
   2
   >>> 5.0 / 2.0 # Dividing floats will return floats.
   2.5
   >>> 5 ** 2 # Exponentiation
   25
   >>> 5 % 2 # Modulo
   1
   >>> (5 + 2) * 5 + 2 # PEMDAS
   37

Logic
-----

.. code-block:: python

   >>> True and False # Note that all of these words are case-sensitive.
   False
   >>> False or True
   True
   # Visit here for more on and/or: https://bit.ly/2vA64pM

   >>> 5 == 5
   True
   >>> 5 == 2
   False

   >>> 5 != 5
   False
   >>> 5 != 2
   True

   >>> 5 > 2
   True
   >>> 5 < 2
   False
   >>> 5 <= 5
   True
   >>> 5 >= 5
   True

Data Structures
===============

Variables
---------

.. code-block:: python

   >>> a_variable = 'can store a string'
   >>> an_integer = 5
   >>> a_float = 2.0
   >>> a_boolean = True

   >>> an_integer + a_float
   7.0

Lists
-----

.. code-block:: python

   >>> a_list = ['can store anything!', 5, 2.0, True]

   >>> a_list
   ['can store anything!', 5, 2.0, True]
   >>> a_list[0]
   can store anything!
   >>> a_list[3]
   True

   >>> a_list.append('add an entry to the end')
   >>> a_list
   ['can store anything!', 5, 2.0, True, 'add an entry to the end']

   >>> a_list.pop() # remove an entry from the end
   >>> a_list
   ['can store anything!', 5, 2.0, True]

   >>> a_list[0] = 'change an entry'
   >>> a_list
   ['change an entry', 5, 2.0, True]

Dictionaries
------------

.. code-block:: python

   >>> a_dict = {'key': 'value', 'integer': 5, 'float': 2.0, 'boolean': True} # Think of a real-life dictionary. word: definition

   >>> a_dict
   {'key': 'value', 'integer': 5, 'float': 2.0, 'boolean': True}
   >>> a_dict['key']
   value
   >>> a_dict['integer']
   5

   >>> a_dict['key'] = 'change an entry'
   >>> a_dict
   {'key': 'change an entry', 'integer': 5, 'float': 2.0, 'boolean': True}

Conditional Statements and Loops
================================

For this section, pay attention to the indentation of each line! Each indent must be 4 spaces or a tab.

``if elif else``
--------------------

.. code-block:: python

   >>> x = 10
   >>> if(x > 10):
   ...     print('x is greater than 10.')
   ... elif(x < 10):
   ...     print('x is less than 10.')
   ... else:
   ...     print('x is exactly 10.')
   ... # elif and else are optional.
   x is exactly 10.

   # What if x was something different?

   >>> x = 8
   >>> # Pretend the if-elif-else statement is here.
   x is less than 10.

   >>> x = 12
   >>> # Pretend the if-elif-else statement is here.
   x is greater than 10.

``for``
-----------

.. code-block:: python

   >>> hydraulic_processes = ['flocculation', 'sedimentation', 'filtration']
   >>> for process in hydraulic_processes:
   ...     print(process)
   ... # "process" can be replaced with any word, and "hydraulic_processes" can be any list.
   flocculation
   sedimentation
   filtration

   >>> for i in range(3):
   ...     print(i)
   ... # range() starts from 0 and counts up. Note that 3 isn't printed.
   0
   1
   2

   >>> for i in range(4, 8):
   ...     print(i)
   ... # You can also set which number range() starts from.
   4
   5
   6
   7

``while``
-------------

.. code-block:: python

   >>> x = 0
   >>> while x < 3:
   ...     print(str(x) + ' is less than 3.') # str() lets you attach numbers to strings.
   ...     x += 1 # Shorthand for adding 1 to x (or x = x + 1).
   ...
   0 is less than 3.
   1 is less than 3.
   2 is less than 3.

Nesting
-------

.. code-block:: python

   >>> for i in range(1, 5):
   ...     if i % 2 == 1: # If the remainder of i/2 is 1
   ...         print(str(i) + 'is odd.')
   ...     else:
   ...         print(str(i) + 'is even.')
   ... # Pay attention to indents when nesting statements inside of others!
   1 is odd.
   2 is even.
   3 is odd.
   4 is even.

Functions
=========

.. code-block:: python

   >>> def exp(base, exponent):
   ...     return base ** exponent

   >>> exp(5, 2)
   25
   >>> exp(2, 4) + exp(10, 2)
   116
   >>> print('The volume of the cube is ' + str(exp(3, 3)) + ' inches.')
   The volume of the cube is 27 inches.

   >>> def parity(number):
   ...     if number % 2 == 1:
   ...         print(str(number) + 'is odd.')
   ...     else:
   ...         print(str(number) + 'is even.')

   >>> parity(27)
   27 is odd.
   >>> parity(40)
   40 is even.

**Now, complete Interactive Tutorial 2: Python Basics** `here <>`_.
