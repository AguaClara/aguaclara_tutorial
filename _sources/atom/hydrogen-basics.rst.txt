.. _hydrogen-basics:

***************
Hydrogen Basics
***************

How do I write Python code in a ``.md`` file?
=================================================

Markdown has a wonderfully easy function that enables you to insert blocks of code written in dozens of common programming languages like Python directly into the file itself. To do this, simply type three consecutive backticks/backquotes, that key with the tilda that you probably seldomly use, followed by the name of the programming language you wish to write in. In our case, we'll always use Python. On a new line, you can begin writing your block of code. Once you finish writing your code, make sure to end the block with three more backticks/backquotes on the line below your final line of code. You should end up with something that looks like this:

.. code-block:: md

   ```python
   myGreeting = 'Welcome to AguaClara!'
   print(myGreeting)
   ```

In your ``.md`` file, the resulting output will look something like this:

.. code-block:: python

   myGreeting = 'Welcome to AguaClara!'
   print(myGreeting)

Now lets say I want to insert a block of plain text like this sentence after a block of code, but decide that I want to continue developing my code after the plain text. Instead of starting a new code block and adding everything I previously coded in the old block into my new code block, I can simply continue writing my code where I left off. For example, say I want to append something to ``myGreeting`` in a code block after this paragraph. All I have to do to implement this is as follows:

.. code-block:: python

   myNewGreeting = myGreeting + ' I hope you have a fun time!'
   print(myNewGreeting)

My variable assignments from my first code block are recognized in my second code block, meaning my assignments for ``myGreeting`` carries between the two blocks.

Running the code with Hydrogen
==============================

``Hydrogen: Run``
---------------------

``Hydrogen: Run`` is the most basic command for running your code, and will execute exactly what you tell it to. The quick keystroke to perform this action is ``Cmnd + Enter`` or ``Cntrl + Enter``. There are several ways to use ``Hydrogen: Run``.


* **Selected Code:** If you've highlighted a block of code and perform ``Hydrogen: Run``\ , the entire block of code will be executed.
* **Current Block:** If you haven't highlighted any code, Hydrogen will attempt to run code on or before the line your cursor is on.

  * If you're on a line with a complete code expression, ``Hydrogen: Run`` will evaluate that line only.
  * If you're on a line that begins a loop, ``Hydrogen: Run`` will evaluate the entire loop.
  * If you're on a blank line, ``Hydrogen: Run`` will run the first block of code above your current position.

``Hydrogen: Run All`` and ``Hydrogen: Run All Above``
-------------------------------------------------------------

``Hydrogen: Run All`` and ``Hydrogen: Run All Above`` are two useful functions that enable you to run an entire script without selecting all the code. Unfortunately, both commands are not supported within a ``.md`` file, and will only be helpful if you work out of a ``.py`` file.


* To use ``Hydrogen: Run All``\ , simply press ``Cmnd + Cntrl + Enter`` anywhere in your code.
* To use ``Hydrogen: Run All Above``\ , you'll have to use ``Cmnd + Shift + P`` to open the Atom palette and search for the command itself since it doesn't come with a keybinding by default.

How do I know if my code has been executed by Hydrogen?
=======================================================

The great thing about Hydrogen is that it's incredibly easy to know if the Python code you wrote is syntactically correct and executable. If we look at the code I wrote above, and use ``Hydrogen: Run`` on the block, we'll get two things to show up. The first thing we'll see is a little check mark next to the line ``myGreeting = 'Welcome to AguaClara!'``. This check indicates that Hydrogen has evaluated that code, but since that line is purely a variable assignment with no output, Hydrogen won't produce any output. In the line containing ``print(myGreeting)``\ , Hydrogen outputs the string "Welcome to AguaClara!" because the ``print()`` function in Python produces an output.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/GoodHydrogenRun.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/GoodHydrogenRun.png
   :alt: GoodHydrogenRun


Hydrogen will also tell you when your code is bad and won't execute by giving you the error message that any other Python interpreter would give if you attempted to run the same bad code. In the case of our sample code, I left out a single quote at the end of my message, so Python couldn't interpret it as a ``string``\ , and Hydrogen told me what the syntax error was in the message.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/BadHydrogenRun.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/BadHydrogenRun.png
   :alt: BadHydrogenRun

**Now, complete Lesson 3 of the interactive tutorials. It's in the**
``Interactive-Tutorial-3-Hydrogen.md`` **file in your** ``aguaclara_tutorial``
**repository.**
