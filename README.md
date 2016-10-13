``ansicolortags``
=================

[ansicolortags, a Python script and module](https://pypi.python.org/pypi/ansicolortags) to simply and efficiently use ANSI colors in a command line Python program.
[![ansicolortags in pypi](https://img.shields.io/pypi/v/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags)

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

For instance, the screenshot below shows the module begin used to print a colored text (the help of the script) which looks like this:

[![Screenshot of the doc, colored with the script](examples/help.png "Screenshot of the doc, colored with the script")]((http://ansicolortags.readthedocs.io/?badge=latest))

[![PyPI version](https://img.shields.io/pypi/v/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI format](https://img.shields.io/pypi/format/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI implementation](https://img.shields.io/pypi/implementation/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

----

### Author?
[Lilian Besson](https://bitbucket.org/lbesson/).

### Language?
Python v2.7+ or Python v3.1+.

This project is hosted on [the Pypi package repository](<https://pypi.python.org/pypi/ansicolortags> "Pypi !").

Documentation
-------------

[![Documentation on ansicolortags.readthedocs.io](https://readthedocs.org/projects/ansicolortags/badge/?version=latest "Documentation on ansicolortags.readthedocs.io")](http://ansicolortags.readthedocs.io/?badge=latest)
[![ansicolortags in pypi](https://img.shields.io/pypi/v/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags)

The complete documentation of the module is available, see [here on readthedocs.io](<http://ansicolortags.readthedocs.io/> "on-line").

**All the details (installation, options, etc) are in the doc**.
Anyway, here are some information.

----

Installation ?
==============

The project consists in just the main script [``ansicolortags.py``](ansicolortags.py).

How to install it
-----------------

[Download the archive](https://bitbucket.org/lbesson/ansicolortags.py/downloads/ansicolortags-0.4.tar.gz) from this git repository, extract it, then launch ``python setup.py install`` in the directory.

More details can be found in the [INSTALL](INSTALL) file.

[![PyPI download total](https://img.shields.io/pypi/dt/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI download month](https://img.shields.io/pypi/dm/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI download week](https://img.shields.io/pypi/dw/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI download day](https://img.shields.io/pypi/dd/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

Dependencies
------------

The project is entirely written in Python, compatible with both version 2.7+ and 3.1+.

For more details about the **Python** language, see [the official site](<https://www.python.org> "Python power !").

Platforms
---------

The project have been developed on *GNU/Linux* (Ubuntu 11.10 to 15.10).

#### Warning : Windows ?
It also have been quickly tested on *Windows 7* with the Cygwin environment and Python 2.7.

#### Warning : Mac OS X ?
It should also work on *Mac OS X*, but not been tested.
Any [feedback](http://perso.crans.org/besson/contact/en/) on this is welcome!

[![PyPI version](https://img.shields.io/pypi/v/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI format](https://img.shields.io/pypi/format/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI implementation](https://img.shields.io/pypi/implementation/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

Contact me
----------

Feel free to contact me, with a Bitbucket message (my profile is [lbesson](https://bitbucket.org/lbesson/ "here")), or via an email at **lilian DOT besson AT ens-cachan DOT org**.

## :scroll: License ? [![GitHub license](https://img.shields.io/github/license/Naereen/ansicolortags.py.svg)](https://github.com/Naereen/ansicolortags.py/blob/master/LICENSE)
This plug-in is published under the terms of the [MIT license](http://lbesson.mit-license.org/) (file [LICENSE.txt](LICENSE.txt)),
© [Lilian Besson](https://GitHub.com/Naereen), 2016.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/ansicolortags.py/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/ansicolortags.py/README.md?pixel)](https://GitHub.com/Naereen/ansicolortags.py/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)
