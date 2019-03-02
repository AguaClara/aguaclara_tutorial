.. _python-packages:

***************
Python Packages
***************

Built-In Python Functions
-------------------------

Python has a lot of built-in functions that you can use to code. Read about the syntax and what they do on the `official Python documentation <https://docs.python.org/3/library/functions.html>`_.

Python ``math`` Package
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

In addition to the modules developed by AguaClara, the ``aguaclara`` package imports third party packages that are useful for calculations and data manipulation. These include ``numpy``\ , which is useful for arrays, ``matplotlib``\ , which is used for plotting, and ``pandas``\ , which can be used to extract data from files like a ``.csv``.

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
--------

When you perform a calculation in Python and print the result, the output tends to be an answer that contains an unnecessary number of decimal places. In order to set the number of significant figures for your printed result, you would simply use the line as shown below:

.. code-block:: python

   u.default_format = '.3f' # This will give my printed value in 3 significant figures
   print(4 / 7 * u.m) # This will print 0.571 meter

   x = 6 / 7 * u.m
   print(x) # This will print 0.857 meter

To change the number of significant figures displayed, simply change the 3 with your desired number of sig-figs. You only need to have ``u.default_format`` once in your code for all printed values to have the same number of sig-figs. It should be noted that significant figures only take place if you ``print()`` your calculated value with units. This means ``print(3 / 9)`` will still give you a lot of sig-figs.

Units
-----

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

Plotting
--------

A lot of us are comfortable plotting in Excel or MATLAB, but did you know Python has the same capabilities, and is just as good? With the ``pandas`` package, Python has the capability of opening and parsing data from a ``.csv`` file. You can then use this data with ``matplotlib.pyplot`` to plot your raw data. Anaconda automatically comes with these packages, and by importing ``aguaclara.play``\ , these are automatically imported into your file.

Using ``pandas`` to read and use data is relatively simple, and the developers have created nice tutorials on how to use the package on `the Pandas documentation <http://pandas.pydata.org/pandas-docs/stable/tutorials.html>`_.

Plotting in Python is relatively straight forward. Below is an example of how to plot the entrance length of fully developed flow of water with velocity of 1 m/s at room temperature as a function of pipe diameter, d, using the Blasius Equation:

.. image:: ../images/blasius-equation.png
    :alt: Blasius Equation

.. code-block:: python

   from aguaclara.play import*

   xArray = u.Quantity(np.arange(0, 0.5, 0.01), u.m)

   @u.wraps(None, [u.m / u.s, u.m, u.m ** 2 / u.s], False)
   def re_flat_plate(velocity, dist, nu):
     """This function calculates the Reynolds Number for flow past a plate using fluid velocity, plate length, and kinematic viscosity."""
     return (velocity * dist / nu)

   plt.plot(xArray, 5 * xArray / np.sqrt(re_flat_plate(1, xArray, pc.viscosity_kinematic(293 * u.kelvin))), '-', label = 'Blasius Solution')
   plt.xlabel('Distance From Leading Edge (Meters)')
   plt.ylabel('Boundary Layer Thickness (Meters)')
   plt.title('Blasius Solution for Water at 293 K')
   plt.minorticks_on()
   plt.grid(which = 'major')
   plt.grid(which = 'minor')
   plt.legend(loc = 'lower right', ncol = 1)
   plt.tight_layout()
   plt.savefig('./Images/Blasius_Plot.png')
   plt.show()

.. TODO: Add photo of output.

Functions Within ``matplotlib.plt``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* ``plt.plot()``

  * This function takes in x values (typically an array), y values (sometimes an array or sometimes a function), a plot type (usually ``'.'`` for dots and ``'-'`` for smooth) to generate a plot, and label (a string that identifies the name of your plot).

    * Usually you won't need to insert inputs beyond the plot label

* ``plt.xlabel()`` and ``plt.ylabel()``

  * These functions take in strings to create axes labels

* ``plt.title()``

  * This function takes in a string to make a plot title

* ``plt.minorticks_on()``

  * Turns on the ability to use minor ticks

* ``plt.grid()``

  * Takes in a string (either ``'major'`` or ``'minor'``\ ) to determine which tick lines are displayed on the plot

