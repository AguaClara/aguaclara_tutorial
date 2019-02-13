.. _installing-on-windows:

*********************
Installing on Windows
*********************

Atom & Sync Settings
====================


#. Download the `Atom installer <https://atom.io/>`_ and double-click it to begin installation. Atom should open up once it's installed.
#. Open Atom settings by going to File > Settings (or Control + Comma).
#. Go to Install and search for ``sync-settings``. Click on the blue Install button in the ``sync-settings`` box.
#. Once it's done installing, click on the Settings button in the ``sync-settings`` box.
#. Create a new `Github personal access token <https://github.com/settings/tokens/new>`_. You may set the name to anything you'd like, but we recommend that you call it something descriptive, like "aguaclara-atom-configuration".
#. Check the "\ **gist**\ : Create gists" permission, then click Generate Token. Copy the generated token.
#. In the Atom ``sync-settings`` settings, paste your generated token in Personal Access Token.
#. Set the Gist Id to ``8cb1fed2721e41873e9bcb315c804579``.

   * This synchronizes your Atom settings and plug-ins with the required `AguaClara Atom configuration <https://gist.github.com/ethan92429/8cb1fed2721e41873e9bcb315c804579>`_.

#. Restart Atom. ``sync-settings`` will do its job in the background. You can check on its progress in File > Settings > Packages.

   * If you get a dialog box saying that ``sync-settings`` is out of date, click "Restore".

.. _installing-on-windows-git:

Git
===


#. Download the `Git installer <https://git-scm.com/downloads>`_ and double-click it to begin installation.
#. When the installer asks which text editor you would like to use with Git (the default is Vim), select Nano instead. While powerful, Vim is difficult to use and not necessary for Git.

   * Aside from this, you can just click "Next" through the entire installation.

#. After the installation is complete, open **PowerShell** or **Command Prompt**.
#. Run the two following commands with your name and Cornell email, carefully observing spaces and punctuation:

   * ``git config --global user.name "Firstname Lastname"``
   * ``git config --global user.email "NetID@cornell.edu"``

     * The quotation marks are important! For example, the command should say something like ``git config --global user.name "Monroe Weber-Shirk"``.

Anaconda & Python
=================


#. Download the `Anaconda installer <https://www.anaconda.com/download/>`_ and double-click it to begin installation.
#. When the installer displays Advanced Options, select "Add Anaconda to my PATH environment variable".

   * Aside from this, you can just click "Next" through the entire installation.

\* If the installer did not give the option to "Add Anaconda to my PATH environment variable", follow the steps below after the installation:
  * Open **Terminal** and enter ``which python``
  * Copy the directory the terminal outputs. (This is the directory Python has been installed in.)
  * Enter the command ``export PATH=$PATH<directory>``, replacing ``<directory>`` with the directory you copied above.

``pip`` Packages
====================


#. Open **PowerShell** or **Command Prompt**\ , as you did when installing :ref:`installing-on-windows-git`.
#. Run the following command, carefully observing spaces and punctuation:

   * ``pip install aguaclara --user``
      * If you get the error ``bash: pip: command not found``, follow the steps in the **Anaconda and Python** section after the asterisk.

**Now, you're ready for** :ref:`installing-interactive-tutorials`.
