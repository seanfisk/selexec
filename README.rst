=========
 selexec
=========

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
