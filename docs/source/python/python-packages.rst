.. _python-packages:

***************
Python Packages
***************

Built-In Python Functions
-------------------------

Python has a lot of built-in functions that you can use to code. Read about the syntax and what they do on the `official Python documentation <https://docs.python.org/3/library/functions.html>`_.

``math`` Package
---------------------------

Python also comes with a pre-installed math package with a whole assortment of different functions and mathematical values like ``pi`` and ``e``. In order to use the package, you'll have to ``import`` the package at the start of your script. Below I've imported the math function.

.. code-block:: python

   import math as m

Notice how I abbreviated the ``math`` package as ``m``. This is because Python uses dot notation, so every time I want to use a function within ``math``\ , I have to do ``m.function()``\ , which is much simpler than using ``math.function()``. For example, say I want to use ``sin()`` to get the value of sin(pi), I would have to call it like so:

.. code-block:: python

   myValue = m.sin(m.pi)

The Python ``math`` package has a whole bunch of useful mathematical functions that you can read about on the `Python documentation for math <https://docs.python.org/3/library/math.html>`_.

Advanced Math Functions
-----------------------

In the rare case that your code requires something more than the basic math operations that Python has built-in, you can take advantage of the SciPy package, which also comes with Anaconda. SciPy is great for things like calculus, differential equations, linear algebra, and statistics. You can learn more about it at the `SciPy documentation <https://docs.scipy.org/doc/scipy/reference/>`_. Additionally, you can perform symbolical calculations using SymPy, which you can learn about on the `SymPy documentation <http://www.sympy.org/en/index.html>`_.

``aguaclara`` Package
---------------------------

AguaClara has a python package called ``aguaclara``\ , which comes with many useful modules including ``unit_registry``\ , ``physchem``\ , ``utility``\ , and ``pipedatabase``. The ``unit_registry`` module allows us to apply units to our calculations, which is talked about later. The ``physchem`` module comes with many pre-defined functions related to hydraulics, flocculation, and sedimentation to name a few. You can explore all the different functions and inputs along with what they calculate in `the physchem source code <https://github.com/AguaClara/aguaclara/blob/master/aguaclara/core/physchem.py>`_.The ``utility`` module comes with many functions that do useful things unrelated to the physical/chemical process of water treatment. To explore the different functions available, go to the `utility source code <https://github.com/AguaClara/aguaclara/blob/master/aguaclara/core/utility.py>`_. Lastly, the ``pipes`` module contains many functions related to pipe sizing. You can check out the different functions available in the `pipes source code <https://github.com/AguaClara/aguaclara/blob/master/aguaclara/core/pipes.py>`_.

In addition to the modules developed by AguaClara, the ``aguaclara`` package imports third party packages that are useful for calculations and data manipulation. These include ``numpy``\ , which is useful for arrays, ``matplotlib``\ , which is used for plotting, and ``pandas``\ , which can be used to extract data from files like a ``.csv``. To learn more about these, see :ref:`data-analysis`.

To install the package, simply run ``pip install aguaclara`` in your Command Shell (PC) or Terminal (Mac). To update the package, use ``pip install -U no-deps aguaclara`` or ``sudo pip install aguaclara --upgrade`` if the other did not work.

In order to use these modules within your Python script, you'll have to import them. At the start of your Python code, you should write the line of code as shown below to take advantage of the packages:

.. code-block:: python

   from aguaclara.play import*

In all code written for AguaClara, the modules are always specified using dot notation with abbreviations for the module names. Here's a quick guide for what the abbreviations are:


* ``pc`` is used to abbreviate the ``physchem`` module
* ``u`` is used to abbreviate the ``unit_registry`` module
* ``ut`` is used to abbreviate the ``utility`` module
* ``pipe`` is used to abbreviate the ``pipedatabase`` module
* ``exp`` is used to abbreviate the ``expert_inputs`` module
* ``mat`` is used to abbreviate the ``materials_database`` mmodule
* ``k`` is used to abbreviate the ``k_value_of_reductions_utility`` module
* ``pipline`` is used to abbreviate the ``pipeline_utility`` module
* ``np`` is used to abbreviate the NumPy package
* ``pd`` is used to abbreviate the Pandas package
* ``plt`` is used to abbreviate MatPlotLib's plotting module

