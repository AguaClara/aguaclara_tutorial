
At the ends of some sections, you'll need to complete *interactive tutorials* from the ``aguaclara_tutorial`` repository; this tutorial will explain how to use them.


.. raw:: html

   <!-- START doctoc generated TOC please keep comment here to allow auto update -->
   <!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->





* `The Command Line <#the-command-line>`_

  * `Why use the command line? <#why-use-the-command-line>`_
  * `What is my command line? <#what-is-my-command-line>`_
  * `Basic Commands <#basic-commands>`_

* `Using the Interactive Tutorials <#using-the-interactive-tutorials>`_

  * `Fork the Repository <#fork-the-repository>`_
  * `Clone Your Repository <#clone-your-repository>`_


.. raw:: html

   <!-- END doctoc generated TOC please keep comment here to allow auto update -->



The Command Line
================

A **Command Line Interface (CLI)**\ , or command line is a program in which you type and enter *commands* to interact with your computer. Compare this to a **Graphical User Interface (GUI)**\ , which you use in nearly every other program on your computer.

Why use the command line?
-------------------------

**To use Git and the interactive tutorials.**

While there are ways to use Git in a GUI, using Git in the command line offers much more control. Furthermore, it's much easier to transition from command line to GUI than from GUI to command line.

Using the command line is usually intimidating at first, but it doesn't have to be! When in doubt:


#. *Read* the messages that the command line is putting out.
#. *Adding ``--help``\ * to the end of your commands will usually show help on how to use them.
#. If you get error messages or don't know how to do something, *search* them online. Chances are that someone else has faced the same problem as you in the past!

What is my command line?
------------------------

For *MacOS and Linux*\ , the command line is called **Terminal**.

For *Windows*\ , the command lines are called **PowerShell** and **Command Prompt**. While Command Prompt is more widely known and used, PowerShell is more powerful and uses the same commands as Terminal. For the rest of these tutorials, **please use PowerShell**.

Basic Commands
--------------

The command line functions much like **Finder** or **Windows Explorer** in that you can look through your computer's files and make changes to them:


* ``ls``\ : **lists** all of the files and folders in the folder you're currently in.
* `cd`: **changes** the **directory** (folder) that you're in. You must add one of the following options after `cd`:

  * ``subdirectory-name/``\ : goes *down* into the specified subdirectory.
  * ``..`` : goes *up* into the superdirectory of your current directory.


.. raw:: html

   <!-- TODO: add a screen recording of using ls and cd. -->



These are the only commands that you'll need for now - if you make a mistake or need help, *keep a file explorer next to your command line* to make sure that you're using the command line correctly.

Using the Interactive Tutorials
===============================

Fork the Repository
-------------------

You need to first create a *fork*\ , or copy, of the original ``aguaclara_tutorial`` repository - we wouldn't want everyone editing the same tutorials!


#. On the original `\ ``aguaclara_tutorial`` repository <https://github.com/AguaClara/aguaclara_tutorial>`_\ , click "Fork" and then choose your Github account.

   * If you haven't made one yet, `create a Github account <https://github.com/join?source=header-home>`_.

#. Under the green "Clone or Download" button, *copy* the URL. 

Clone Your Repository
---------------------

Now we'll *clone*\ , or download, the repository that you just forked.


#. Open your *command line*.
#. Enter ``ls``

   * The command line starts in your "home" directory, which should contain folders like ``Desktop/``\ , ``Documents/``\ , ``Pictures/``\ , etc.

#. If you'd like to put the *Interactive Tutorials* elsewhere, use ``ls`` and ``cd`` to get to your preferred directory.
#. Enter ``git clone``\ , a space, and then the URL that you copied above.

   * The command should look like ``git clone https://github.com/<yourusername>/aguaclara_tutorial.git``
   * Git should begin downloading your ``aguaclara_tutorial`` repository to your current directory.


.. raw:: html

   <!-- TODO: Add a screen recording of cloning the repo. -->



**Congratulations, you've completed the `Installing Software <https://github.com/AguaClara/aguaclara_tutorial/wiki/Installing-Software>`_ section!**

**Now, continue with the `Atom and Markdown <https://github.com/AguaClara/aguaclara_tutorial/wiki/Atom-and-Markdown>`_ section.**
