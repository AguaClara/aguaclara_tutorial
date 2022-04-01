.. _transitioning-from-matlab:

*************************
Transitioning from MATLAB
*************************

Differences Between Python and MATLAB
=====================================

Indentation
-----------

Python interprets your code based off of the amount of indentation, or "whitespace", each line has. Successive lines with the same indentation are recognized as code blocks, which are run in context of the header:

.. code-block:: python

   # Good indentation
   if(x == y):       # Header
       x = x * 2     # Code block
       x = x + y     # Code block
       return x      # Code block

   # Bad indentation
   if(x == y):
      x = x * 2
        x = x + y
       return x

Ending statements
-----------------

Unlike MATLAB, you do not need a semi-colon to end a statement in Python.

Data indexing
-------------

MATLAB matrices begin at index 1, whereas Python lists begin at index 0.

.. code-block:: python

   >>> list = ['dog', 'cat', 'fish']
   >>> list[0]
   dog

Functions
---------

In MATLAB, functions are written with the keyword ``function``\ , the return parameter(s), the equals sign ``=``\ , the function name, and the input parameters. Functions are terminated with ``end``.

.. code-block:: matlab

   function y = average(x)
       if ~isvector(x)
           error('Input must be a vector')
       end
       y = sum(x)/length(x);
   end

In Python, functions can be written by using the keyword ``def``\ , followed by the function name, the input parameters in parentheses, and a colon. You may ``return`` a value at the end, although it isn't necessary.

.. code-block:: python

   def average(x):
       if ~isvector(x)
           raise VocationError("Input must be a vector")
       return sum(x)/length(x)

Statements
----------

``for`` loops and ``if`` statements do not require the keyword "end" in Python. The loop header in MATLAB varies from that of Python. Check examples below:

.. code-block:: matlab

   % MATLAB
   s = 10;
   H = zeros(s);
   for c = 1:s
       for r = 1:s
           H(r,c) = 1/(r+c-1);
       end
   end

.. code-block:: python

   # Python
   s = 10
   H = []
   for (r in range(s)):
       for (c in range(s)):
           H[r][c].append(1/(r + c - 1))

Printing
--------

In Python, printing is done with ``print()``\ , whereas MATLAB uses ``disp()``.

External Resources
==================


* `Numpy for MATLAB users <https://numpy.org/doc/stable/user/numpy-for-matlab-users.html>`_
* `Stepping from MATLAB to Python <http://stsievert.com/blog/2015/09/01/matlab-to-python/>`_
* `Python for MATLAB Users, UC Boulder <https://csdms.colorado.edu/w/images/Thomas_Hauser_CSDMS_2013_annual_meeting.pdf>`_
