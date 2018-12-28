.. _contributing-to-the-tutorial:

****************************
Contributing to the Tutorial
****************************


I want a new tutorial...
========================

...and I'll write it.
---------------------


#. ``git clone https://github.com/AguaClara/aguaclara_tutorial.wiki.git``
#. The repo contains folders for each tutorial section. Decide whether you would like to *add to an existing section or make a new section*.

   * **To add a new section**\ : Make a new folder and Markdown file, both named after the new section. The Markdown file should briefly explain the purpose/contents of the new section.


.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/NewTutorialSection.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/NewTutorialSection.png
   :alt: New Section
 
.. image:: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/NewSectionMarkdown.png
   :target: https://github.com/AguaClara/aguaclara_tutorial/wiki/Images/NewSectionMarkdown.png
   :alt: New Section's Markdown



#. Your new tutorial's ``File-Name.md`` should *properly capitalized with dashes instead of spaces*. This **File Name** will be the displayed page title on the wiki.
#. Write your tutorial like how you'd write a report:

   * *Define any terms* that may be new to the reader.
   * *Write with brevity*\ , but don't oversimplify concepts.

#. **To add images**\ , use URL links:

   #. Add your images to the ``<Your-Section>/Images/`` folder, or make a new ``Images`` folder if it doesn't exist yet.
   #. Be sure that the ``Image-Name.jpeg`` is *properly capitalized with dashes instead of spaces*\ , like the Markdown file.
   #. ``![](https://github.com/AguaClara/aguaclara_tutorial/wiki/FILE-PATH/OF-IMAGE.jpeg)``

#. *Push* your changes to the `wiki <https://github.com/AguaClara/aguaclara_tutorial/wiki>`_. In the Pages dropdown in the sidebar, *check to see if your tutorial looks good*.
#. `Open an issue <https://github.com/AguaClara/aguaclara_tutorial/issues/new>`_ on the ``aguaclara_research`` repo with the title "Add \<Tutorial Name&gt; tutorial", and explain its contents.

   * *Label* it as ``addition`` and ``medium priority``.

#. Once the tutorial has been reviewed and accepted, it will appear in the wiki's sidebar.

...but I don't know how to write it.
------------------------------------


#. `Open an issue <https://github.com/AguaClara/aguaclara_tutorial/issues/new>`_ on the ``aguaclara_research`` repo with the title "Add \<Requested Tutorial Name&gt; tutorial", and *explain what you'd like to see in it*.

   * *Label* it as ``addition`` and ``low priority``.
   * If you know someone who would be good at writing this tutorial, *assign* the issue to them.

#. Once the tutorial has been written, reviewed, and accepted, it will appear in the wiki's sidebar.

I want to change...
===================

...an existing tutorial.
------------------------


#. ``git clone https://github.com/AguaClara/aguaclara_tutorial.wiki.git``
#. ``git branch change-<tutorial-name>`` (In the repo)
#. *Make your changes* to the tutorial.
#. *Push your changes* to the `wiki <https://github.com/AguaClara/aguaclara_tutorial/wiki>`_.
#. `Open an issue <https://github.com/AguaClara/aguaclara_tutorial/issues/new>`_ on the ``aguaclara_research`` repo with the title "Change \<Tutorial Name&gt; tutorial", and *explain the changes you made*.

   * *Label* it as ``enhancement`` and ``low priority``.
   * In the issue, write the exact name of the branch you made.

#. Once the changes have been reviewed and accepted, they will appear in the wiki tutorial.

...how the wiki is organized.
-----------------------------


#. ``git clone https://github.com/AguaClara/aguaclara_tutorial.wiki.git``
#. ``git branch reorganize-<yourNetID>`` (In the repo)
#. *Reorganize the wiki tutorials* how you'd like.
#. *Push your changes* to the `wiki <https://github.com/AguaClara/aguaclara_tutorial/wiki>`_.
#. `Open an issue <https://github.com/AguaClara/aguaclara_tutorial/issues/new>`_ on the ``aguaclara_research`` repo with the title "Reorganize \<section name, if applicable&gt;", and explain the changes you made.

   * *Label* it as ``enhancement`` and ``low priority``.
   * In the issue, write the exact name of the branch you made.

#. Once the changes have been reviewed and accepted, they will appear in the wiki.
