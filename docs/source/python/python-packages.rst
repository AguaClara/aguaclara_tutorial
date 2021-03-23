.. _python-packages:

***************
Python Packages
***************

Built-In Python Functions
-------------------------

Python has a lot of built-in functions that you can use to code. Read about the syntax and what they do on the `official Python documentation <https://docs.python.org/3/library/functions.html>`_.

There are also many third-party Python packages you can use for more powerful and specialized programming. We'll introduce a few in this tutorial.

NumPy
-----

NumPy is the fundamental package for scientific computing in Python. It contains a whole assortment of mathematical functions and values like ``pi`` and ``e``. In order to use the package, you'll have to ``import`` the package at the start of your script:

.. code-block:: python

    import numpy as np

Notice how NumPy is imported as ``np``. This is because Python uses dot notation, so every time we want to use a function within NumPy, we have to write ``numpy.function()``, but if we abbreviate it to ``np``, we can simply write ``np.function()``. For example, to use the ``sin()`` function to get the value of sin(pi), we would call it like so:

.. code-block:: python

    np.sin(np.pi)

The package has many other useful mathematical functions that you can read about in the `NumPy documentation <https://numpy.org/devdocs/>`_.

Advanced Math Packages
----------------------

If your code requires more advanced mathematical calculations, you can take advantage of the SciPy package. SciPy is great for things like calculus, differential equations, linear algebra, and statistics. You can learn more about it in the `SciPy documentation <https://docs.scipy.org/doc/scipy/reference/>`_.

For those who are curious, you can also perform symbolical calculations using SymPy, which you can learn about on the `SymPy documentation <http://www.sympy.org/en/index.html>`_.

AguaClara Package
-----------------

AguaClara has a Python package too! It's named ``aguaclara`` and is built for any calculations related to the design and research of AguaClara water treatment plants.

To install the package, simply run ``pip install aguaclara`` in your command line. To update the package, use ``pip install aguaclara --upgrade``. Then import it at the start of your Python script:

.. code-block:: python

    import aguaclara as ac

From ``ac``, we can now access values of `physical constants <https://aguaclara.github.io/aguaclara/core/constants.html>`_ and functions for `modeling physical, chemical, and hydraulic processes <https://aguaclara.github.io/aguaclara/core/physchem.html>`_; for `pipe sizing <https://aguaclara.github.io/aguaclara/core/pipes.html>`_, for `reading and analyzing data files <https://aguaclara.github.io/aguaclara/research/procoda_parser.html>`_, for `experimental design <https://aguaclara.github.io/aguaclara/research/stock_qc.html>`_, and more.

Just like with NumPy, we have to use dot notation. For example, here's code that uses a Reynolds number function called ``re_pipe()``:

.. code-block:: python

    ac.re_pipe(1, 1, 1)

Note that the 1's are the function's inputs: flow rate, pipe diameter, and kinematic viscosity. These quantities aren't obvious because they're missing scientific units, which we'll cover next.

To learn about all the functions and features available in the ``aguaclara`` package, check out the `AguaClara package documentation <https://aguaclara.github.io/aguaclara/index.html>`_.

Units
~~~~~

In research and engineering, units are incredibly important. They give physical significance to quantities and serve as a sanity check to confirm our answers. The ``aguaclara`` package comes with a system of units based on the `Pint package <https://pint.readthedocs.io/en/latest/>`_. To use ``aguaclara``'s unit registry (i.e. list of units), use the following import:

.. code-block:: python

    from aguaclara.core.units import u

The most commonly used units in AguaClara research and design are listed in the ``aguaclara`` documentation under the `Units module <https://aguaclara.github.io/aguaclara/core/units.html>`_. Here are some examples:

.. code-block:: python

    flow_rate = 10 * u.mL / u.s
    temperature = 20 * u.degC
    density = 60 * u.kg / u.m ** 3

Say we want to convert ``flow_rate`` to its metric base units (meters cubed). We can do this in 2 ways.

.. code-block:: python

    flow_rate.to(u.m ** 3 / u.s)

    flow_rate.to_base_units()

The unit registry also includes constants, which you can also find in the ``aguaclara`` `Units module documentation <https://aguaclara.github.io/aguaclara/core/units.html#constants>`_. For example, ``1 * u.gravity`` is equivalent to ``9.80665 u.m / u.s ** 2``.

Sig-Figs
~~~~~~~~

When you perform a calculation in Python and print the result, the output tends to contain an unnecessary number of decimal places. The ``set_fig_figs(n)`` function allows you to display only ``n`` significant figures when you print a value that has units. Note that this is only for printing; the actual value stored in Python still has its original precision.

.. code-block:: python

    >>> ac.set_sig_figs(3)

    >>> print(4 / 7 * u.m)
    0.571 meter

    >>> x = 6 / 7 * u.m
    >>> print(x)
    0.857 meter

Packages for Data Analysis
--------------------------
There are several other packages important to Python programming, such as Matplotlib and Pandas, but we will cover these in :ref:`data-analysis`.

So take a breath for now! Then dive into **Interactive Tutorial 3: Python Packages** `here <https://colab.research.google.com/drive/1A0QPENOXXhVq8T4PL6sD0XCUCQ2LHmj5?usp=sharing>`_.
