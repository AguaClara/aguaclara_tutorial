.. _common-issues:

*************
Common Issues
*************

``python`` Command Not Found
================================

If you get an error that the ``python`` command can't be found in the command line, that means that your command line doesn't know where your Python interpreter is.

Follow the steps for `Windows <https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/>`_ or `MacOS <https://python-docs.readthedocs.io/en/latest/starting/install3/osx.html>`_ to reinstall Python and add it to your computer's PATH.

If-Else Statements in Hydrogen
==============================

If you are using Hydrogen and are using ``Shift + Enter``\ , ``Cmnd + Enter``\ , or ``Cntrl + Enter`` to run python code then you may have noticed an error when trying to use if-else statements similar to the one below.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/IfElse1.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/IfElse1.png
   :alt: IfElseError


I think this error comes from the fact that by running an if-else statement line-by-line the else is not properly associated with the if, leading to a syntax error. Fortunately the solution is simple, just highlight the entire block of code containing the if-else statement and then use ``Shift + Enter``\ , ``Cmnd + Enter``\ , or ``Cntrl + Enter`` to run it.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/IfElse2.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/IfElse2.png
   :alt: IfElseSolution


Linter/Pycodestyle and Teletype
===============================

When editing Python code while using Teletype you may see an error similar to the one in the picture below. This error stems from something Teletype does when you are accessing a file that's not on your computer.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/LinterError.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/LinterError.png
   :alt: LinterError


At the moment we don't have a fix, so just continue working as usual and try not to get too annoyed at all the red boxes popping up.

Clone Error Using ``https``
===============================

For some users, when attempting to clone a repository with a URL that contains ``https``\ , they are given the error shown below. The current fix to this issue is to simply remove the "s" from ``https`` in the URL, and simply use ``http``.

[[/Images/httpsCloneError.png|httpsCloneError]]

Tell Me Who You Are GitHub Error
================================

When some people commit their changes to a file using Atom's built in GitHub, they get a red error box that asks them who they are. The error message is shown below:

.. code-block::

   *** Please tell me who you are.

   Run

     git config --global user.email "you@example.com"
     git config --global user.name "Your Name"

   to set your account's default identity.
   Omit --global to set the identity only in this repository.

   fatal: unable to auto-detect email address (got 'atomuser@WIN-VU79AHTD4PV.(none)')

To fix this error there are two different methods. One of them requires installing Git onto your computer. Since this is laborious, and takes time, we'll use a method that requires writing a ``.gitconfig`` file.

To write a ``.gitconfig`` file, follow these steps:


#. Open TextEdit for Mac or Notepad for Windows.
#. Write the following lines in TextEdit or Notepad:

.. code-block::

   [user]
         name = "YOUR GITHUB USERNAME"
         email = "YOUR GITHUB EMAIL"


#. Save the file with the name ``.gitconfig`` to your desktop. When you do this, you will likely save it as a ``.txt`` or ``.rtf`` file. Locate the file on your desktop, and right click to get the file info and remove ``.txt``\ , ``.rtf``\ , or any other extension that it may have saved as.
#. Navigate to ``C:\Users\YOUR_COMPUTERS_USERNAME`` for Windows or ``/Users/YOUR_COMPUTERS_USERNAME`` for Mac. These can be found in your File Navigator or Finder under your local drive.
#. Move the ``.gitconfig`` file to this location.
#. Quit and restart Atom. You should now be able to commit without running into the error above.
