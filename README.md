ansicolortags
=============

[ansicolortags, a Python script and module](https://pypi.python.org/pypi/ansicolortags) to simply and efficiently use ANSI colors in a command line Python program.


The ``ansicolortags`` module provides an efficient and useful function
(``printc``) to print colored text in a terminal application with Python 2 and 3, with a *HTML-tag* like style:

```python
from ansicolortags import printc  # Import the function
# ...
printc("France flag is <blue>blue<reset>, <red>red<reset>, and <white>white<reset> !")
```

will print the text *"France flag is blue, white and red !"* with appropriate colors (if the output supports them -- a terminal should but a file or a pipe should not).


All ANSI colors code are defined with this *HTML-tag like style*: ``<blue>``, ``<red>`` etc.
**This point is the main interest of this module,**
because all others modules define function to print with some colours.


[![Documentation on ansicolortags.readthedocs.io](https://readthedocs.org/projects/ansicolortags/badge/?version=latest "Documentation on ansicolortags.readthedocs.io")](http://ansicolortags.readthedocs.io/?badge=latest)


For instance, the screenshot below shows the module begin used to print a colored text (the help of the script) which looks like this:

[![Screenshot of the doc, colored with the script](examples/help.png "Screenshot of the doc, colored with the script")]((http://ansicolortags.readthedocs.io/?badge=latest))

----

### Author?
[Lilian Besson](https://bitbucket.org/lbesson/).

### Language?
Python v2.7+ or Python v3.2+.

This project is hosted on [the Pypi package repository](<https://pypi.python.org/pypi/ansicolortags> "Pypi !").

Documentation
-------------

The complete documentation of the module is available, see [here on readthedocs.io](<http://ansicolortags.readthedocs.io/> "on-line").

A short documentation is also available [here on pydoc.net](http://pydoc.net/Python/ansicolortags/0.1/#description).

**All the details (installation, options, etc) are in the doc**.
Anyway, here are some information.

----

Installation ?
==============

The project consists in just the main script [``ansicolortags.py``](ansicolortags.py).

How to install it
-----------------

[Download it](https://bitbucket.org/lbesson/ansicolortags.py/raw/master/ansicolortags.py) or copy it from this git repository, then launch ``python setup.py install``.
More details can be found in the [INSTALL](INSTALL) file.

Dependencies
------------

The project is entirely written in Python, compatible with both version 2.7+ and 3.2+.

For more details about the **Python** language, see [the official site](<https://www.python.org> "Python power !").

Platforms
---------

The project have been developed on *GNU/Linux* (Ubuntu 11.10).

#### Warning : Windows ?
It also have been quickly tested on *Windows 7* with the Cygwin environment and Python 2.7.

#### Warning : Mac OS X ?
It should also work on *Mac OS X*, but not been tested.
Any [feedback](http://perso.crans.org/besson/contact/en/) on this is welcome!

Contact me
----------

Feel free to contact me, either with a bitbucket message (my profile is [lbesson](https://bitbucket.org/lbesson/ "here")), or via an email at **lilian DOT besson AT ens-cachan DOT org**.

License
-------

This project is released under the [MIT License](https://lbesson.mit-license.org/).
