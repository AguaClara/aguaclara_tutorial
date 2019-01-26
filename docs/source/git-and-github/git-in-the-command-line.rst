.. _git-in-the-command-line:

***********************
Git in the Command Line
***********************

What is Git?
============

Git is a free and open source control system used for managing projects through Github.  Every time you push or pull your work through Atom, Atom is running Git commands to facilitate this.

**Note:** This tutorial assumes some knowledge of the basic commands of Github.  To refresh on those, refer to :ref:`github-basics`

Why use Git at all?  Why not just use Atom?
===========================================

Running Git offers a new level of flexibility for managing your repositories in Github.  Where in Atom, you can only push and pull, using Git from the command line offers up many new possible commands to help you manage your project.  Atom also can have many internal errors, so knowing Git allows you to work on your projects even when Atom is not cooperating.

Installing Git
==============

To install Git, follow the instructions on `this page <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_.  For Windows, when installing Git through the installer, it is recommended you select the "Use Git from the Windows Command Prompt" option.  This will allow you to use all git commands through your terminal (CMD, Powershell, Anaconda) rather than having to use Git's personal terminal, Git Bash.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git1.PNG
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git1.PNG
   :alt: 


Using the Command Line
======================

If you are already familiar with using the command prompt, feel free to skip this section.  

The command prompt/terminal is another way of interfacing with your computer, rather than the way you typically would use a computer by clicking different buttons.  While the terminal can be confusing at first, and requires some memorization of some commands, it provides a lot of power for using your computer in different ways.  Knowing how to use the terminal opens a lot of new doors and can ultimately make using your computer much easier and more accessible. 

Note that there are a few terminal options for Windows, such as CMD, Windows Powershell, and the Anaconda Prompt.  This tutorial will use Powershell, as it is most similar to the Mac terminal, and has all the necessary functionality.  However, all the other terminal options should accomplish everything you want, just with slightly different commands.

To open your terminal in Windows, search for "Powershell" in your programs.  On Mac, just search for "Terminal" in your programs.  A prompt like the one below should open up.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git2.PNG
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git2.PNG
   :alt: 


Within this prompt, you will run commands by typing them directly into this prompt and hitting "Enter".  The path listed before the where you type is the directory you are currently working in on your computer.  In order to run commands on a specific folder (such as your subteams repository) you will need to navigate to that folder.  The two commands to do this are:


* ``ls`` (list): Lists all files in the current directory you are in
* ``cd`` (change directory): changes your directory to the directory listed after cd

For example, say I want to move to the "aguaclara_tutorial" repository to make some git changes.  First I use ls to see what files I can change to: 


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git3.PNG
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git3.PNG
   :alt: 


I see the github folder, so I use ``cd github`` to move to that folder.  From there I continue to use these commands until I find the folder I am looking for.

If you ever need to move up one folder, you can use ``cd ..`` to accomplish this.  If you know the file path of the folder you want, you can also add that directly to move to your desired folder.  For example, I could move directly to the aguaclara_tutorial folder as shown below:


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git4.PNG
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git4.PNG
   :alt: 


One other important note for using the terminal is to always wait for the commands to finish running.  Sometimes when running a more complicated command, the computer will take a while to run, and the terminal will slowly show commands as they run.  In this case, make sure to wait until all the commands are done running, and you can see the blinking cursor before you type another command.  If you ever want to stop a command while its running, hold down the control button (or the command button on Mac) and hit c.

Using Git in the command line
=============================

Assuming you added Git to your command line during installation, you can run any Git command from the command line just by typing ``git`` adding a space, and writing the command.  For example, to use the simple command ``git status``\ , which compares your local progress to the digital collection of Github, just type "git status" while in the folder you want to check.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git5.PNG
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git5.PNG
   :alt: 


Pulling
-------

Most of what you will be doing with Git is pulling and pushing changes from Github.  To pull, just use the command ``git pull``.

Pushing
-------

To push your local changes, you will use the same process as you do in atom, staging your changes, committing them to your branch, and then pushing them to the origin.  


* To stage your changes, use ``git add -A`` The -A ensures you add all of your files you have worked on.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git7.PNG
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git7.PNG
   :alt: 



* To commit your changes, use the command ``git commit -m "Commit Message"`` and fill in the commit message with whatever you want to say about your commit.  Note that it is very important to include the -m and the commit message.  If you do not, Git will take you to an interface using the text editor Vim, which is very challenging to use.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git10.PNG
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git10.PNG
   :alt: 


Write your commit message, then to exit out of this editor, press Escape.  You cursor should appear in the bottom left corner.  From there type ``:x`` and hit enter to save your commit message.


* Finally, to push your changes, use ``git push``.  If you have any merge errors, the terminal will notify you and you can go fix them in Atom like you would normally.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git5.PNG
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Git-and-Github/Images/git5.PNG
   :alt: 


**Note:** This tutorial only covers the basics of using Git.  For the full list of commands, `view the full documentation here <https://git-scm.com/doc>`_
