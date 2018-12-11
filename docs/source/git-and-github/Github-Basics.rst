.. role:: raw-html-m2r(raw)
   :format: html


Updating Your Profile
=====================

When you log in to GitHub, click on the icon in the top right. There should be a dropdown which has "Your profile" as one of the first options. Click there and then you'll be able to modify your profile settings. Please fill in your real name so that we will be able to quickly recognize who we're assigning issues to. After that feel free to change your settings however you'd like. Make sure to click the green update profile button at the bottom so the changes are saved.

Repositories
============

Creating a Repository
---------------------

Creating a repository is simple. We'll do this through the `GitHub Website <https://www.github.com>`_. First go to the `AguaClara Team Page <https://github.com/AguaClara>`_.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/AguaClaraHome.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/AguaClaraHome.png
   :alt: AguaClaraHomePage


Now click on the green ``New`` button, and this will direct you to a repository creation page. Each subteam lead should create a repository with the name of their subteam. Put in a description of what your subteam does and check the create a README box. Now go ahead and click the green ``Create repository`` button.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/CreateRepo.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/CreateRepo.png
   :alt: CreateRepository


Cloning a Repository
--------------------

Once you've created a repository, you'll want to show your subteam members how to create a copy of it on their computers so that they'll be able to push and pull.
This is done by cloning the repository. Let's all clone the aguaclara_tutorial repository so that you get the hang of it. First go to the `repository <https://github.com/AguaClara/aguaclara_tutorial>`_ and click on the green ``Clone or Download`` button. Copy the URL shown. Then open Atom and press ``Cmnd + Shift + P`` on mac, or ``Cntrl + Shift + P`` and search for ``GitHub: Clone``. Paste the URL into the ``Clone From`` box and put the path to your GitHub folder, e.g. for me it's ``Users/Fletch/Documents/GitHub/aguaclara_tutorial``\ , in the ``To directory`` box.
`Here <https://knowledge.autodesk.com/community/screencast/cd8c1cb7-511e-45aa-a7b6-7af02b868bd0>`_ is a video demonstrating this.

Watching a Repository
---------------------

When you create or join a repository, you'll want to watch it. This means that every time someone posts an issue, you'll be notified of what they said. To make sure you get these notifications, you'll want to make sure you receive email notifications in your profile settings. To watch a repository, simply click the eyeball button at the top of your repository as shown below.

[[/Images/WatchRepo.png|WatchRepository]]

Editing a Wiki
==============

Once you've created and cloned your repository the wiki will be created automatically. Simply open your repository and click on the ``Wiki`` button in the top bar and you'll open your wiki. From there you have a few options. You can click ``Edit`` to modify the current page in the browser or ``Clone this wiki locally`` so that you'll be able to edit the wiki in a Markdown file in Atom. To create multiple pages just use the ``New Page`` button.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/GitHubTopBar.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/GitHubTopBar.png
   :alt: TopBarTest


Creating an Issue
=================

Creating an issue is as simple as editing the wiki. Just go to the ``Issues`` section on the top bar and then click ``New issue``. Let's call the first issue for each subteam "Update the wiki". You should put a good enough description of the issue so that anyone could read it and begin working on the problem. Attaching images can help explain the issue better. You can also assign people to the issue and add it to a project (more on that later) on the right side.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/NewIssue.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/NewIssue.png
   :alt: NewIssue


Creating a Project
==================

First go to the ``Projects`` section of the top bar, then click ``Create a project``. Now name your project and add a description. You can change the project template through the dropdown, but for the task map we'll use the blank template.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/TaskMap.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/TaskMap.png
   :alt: TaskMap


You can edit the columns to have whatever organization you'd like, but if you're not sure what would work best we'd suggest trying the example above. Once the columns are created, just click ``+ Add cards`` to search through the issues associated with your subteam's repository and add them to the project board.

GitHub for Atom
===============

Perhaps the best part of Atom is GitHub integration, which comes installed with Atom. This means there's no extra steps to install Git or GitHub packages! The beauty of GitHub integration is that all of your GitHub actions can be done through a GUI in the Atom IDE, which circumvents the need to install GitHub desktop or learn the tedious Command Shell or Terminal Git commands. To learn more about how to use the GitHub integration, check out the `GitHub Basics Wiki <https://github.com/AguaClara/aguaclara_tutorial/wiki/Tutorial:-GitHub-Basics>`_ within aguaclara_tutorial. This page also has useful information about the different GitHub terminology and how to use GitHub in Atom.

How to use GitHub in Atom
=========================

The wonderful part about Atom is that GitHub is integrated directly into it. The GitHub GUI in Atom makes all of the Git commands easy to use.

Adding a project folder
-----------------------

Before you can start working on a project, you'll have to add the project folder to Atom. Project folders are the same things as repositories, so every time you add a project folder, you're adding the entire repository to Atom. To add a project forlder, use ``Cmnd + Shift + O`` or ``Cntrl + Shift + O``\ , and navigate to the repository you wish to work out of. Your project will then appear in a side bar within the Atom interface. Clicking on it enables you to open any file within the repository.

:raw-html-m2r:`<img src="https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/GitProject.png" height=600>`

Navigating branches
-------------------

On the bottom right hand corner of Atom, there's a toolbar with many different icons. One of them shows what branch your file is in within a given repository. It should look something like this:


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/Branch.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/Branch.png
   :alt: Branch


Clicking on that icon will being up a window that allows you to switch branches and create a new branch.

.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/SwitchNewBranch.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/SwitchNewBranch.png
   :alt: SwitchNewBranch


Pushing and pulling
-------------------

On the same toolbar as the branch icon, there's an icon that enables you to push, pull, or fetch. It looks like this:


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/PushPullIcon.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/PushPullIcon.png
   :alt: PushPullIcon


Clicking on it will give you a window to push or pull.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/PushPullWindow.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/PushPullWindow.png
   :alt: PushPullWindow


Committing
----------

To open the GitHub commit GUI, use ``Cntrl + Shift + 9``\ , or find it in ``Toggle Git Tab`` within ``GitHub`` under the ``Packages`` tab in the menu bar. The GUI looks like this:

:raw-html-m2r:`<img src="https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/GitGUI.png" height=700>`

When you save a file that's in one of the repositories your working on using ``Save As``\ , ``Cmnd + S``\ , or ``Cntrl + S``\ , the file name will appear uder the ``Unstaged Changes`` tab. In order to commit your files, you first have to stage them either using the ``Stage All`` button or selecting the files you want to stage and staging them using a right click on the file name. Once you've done that, the files will appear under ``Staged Changes``.

You won't be able to commit your file until you write your ``Commit message``\ , so make sure you fill it out with detailed info about the changes made to the files. Once you've filled out your message, you can click ``Commit``. After committing, you're ready to push!

If you ever want to modify a commit, click ``Ammend``\ , and you can change anything you want about the last commit you made.

Resolving Merge Conflicts
=========================

Most of you probably won't have merge conflicts, but if you do they're easy to resolve in Atom. When a merge conflict occurs during a push, Atom will pop up ``Use me`` buttons like in the picture below, and simply click on the button for the code block you'd like to keep.


.. image:: https://user-images.githubusercontent.com/401128/27737141-6f7ae2f6-5d7d-11e7-9312-87c8611e7328.png
   :target: https://user-images.githubusercontent.com/401128/27737141-6f7ae2f6-5d7d-11e7-9312-87c8611e7328.png
   :alt: MergeConflict