When I want to use a function or something from these modules, I have to use dot notation. For example, if I want to make use of a Reynolds Number function in ``physchem``\ , I would do this:

.. code-block:: python

   pc.re_pipe(1, 1, 1) # Note that the 1s are the function's respective inputs (Flow Rate, Pipe Diameter, and Kinematic Viscosity)

Sig-Figs
~~~~~~~~

When you perform a calculation in Python and print the result, the output tends to be an answer that contains an unnecessary number of decimal places. In order to set the number of significant figures for your printed result, you would simply use the line as shown below:

.. code-block:: python

   u.default_format = '.3f' # This will give my printed value in 3 significant figures
   print(4 / 7 * u.m) # This will print 0.571 meter

   x = 6 / 7 * u.m
   print(x) # This will print 0.857 meter

To change the number of significant figures displayed, simply change the 3 with your desired number of sig-figs. You only need to have ``u.default_format`` once in your code for all printed values to have the same number of sig-figs. It should be noted that significant figures only take place if you ``print()`` your calculated value with units. This means ``print(3 / 9)`` will still give you a lot of sig-figs.

Units
~~~~~

In engineering, units are incredibly important to us. They help as a sanity check to confirm our answers or reveal problems with our solutions. We'll be using Pint. The ``aguaclara`` package that you installed comes with the necessary units module. When you use the import code as shown in the ``aguaclara`` packages section of this Wiki, your script will have access to the unit registry.

Now we are ready to use units. As an example of how to use them, say I want to define a flow rate with units of mL/s. I would simply do as follows:

.. code-block:: python

   QPlant = 10 * u.mL / u.s

Let's say I want to convert the units to its metric base units (meters cubed). I can do this in two ways.

.. code-block:: python

   # If I already know the base units, I can do this:
   QPlant.to(u.m ** 3 / u.s)

   # Or I can do this:
   QPlant.to_base_units()

Pint also includes constants, which you can find on the `Pint documentation <https://github.com/hgrecco/pint/blob/master/pint/constants_en.txt>`_.


Arrays and Lists in Python
--------------------------

Python has no native array type. Instead, it has lists, which are defined using ``[ ]``\ :

.. code-block:: python

   myList = [0, 1, 2, 3]

In order to use arrays, we will utilize the NumPy package, which comes with the Anaconda installation. Like the ``math`` package, NumPy has to be imported into your code. Typically, we will import it via ``aguaclara.play`` as ``np`` as you will see in a lot of AguaClara code. To turn my list into an array, I would simply write this code:

.. code-block:: python

   from aguaclara.play import*
   myArray = np.array(myList)

To make a 2D array, I can use the same ``np.array()`` command. Below is an example of how to make a 2D array.

.. code-block:: python

   my2DArray = np.array([[1 ,2, 3], [4, 5, 6], [7, 8, 9]])

If I want to pull out a single row or column from my 2D array, I would do the following:

.. code-block:: python

   my2DArray[:,1] # This will give me the middle column

   my2DArray[1,:] # This will give me the middle row

To find the length of a 1D array or size or shape of a 2D array, I can do the following:

.. code-block:: python

   len(myArray) # This tells me the length of myArray

   np.size(my2DArray) # This tells me the size of my2DArray

   np.shape(my2DArray) # This tells me the dimensions of my2DArray

NumPy arrays also support units, which are mentioned later in this guide. If I wanted to apply units to my array, I would run this code:

.. code-block:: python

   myArrayUnits = myArray * u.m

Say I want an array of a specified size starting from 0, something that would be helpful for generating a plot. I could use ``np.arange()`` to do this. If I want an array from 0 to 9, or of size 10, I would simply run ``np.arange(10)``. I can also specify two bounds and a step size if I want to have even greater control over my array. To do this, I would still use ``np.arange()``\ , but with 3 inputs as such: ``np.arange(low, high, step size)``\ , so ``np.arange(0, 1, 0.1)`` would give me an array from 0 to, but not including, 1 in 0.1 increments.

NumPy has many capabilities, which I won't be able to discuss in-depth on the Wiki, but `numpy's cheat sheet <https://www.dataquest.io/blog/numpy-cheat-sheet/>`_ is a great guide to learn more about NumPy's power.