* ``plt.legend()``

  * Takes a string for the location (\ ``loc``\ ) of the plot legend and the number of columns in your legend (\ ``ncol``\ ) to produce a plot legend

* ``plt.savefig()``

  * Takes a string for a file path for where you want to save your image (this will usually be an images folder in your repository)
  * When using a path, be sure to use forward slashes
  * If you're saving an image to a folder within the same repository as your Markdown file, you can use a relative path as shown above

* ``plt.xlim()`` and ``plt.ylim()``

  * Takes a range of values (i.e. 0:0.5 for our example above) to restrict the axes range

* ``plt.tight_layout()``

  * Ensures that your plot doesn't get cut off when saving as an image

* ``plt.show()``

  * Shows the plot in Atom when you run the code with Hydrogen

For more tutorials on plotting, check out this `pyplot tutorial <https://matplotlib.org/users/pyplot_tutorial.html>`_ or this `matplotlib tutorial <https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python>`_. You can also access a ``matplotlib`` `cheat sheet <https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf>`_.

Pandas
------

Load Data from CSV Files
~~~~~~~~~~~~~~~~~~~~~~~~

CSV files are good for transferring and storing data, good for business and data analysis. Pandas is the most popular data manipulation package in Python, and DataFrames are the Panda data type for storing tabular 2D data. To load data from CSV files, one can use the read_csv function in Pandas.

To start, one must first load the Pandas libraries with alias 'pd.'

.. code-block:: python
  import pandas as pd

Then, one can read data from the file "filename.csv." data = pd.read_csv("filename.csv")

One must add the path to the csv file in parentheses and assign this to the variable data.

There are several concepts that are important for understanding CSV files:

1. Filetypes and file extensions: data is stored in files with different names of different types. File is read by file extensions, which is the code following the dot.

2. CSV is a basic text file and any text editor can open it. Commas separate different columns and newlines separate rows.

3. Python looks in current working directory. Using relative paths is more common, which means starting at the current working directory until ending at the desired file location.

Possible Errors

File Not Found: path setup, current directory, or file name confusion
Unicode Decode: not specifying encoding which happens with non-standard characters
Parse Error: data format. If one adds the parameter engine='python', the data reading function is slower but more stable.

Helpful Pandas Functions
~~~~~~~~~~~~~~~~~~~~~~~~

**Boolean Indexing**

This would filter values of a column based on conditions from another set of columns. The conditions would be true or false.

.. code-block:: python
  data.loc[(data["Column 1"]=="Condition 1") & (data["Column 2"]=="Condition 2") & (data["Column 3"]=="Condition 3"), [Column 1, Column 2, Column 3]]

**Apply Function**

Returns some value after passing each row/column of a data frame with some function. Very common for playing with data and creating new variables.

.. code-block:: python
#Applying per column
data.apply(function, axis=0) #axis=0 defines that function is to be applied to each column

#Applying per row
data.apply(function, axis=1) #axis=1 defines that function is to be applied on each row
#use .head() after axis=#) if there are many rows

**Input Missing Files**

Can update missing values with mean/mode/median of the column. In this example we will use mode.

To find the mode you first need to import a function to determine the mode.

.. code-block:: python
  from scipy.stats import mode
  mode(data['Column name'])

This will return both the mode and count. Mode can be an array since there can be multiple values with high frequency. We take the first one by default:

.. code-block:: python
  mode(data['Gender']).mode[0]

This function is everything integrated together:

.. code-block:: python
  data['Column name'].fillna(mode(data['Column name']).mode[0], inplace=True)
  data['Column name 2'].fillna(mode(data['Column name 2']).mode[0], inplace=True)
  data['Column name 3'].fillna(mode(data['Column name 3']).mode[0], inplace=True)

**Pivot Table**

Input missing values.

.. code-block:: python
  impute_grps = data.pivot_table(values=["Column 1"], index=["Group 1"], index=["Group 2", "Group 3", "Group 4"], aggfunc=np.mean)
  print impute_grps

**Multi-Indexing**

One index can be a combination of several values, and it helps to perform operations really fast.

.. code-block:: python
  for i, row in data.loc[data['Column 1'].isnull(),:].iterrows():
    ind = tuple([row['Group 1'], row['Group 2'], row['Group 3']])
    data.loc[i, 'Column 1'] = impute_grps.loc[ind].values[0]

