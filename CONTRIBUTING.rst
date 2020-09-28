.. highlight:: shell

============
Contributing
============

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/sp-fm/fuse-utils/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs that are tagged with "bug".

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features that are tagged with "enhancement".

Write Documentation
~~~~~~~~~~~~~~~~~~~

Fusemachines Utilities could always use more documentation, whether as
part of the official Fusemachines Utilities docs, in docstrings, or
even on the web in blog posts, articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/sp-fm/fuse-utils/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.

Get Started!
------------

Ready to contribute? Here's how to set up `fuse-utils`
for local development. Please note this documentation assumes you already have
`poetry` and `git` installed and ready to go.

#. Clone the `fuse-utils` repo locally:

   .. code-block:: console

        $ git clone git@github.com:sp-fm/fuse-utils.git

#. Assuming you have poetry installed, you can create a new environment for your
   local development by typing:

   .. code-block:: console

        $ poetry shell
        $ poetry install

#. Create a branch for local development:

   .. code-block:: console

        $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

#. When you're done making changes, check that your changes pass flake8. Since,
   this package contains mostly templates the flake should be run for tests
   directory:

   .. code-block:: console

        $ flake8 ./tests

#. The next step would be to run the test cases. `fuse-framework` uses pytest,
   you can run PyTest. Before you run pytest you should ensure all dependancies
   are installed:

   .. code-block:: console

        $ poetry install
        $ pytest ./tests

#. Before raising a pull request you should also run tox. This will run the
   tests across different versions of Python:

   .. code-block:: console

        $ tox

   If you are missing flake8, pytest, and/or tox, just `poetry add` them into
   your virtualenv.

#. If your contribution is a bug fix or new feature, you may want to add a test
   to the existing test suite. See section Add a New Test below for details.

#. Commit your changes and push your branch to GitHub:

   .. code-block:: console

        $ git add .
        $ git commit -m "Your detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature

#. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

#. The pull request should include tests.

#. If the pull request adds functionality, the docs should be updated. Put your
   new functionality into a function with a docstring, and add the feature to
   the list in README.rst.

#. The pull request should work for Python 3.7 and 3.8. Check
   https://travis-ci.com/sp-fm/fuse-utils/pull_requests
   and make sure that the tests pass for all supported Python versions.

Add a New Test
--------------

When fixing a bug or adding features, it's good practice to add a test to
demonstrate your fix or new feature behaves as expected. These tests should
focus on one tiny bit of functionality and prove changes are correct.

To write and run your new test, follow these steps:

#. Add the new test to `tests/test_fuse_utils.py`. Focus
   your test on the specific bug or a small part of the new feature.

#. If you have already made changes to the code, stash your changes and confirm
   all your changes were stashed:

   .. code-block:: console

        $ git stash
        $ git stash list

#. Run your test and confirm that your test fails. If your test does not fail,
   rewrite the test until it fails on the original code:

   .. code-block:: console

        $ pytest ./tests

#. (Optional) Run the tests with tox to ensure that the code changes work with
   different Python versions:

   .. code-block:: console

        $ tox

#. Proceed work on your bug fix or the new feature or restore your changes. To
   restore your stashed changes and confirm their restoration:

   .. code-block:: console

        $ git stash pop
        $ git stash list

#. Rerun your test and confirm that your test passes. If it passes,
   congratulations!

Deploying
---------

A reminder for the maintainers on how to deploy. Make sure all your changes are
committed (including an entry in CHANGELOG.rst). Then run:

   .. code-block:: console

         $ poetry version patch
         $ git tag `poetry version -s`
         $ git push --tags

Travis will then deploy to PyPI if tests pass.
