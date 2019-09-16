.. _markdown-basics:

***************
Markdown Basics
***************

Basic Text
----------

.. code-block:: md

   Regular text comes out normally.

   Leave an empty line between paragraphs.

Regular text comes out normally.

Leave an empty line between paragraphs.

Headers
-------

.. code-block:: md

   # To write a header, write a pound symbol (#), followed by a space, followed by your header text.

To write a header, write a pound symbol (\ ``#``\ ), followed by a space, followed by your header text.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: md

   ## Add pound symbols to write lower level (smaller) headers.

Add pound symbols to write lower level (smaller) headers.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Emphasis
--------

.. code-block:: md

   *To write in italics, begin and end your text with single asterisks.*

*To write in italics, begin and end your text with single asterisks.*

.. code-block:: md

   **To write in bold, begin and end your text with double asterisks.**

**To write in bold, begin and end your text with double asterisks.**

.. code-block:: md

   ***To write in bold and italics, begin and end your text with triple asterisks.***

**To write in bold and italics, begin and end your text with triple
asterisks.** (This webpage's line can't be bolded and italicized due to the
`limitations of RST
<https://stackoverflow.com/questions/11984652/bold-italic-in-restructuredtext>`_!)

.. code-block:: md

   ~~To write in strikethrough, begin and end your text with double tildes.~~

To write in strikethrough, begin and end your text with double tildes. (This
webpage's line can't be strikethrough'd due to the limitations of RST!)

Lists
-----

.. code-block:: md

   1. Ones followed by a period and space
   1. make ordered lists.


#. Ones followed by a period and space
#. make ordered lists.

.. code-block:: md

   - Dashes followed by a space
   - make unordered lists.


* Dashes followed by a space
* make unordered lists.

.. code-block:: md

   1. You can indent
       1. ordered lists
       - or unordered lists
           - to make sublists.


#. You can indent

   #. ordered lists

   * or unordered lists

     * to make sublists.

Links
-----

.. code-block:: md

   To insert a link, [put the display text in square brackets and the URL in
   parentheses](http://aguaclara.cornell.edu).

   Unformatted URL's automatically become links: http://aguaclara.cornell.edu

To insert a link, `put the displayed text in square brackets and the URL in parentheses <http://aguaclara.cornell.edu>`_.

Unformatted URL's automatically become links: http://aguaclara.cornell.edu

Images
------

.. code-block:: md

   To insert an image, put an exclamation point (!) before a link to the image.
   ![The display text appears when you hover over the image.](http://aguaclara.cornell.edu/images/logo.png)

   You can also link to local files.
   ![This image is in ``docs/images``.](../images/logo.png)

   Markdown supports HTML image rendering too. You can adjust the dimensions...
   <img src="http://aguaclara.cornell.edu/images/logo.png" width=100>

   ... and change the alignment.
   <p align="center"> <img src="../images/logo.png"> </p>

To insert an image, put an exclamation point (!) before a link.

.. image:: http://aguaclara.cornell.edu/images/logo.png
   :target: http://aguaclara.cornell.edu/images/logo.png
   :alt: The display text appears when you hover over the image.

You can also link to local files.

.. image:: ../images/logo.png
   :alt: This image is in ``docs/images``.

Markdown supports HTML image rendering too. You can adjust the dimensions...

.. image:: http://aguaclara.cornell.edu/images/logo.png
   :target: http://aguaclara.cornell.edu/images/logo.png
   :width: 100

... and change the alignment.

.. image:: ../images/logo.png
   :align: center

Code Formatting
---------------

.. code-block:: md

   To add formatted code, `begin and end your code with backticks`.

   The backtick is usually found under the Esc button on your keyboard. It is NOT an
   apostrophe (') !

   ```
   To make a block of formatted code, begin and end your code with triple backticks.
   ```

   ```python
   def foo():
       print("Add the name of your programming language after the first triple backticks to add syntax highlighting.")
   ```

To add formatted code, ``begin and end your code with backticks``.

The backtick is usually found under the Esc button on your keyboard. It is NOT an apostrophe (') !

.. code-block:: md

   To make a block of formatted code, begin and end your code with triple backticks.


.. code-block:: python

   def foo():
       print("Add the name of your programming language after the first triple backticks to add syntax highlighting.")

**Note: In a Colab/Jupyter notebook, we replace blocks of Python code with runnable code cells.**

Tables
------

.. code-block:: md

   | Heading | Above | Dashes |
   | --- | :---: | ---: |
   | Separate row | entries with | pipes |
   | Use | colons | for alignment |
   | Left | Center | Right |

.. list-table::
   :header-rows: 1

   * - Heading
     - Above
     - Dashes
   * - Separate row
     - entries with
     - pipes
   * - Use
     - colons
     - for alignment
   * - Left
     - Center
     - Right

(Alignment doesn't work in this webpage due to the limitations of RST!)

Blockquotes
-----------

.. code-block:: md

   > To add a blockquote, write a greater than symbol, followed by a space,
   followed by your quoted text.

..

   To add a blockquote, write a greater than symbol, followed by a space,
   followed by your quoted text.


Horizontal Rules
----------------

.. code-block:: md

   To add a horizontal rule, put three dashes (-) on a line.

   ---

To add a horizontal rule, put three dashes (-) on a line.

----

*For some more ways to use Markdown, check out the* `Markdown Cheatsheet <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>`_.

LaTeX Formatting
----------------

LaTeX formatted equations won't show up on this wiki page, but try pasting this line into a text cell in Colab:

.. code-block:: md

   $$ a^2 + b^2 = c^2 $$

Please refer to `this LaTeX tutorial <https://www.latex-tutorial.com/tutorials/amsmath/>`_ to learn how to write equations.

**Now, you're ready to complete Interactive Tutorial 1: Markdown** `here <https://colab.research.google.com/drive/15yYapOXlOLOEYMttz8v1Vb5odRkkJdhO>`_.