It requires a tuple to hav ea loc statement. The values[0] suffix is required because by default, the answer returned would not match with the answer that you are looking for.

**Cross Tab**

Gets an initial "feel," or view, of the data. Can validate some basic hypothesis.

.. code-block:: python
  pd.crosstab(data["Column 1"], data["Column 2"], margins=True)

You can also use percentages instead of absolute numbers to make quick insights by the apply function.

.. code-block:: python
  def percConvert(ser):
    return ser/float(ser[-1])
    pd.crosstab(data["Column 1"], data["Column 2"], margins=True).apply(percConvert, axis=1)

**Merge DataFrames**

Need to collate information from different sources.

.. code-block:: python
  data = pd.DataFrame([1, 2, 3], index=['Type 1', 'Type 2', 'Type 3'], columns=['factors'])
data)

Now can merge this information with the original dataframe as:

.. code-block:: python
  data_merged = data.merge(right=certain_factors, how='inner', left_on='Columns', right_index=True, sort=False)
  data_merged.pivot_table(values='subject', index=['Columns', 'factors'], aggfunc=len)

The pivot table validates successful merge operation. The 'values' argument is irrelevant here because we are counting the values.

**Sorting DataFrames**

Pandas allow easy sorting based on multiple columns, as shown here:

.. code-block:: python
  data_sorted = data.sort_values(['Column 1', 'Column 2'], ascending=False)
  data_sorted[['Column 1', 'Column 2']].head(10)

**Plotting (Boxplot & Histogram)**

Boxplots and histograms can be directly plotted in Pandas, so calling matplotlib separately is unnecessary. It is just a one-line command. An example is comparing the distribution of the two columns:

.. code-block:: python
  import matplotlib.pyplot as plt
  %matplotlib inline
  data.boxplot(column="Column 1", by="Column 2")

.. code-block:: python
  data.hist(column="Column 1", by="Column 2",bins=30)

**Cut function for binning**

Numerical values can make more sense if clustered together. Modeling this way is more intuitive and will avoid overfitting. This is a simple function which can be reused for binning any variable pretty easily:

.. code-block:: python
  def binning(col, cut_points, labels=None):
  #Define min and max values:
  minval = col.min()
  maxval = col.max()

  #create list by adding min and max to cut_points
  break_points = [minval] + cut_points + [maxval]

  #if no labels provided, use default labels 0 ... (n-1)
  if not labels:
     labels = range(len(cut_points)+1)

  #Binning using cut function of pandas
  colBin = pd.cut(col,bins=break_points,labels=labels,
  include_lowest=True)
  return colBin

**Coding Nominal Data**

Sometimes it is necessary to modify nominal variable categories. This may be because of:

- Algorithms like Logistic Regression needing all inputs to be numeric, so nominal variables are usually coded as 0, 1...(n-1)
- Category may be represented in two ways. For example, temperature might be recorded as "High," "medium," "low," "H," "Low." "High" and "H" are the same category, and "low" and "Low" are, but python would read them as different
- Some categories may have low frequencies so one should combine them

.. code-block:: python
  #Replace function
  def coding(col, codeDict):
    colCoded = pd.Series(col, copy=True)
    for key, value in codeDict.items():
      colCoded.replace(key, value, inplace=True)
      return colCoded

  #Coding Status as Y=1, N=0:
  print 'Before Coding:'
  print pd.value_counts(data["Status"])
  data["Status"] = coding(data["Status"], {'N':0, 'Y':1})
  print '\nAfter Coding:'
  print pd.value_counts(data["Status_Coded"])

**Iterating over rows of a dataframe**

Though this operation isn't frequently used, there are times when you may have to iterate through all rows using a for loop. For example, a common problem is treating variables incorrectly in Python. Usually, this happens when: nominal variables with numeric categories are treated as numerical, or numeric variables with characters entered in one of the rows because of a data error are considered categorical.

It's usually a good idea to manually define column types. If we check current data types of all columns:

.. code-block:: python
  data.dtypes

**Functions Within ``matplotlib.plt``**

- ``plt.plot()``







#To check missing values to confirm:
print data.apply(num_missing, axis=0)

Arrays and Lists in Python
==========================

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
