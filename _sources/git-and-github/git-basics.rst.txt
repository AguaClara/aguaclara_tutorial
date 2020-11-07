.. _git-basics:

**********
Git Basics
**********

Git Terminology
===============

The purpose of GitHub is to allow multiple people to work on a coding project and maintain consistency. In order to accomplish this, Git employs a number of tools such as pull, push, commit, and merge conflicts which are explained below. To aid(e) in this explanation let's imagine that AguaClara is a company which owns a chain of sandwich restaurants.

Repository
----------

A repository is like a folder in Git. If AguaClara were a restaurant chain, then each individual restaurant would be a repository. You can save many associated files in a repository and give specific users permission to edit the files in the repository. There are a number of repositories on the AguaClara GitHub including this one, aguaclara_tutorial.

Branches and Forks
------------------

A repository can have a number of different branches and forks. These branches allow different people to make edits to the code without disrupting each other. This is sort of like how one chef could be working on a BLT while another scooped ice cream (for the record, an ice cream cone is a sandwich). Then at the end the branches can be merged together. If some of the ice cream melted onto the BLT then there might be a merge conflict which needs to be resolved (this is explained in more detail below). Most research teams will use only a single branch, the master.

Clone
-----

When you first want to access a repository locally you'll have to clone it. By cloning the repository you make a local copy to which you'll be able to pull updates from online and push your changes to the repository. If pulling and pushing don't make sense yet don't worry, just read the sections below. As for a sandwich analogy, imagine that a restaurant has the recipe for making a BLT and you wanted the recipe as well to make your own BLT. This way, both you and the restaurant have the exact same BLT recipe. However, if you modify your copy of the recipe, this does not affect the restaurant's original BLT recipe.

Pull
----

A pull request takes the most recent version of whatever branch you're in and downloads it onto your computer. Basically the chef double checks the recipe for his sandwich and updates it accordingly. Then from there he can modify the sandwich from the most recent recipe in order to minimize conflicts.

Commit
------

Once the chef creates a new sandwich and taste tests it, she'll want to save the recipe so that she can recreate the sandwich. In computer terms, a commit is saving the changes you've made locally, and it's important to commit before pushing any changes to a repository. How could you publish a recipe for others to use if you never write it down, right?

Push
----

Now that the chef has written down the recipe, she will want to update the restaurant's recipe. Updating the branch on GitHub is accomplished through a push. Once a push occurs, other chefs will be able to pull request the most updated recipe so they can try the delicious sandwich and modify it themselves.

Merge Conflicts
---------------

Now let's say two chefs were working on changing the recipe for the same sandwich simultaneously. One decides to add cheese to the BLT, while the other doesn't like tomato so he takes that out and puts in avocado instead. When they go to publish the recipe (push), the restaurant manager won't know which recipe to use. This is called a merge conflict. How a merge conflict is resolved is explained in more detail `here <https://help.github.com/en/articles/resolving-a-merge-conflict-using-the-command-line>`_.
