eval.workspace Installation
---------------------

To install eval.workspace using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``eval.workspace`` to the list of eggs to install, e.g.:

    [buildout]
    ...
    eggs =
        ...
        eval.workspace

* Re-run buildout, e.g. with:

    $ ./bin/buildout

