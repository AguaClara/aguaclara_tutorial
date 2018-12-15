.. _markdown-basics:

***************
Markdown Basics
***************

Using Markdown
==============

We'll be using **Atom** to edit Markdown files and preview them nicely:

#. Open **Atom** and open the ``aguaclara_tutorial/`` repository folder that
   you cloned (or any other project folder you have).
#. Click on one of the ``*.md`` files in the left Project pane to open it.
#. Press ``Ctrl + Shift + M`` to open a formatted preview on the right.

   * If a preview didn't show up, review the instructions on `installing Atom <https://github.com/AguaClara/aguaclara_tutorial/wiki/Installing-Software-Tools>`_.

All Markdown files must be **text files with the** ``.md`` **file extension**. All of the text files within the ``aguaclara_tutorial`` repository are already Markdown files.

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

**To write in bold and italics, begin and end your text with triple asterisks.** asdfadf

.. code-block:: md

   ~~To write in strikethrough, begin and end your text with double tildes.~~

:raw-html-m2r:`<del>To write in strikethrough, begin and end your text with double tildes.</del>`

Lists
-----

.. code-block:: md

   1. Numbers followed by a period and space
   2. make ordered lists.


#. Numbers followed by a period and space
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
   #. or unordered lists

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

   To insert an image, put an exclamation point (!) before a link to the image. ![The
   display text appears when you hover over the image.]
   (http://aguaclara.cornell.edu/images/logo.png)

   You can also link to local files, although they won't show up on Github online.
   ![This image is in the wiki repository.](../Images/AguaClaraHome.png)

To insert an image, put an exclamation point (!) before a link. 
.. image:: http://aguaclara.cornell.edu/images/logo.png
   :target: http://aguaclara.cornell.edu/images/logo.png
   :alt: The display text appears when you hover over the image.


You can also link to local files, although they won't show up online on Github. 
.. image:: ../Images/AguaClaraHome.png
   :target: ../Images/AguaClaraHome.png
   :alt: This image is in the wiki repository.


Code Formatting
---------------

.. code-block:: md

   To add formatted code, `begin and end your code with backticks (`) `.

   The backtick (`) is usually found under the Esc button on your keyboard. It is NOT an
   apostrophe (') !

   ```
   To make a block of formatted code, begin and end your code with triple backticks (`).
   ```

   ```python
   def foo():
       print("Add the name of your programming language after the first triple backticks
       to add syntax highlighting.")
   ```

To add formatted code, ``begin and end your code with backticks (`)``.

The backtick (`) is usually found under the Esc button on your keyboard. It is NOT an apostrophe (') !

.. code-block:: md

   To make a block of formatted code, begin and end your code with triple backticks (`).

.. code-block:: python

   def foo():
       print("Add the name of your programming language after the first triple backticks to add syntax highlighting.")

Tables
------

.. code-block:: md

   | Heading | Above | Dashes |
   | --- | :---: | ---: |
   | Separate row | entries with | pipes | |
   | Use | colons | for alignment |
   | Left | Center | Right |

.. list-table::
   :header-rows: 1

   * - Heading
     - Above
     - Dashes
   * - Separate row
     - entries with
     - pipes \
     - 
   * - Use
     - colons
     - for alignment
   * - Left
     - Center
     - Right


Blockquotes
-----------

.. code-block:: md

   > To add a blockquote, write a greater than symbol (>), followed by a space, followed
   by your quoted text.

..

   To add a blockquote, write a greater than symbol (>), followed by a space, followed by your quoted text.


Horizontal Rules
----------------

.. code-block:: md

   To add a horizontal rule, put three dashes (-) on a line.

   ---

To add a horizontal rule, put three dashes (-) on a line.

----

*For some more ways to use Markdown, check out the `Markdown Cheatsheet <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>`_.*

LaTeX Formatting
----------------

In Atom, ``Ctrl + Shift + M`` will automatically display LaTeX formatted equations within Markdown files. They won't show up on this wiki page, but try pasting this line into a Markdown file in Atom:

.. code-block:: md

   $$ a^2 + b^2 = c^2 $$

Please refer to `this LaTeX tutorial <https://www.latex-tutorial.com/tutorials/amsmath/>`_ to learn how to write equations.


.. raw:: html

   <!-- TODO: Elaborate on writing LaTeX equations in a separate tutorial. -->



**Now, complete Lesson 1 of the interactive tutorials. It's in the ``Interactive-Tutorial-1-Markdown.md`` file in your ``aguaclara_tutorial`` repository.**

**Then, continue with the `Saving Markdown to PDF <https://github.com/AguaClara/aguaclara_tutorial/wiki/Saving-Markdown-to-PDF>`_ tutorial.**
