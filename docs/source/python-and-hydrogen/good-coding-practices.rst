.. _good-coding-practices:

*********************
Good Coding Practices
*********************

Doctest
=======

While you're writing your code or are finished with your code, it is always important to test your code. One of the things that has to be tested is any function that you write because you'll want to know whether the output from your new function is correct. You can also test a block of code to make sure all the pieces to your script work together properly. For AguaClara work, your code should always incorporate doctesting.

Doctesting is important to your work because it helps with documentation and debugging. When you use doctesting, you're essentially telling the test that your code should produce a specific output in the development stage it's currently in. This is useful during the transition between semesters when teams are changing personnel. Having that doctest tells the new members what the code was previously producing, so if the code isn't producing what was previously eexpected, they can try to identify the source of the problem. Additionally, doctesting lets you keep track of your code's progress throughout the development stages. If your tests are failing, it can be an indication that an unexpected change occured in the code, which can then be identified and fixed.

Using doctesting is fairly straight forward. There are several key things that your code will need in order to doctest.


* You **must** have your tests in docstrings

  * Docstrings are sets of triple double quotations as follows:
    .. code-block:: python

       """This is a docstring"""

* Within your docstring, you must us ``>>>`` to indicate a Python interpreter input

  * This is what you would see if you called a Python function or ran a block of Python code in Terminal or Command Shell

* Below each input, you **must** put the output that would be displayed in the interpreter if you ran your function or block of code

  * This can be done by running the code that you wish to test using Hydrogen, and copying and pasting the output that it gives you to the doctest
  * For outputs that contain units, which most of your code should have, Hydrogen will not give you the Python interpreter output. To get that output, you must enter the test output as ``<Quantity(THE NUMERICAL PART OF THE OUTPUT, 'STRING OF THE UNITS ASSOCIATED WITH YOUR OUTPUT')>``
  * If you're testing a function with a ``print()`` statement and a ``return`` value, you must include the output produced by both in your doctest. Usually the ``print()`` statement output appears before the function's return value. **Remember that ``aide_design.play`` automatically sets the number of sigfigs in a print statement to 3 sig figs. Hydrogen will always give the full numerical answer.**
  * Array outputs are always enclosed in ``[]`` if you ``print()`` it, as nothing if you only assign it to a variable name, or as ``array([YOUR ARRAY])`` if you don't assign it to a variable name or ``print()`` it
  * If you're testing a loop or ``if-statement``\ , you must show the indentation in the inout using ``...`` followed by tabs

* At the start of your code, you should ``import doctest`` to use the doctest functionality in Python
* At the end of the code, you should have a line with ``doctest.testmod(verbose=True)``

Let's use doctesting on the function for the calculating the number of moles for an ideal gas written above.

.. code-block:: python

   from aide_design.play import*
   import doctest

   def nmoles_alt(P, V, T):
     """This function also takes in values of pressure, temperature,
     and volume to determine the number of moles of an ideal gas.

     >>> from aide_design.play import*
     >>> nmoles_alt(1, 10, 100)
     <Quantity(1.2186597134166985, 'mole')>
     """
     P = P * u.atm # Applies units to pressure
     V = V * u.liter # Applies units to volume
     T = T * u.kelvin # Applies units to temperature
     return ((P * V / (u.R * T)).to_base_units())

   doctest.testmod(verbose=True)

After running the test in the code block above, this is what I got:

[[/Images/TestPass.png|TestPass]]

Now lets say I wrote the code a long time ago and the output that I got during testing at that point in the development gave me an ouput of ``<Quantity(10, 'meter')>``. My doctest would look like this:

.. code-block:: python

   from aide_design.play import*
   import doctest

   def nmoles_alt(P, V, T):
     """This function also takes in values of pressure, temperature,
     and volume to determine the number of moles of an ideal gas.

     >>> from aide_design.play import*
     >>> nmoles_alt(1, 10, 100)
     <Quantity(10, 'meter')>
     """
     P = P * u.atm # Applies units to pressure
     V = V * u.liter # Applies units to volume
     T = T * u.kelvin # Applies units to temperature
     return ((P * V / (u.R * T)).to_base_units())

   doctest.testmod(verbose=True)

Since my new code has been updated to produce the output we previously saw, I should expect my test to fail, which we see in the message below:

[[/Images/TestFail.png|TestFail]]

In the next code block, I've shown how to write doctests for code containing loops, ``print()`` statements within functions, and arrays.

.. code-block:: python

   from aide_design.play import*
   import doctest

   def nmoles_alt(P, V, T):
     """This function also takes in values of pressure, temperature,
     and volume to determine the number of moles of an ideal gas.

     >>> from aide_design.play import*
     >>> np.array([1, 1, 1, 1])
     array([1, 1, 1, 1])
     >>> print(np.array([1, 1, 1, 1]))
     [1 1 1 1]
     >>> P = np.array([1, 1, 1, 1])
     >>> V = np.array([])
     >>> for i in [1, 2]:
     ...   for j in [3, 4, 5]:
     ...     V = np.append(V, i*j)
     ...     print(i*j)
     3
     4
     5
     6
     8
     10
     >>> nmoles_alt(1, 10, 100)
     1.219 mole
     <Quantity(1.2186597134166985, 'mole')>
     >>> nmoles_alt(P[0], V[5], 100)
     1.219 mole
     <Quantity(1.2186597134166985, 'mole')>
     """
     P = P * u.atm # Applies units to pressure
     V = V * u.liter # Applies units to volume
     T = T * u.kelvin # Applies units to temperature
     print((P * V / (u.R * T)).to_base_units()) # This prints the number of moles
     return ((P * V / (u.R * T)).to_base_units())

   doctest.testmod(verbose=True)

**It is important to note that any white spaces (spaces in your code) in your inputs or outputs of your doctest will be interpreted in the test. These will throw a failed test even if the output is correct, so it is extremely important to check that your doctests don't have white spaces.**

AguaClara Coding Standards and Variable Naming
==============================================

When coding for AguaClara, you should stick closely to our style guide and variable naming conventions.


* For variable naming, check out `the aguaclara naming conventions <https://github.com/AguaClara/aide_design/wiki/Variable-Naming>`_.
* For coding standards, check out `the aguaclara coding standards <https://github.com/AguaClara/aide_design/wiki/Standards>`_.

.. TODO: change those links to the latest version.
