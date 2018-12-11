

.. raw:: html

   <!-- START doctoc generated TOC please keep comment here to allow auto update -->
   <!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->





* `Python in Command Line <#python-in-command-line>`_

  * `Interactive Python Interpreter <#interactive-python-interpreter>`_
  * `Python Scripts <#python-scripts>`_


.. raw:: html

   <!-- END doctoc generated TOC please keep comment here to allow auto update -->



Now that you've written Python code, it's time to see how to run it!

Python in Command Line
======================

In this tutorial, we'll be focusing on how to run Python within the command line. In a following tutorial, we'll show how to run Python in a Markdown file using Hydrogen.

There are two methods to run Python code in the Command Line: the *Interactive Python Interpreter* and *Python scripts*.

Interactive Python Interpreter
------------------------------

Remember how the `Writing Python Code <https://github.com/AguaClara/aguaclara_tutorial/wiki/Writing-Python-Code#how-this-tutorial-works>`_ tutorial was formatted?

.. code-block:: python

   >>> a_dict
   {'key': 'value', 'integer': 5, 'float': 2.0, 'boolean': True}
   >>> a_dict['key']
   value

That was an example of the **Interactive Python Interpreter**\ : a way to intuitively run Python within the command line.

To enter the **Interactive Python Interpreter**\ , open your command line (MacOS/Linux = **Terminal**\ , Windows = **PowerShell**\ ) and enter ``python``\ :

.. code-block:: bash

   $ python
   Python 3.6.5
   Type "help", "copyright", "credits" or "license" for more information.
   >>> _

`Help: the ``python`` command isn't working! <https://github.com/AguaClara/aguaclara_tutorial/wiki/Common-Issues#python-command-not-found>`_

(\ **\ *Note*\ **\ : The ``$`` on the first line indicates that we're in **Terminal** - it's *not* part of the command that you type. In **Powershell**\ , you'd see a ``>`` instead.)

Now you can run any lines of Python code that you'd like: try it out for yourself!

.. code-block:: python

   >>> a_list = ['can store anything!', 5, 2.0, True]

   >>> a_list
   ['can store anything!', 5, 2.0, True]
   >>> a_list[0]
   can store anything!
   >>> a_list[3]
   True

To leave the **Interactive Python Interpreter**\ :

.. code-block:: bash

   >>> quit()
   $ _

Note that variables are only stored until you quit the interpreter.

Python Scripts
--------------

The **Interactive Python Interpreter** is great for quickly testing lines of Python code, but what if you want to write something more complex?

In the last tutorial, you wrote part of a **Python script**\ : a file with the ``*.py`` extension. To run the code in a Python script in the command line:


#. Navigate to the script's directory with the ``ls`` and ``cd`` commands. `Need a refresher? <https://github.com/AguaClara/aguaclara_tutorial/wiki/Interactive-Tutorials#basic-commands>`_
#. Enter ``python``\ , followed by a space, followed by the name of the file.

Let's say we have a script called ``foo.py`` containing this line:

.. code-block:: python

   print('Hello world!')

Now, let's run the script in the command line:

.. code-block:: bash

   $ python foo.py
   Hello world!

What this does is run the *main body* of the script: the lines which are *not in functions*. To use functions, *define* them at the *beginning* of the script and *call* them in the main body.

``foo.py``\ :

.. code-block:: python

   def greet():
       print('Hello world!')

   greet()

Command line:

.. code-block:: bash

   $ python foo.py
   Hello world!

Python runs code lines in order from start to end; if you don't define functions at the beginning, Python won't know what to do when you call them!

**Now, run the code in ``Interactive-Tutorial-2-Python-Basics.py``. Fix any TODO's that fail the tests.**

**Then, continue with the `Python Packages <https://github.com/AguaClara/aguaclara_tutorial/wiki/Python-Packages>`_ tutorial.**
