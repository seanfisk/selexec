=========
 selexec
=========

.. image:: https://secure.travis-ci.org/seanfisk/selexec.png
   :target: https://secure.travis-ci.org/seanfisk/selexec

**selexec** provides pipline selection the UNIX way. A simple example
illustrates it best.

Let's say you want to edit a few Python files in your project tree,
but you're not sure *which ones* you'd like to edit without seeing
them. Normally, you might run the following:

.. code-block:: bash

    $ find . -name '*.py'
    eggs/bedevere.py
    eggs/galahad.py
    spam/lancelot.py
    spam/robin.py
    # oh, that's right, I wanted to edit galahad and lancelot
    $ $EDITOR eggs/galahad.py spam/lancelot.py

There's a bit of extra typing in the second command, which involves
*re-typing* the names of the files. Why not just select them from the
already-produced list? With **selexec**, you can:

.. code-block:: bash

    $ find . -name '*.py' | slxc | xargs $EDITOR

The ``slxc`` command takes a list on standard input. It will then
bring up an interface which allows you to select one, many, or all
items in the list. Once the choice is made, the truncated list will be
echoed to standard output.

**selexec** is not limited to files only. Let's say you wanted to
uninstall a couple plugins for pytest_, but weren't sure of their
names. It's pipeline time!

.. code-block:: bash

    $ pip freeze | grep pytest | slxc | xargs pip uninstall --yes

As you can see, with **selexec**, you can save a lot of time avoiding
retyping items you've already seen.

Enjoy using **selexec**!

.. _pytest: http://pytest.org/

-----------
Development
-----------

Run
===

The program can be run locally by following these steps. First install
the requirements::

    pip install -r requirements/dev.txt

Then run with the current directory on the ``PYTHONPATH``:

.. code-block:: bash

    PYTHONPATH=$PWD python selexec/console/main.py

Test
====

Tests are written using pytest_ and mock_. To run unit tests and PEP8
enforcement, run::

    shovel test_all

Continuous integration is provided by Travis-CI_. Find the build
status at https://secure.travis-ci.org/#!/seanfisk/selexec.

.. _mock: http://www.voidspace.org.uk/python/mock/
.. _Travis-CI: https://travis-ci.org/

Test Coverage
=============

To view the test coverage report, run::

    shovel coverage

Emacs Tags File
===============

Sean uses Emacs_ to edit code. To easily generate a tags file for
Emacs, run::

    shovel emacs_tags

This command uses `Exuberant Ctags`_ to generate a ``TAGS``
file. Within Emacs, run ``M-x visit-tags-table`` to load the generate
tags file. Then use ido-find-file-in-tag-files_ to find project files.

.. _Exuberant Ctags: http://ctags.sourceforge.net/
.. _Emacs: http://www.gnu.org/software/emacs/
.. _ido-find-file-in-tag-files: http://emacswiki.org/emacs/InteractivelyDoThings#toc11

-------
License
-------

.. image:: http://www.gnu.org/graphics/gplv3-127x51.png
   :target: `GNU General Public License version 3`_

**selexec** is free software licensed under the `GNU General Public
License version 3`_.

.. _GNU General Public License version 3: http://www.gnu.org/licenses/gpl.html#content

-------
Credits
-------

**selexec** makes use of the following libraries/tools/services:

- Python_ programming language
- git_ version control system
- GitHub_ for git hosting
- pytest_ test framework
- mock_ for creating mock objects
- coverage.py_ and pytest-cov_ for test coverage statistics
- pep8_ for enforced PEP8 compliance
- Travis-CI_ for continuous integration
- Sphinx_ and docutils_ for documentation generation
- shovel_ for running miscellaneous tasks

.. _Python: http://python.org/
.. _git: http://git-scm.com/
.. _GitHub: https://github.com/
.. _coverage.py: http://nedbatchelder.com/code/coverage/
.. _pytest-cov: http://pypi.python.org/pypi/pytest-cov
.. _pep8: https://github.com/jcrocholl/pep8/
.. _Sphinx: http://sphinx.pocoo.org/
.. _docutils: http://docutils.sourceforge.net/
.. _shovel: https://github.com/seomoz/shovel

-------
Authors
-------

* `Sean Fisk <mailto:sean@seanfisk.com>`_
* `Ira Woodring <mailto:irawoodring@gmail.com>`_

----
Note
----

**selexec** is inspired by the **vipe** tool in moreutils_ that allows
a user to *insert a text editor into a pipe*. It can be used for much
the same purpose with somewhat greater hassle:

.. code-block:: bash

    $ find . -name '*.py' | vipe | xargs $EDITOR

...which would allow me to edit a list of files I'd like to open in my
editor before actually opening them.

.. _moreutils: http://joeyh.name/code/moreutils/
