#!/usr/bin/env python
# -*- coding: utf-8; mode: python -*-

from distutils.core import setup
import ansicolortags

setup(name='ansicolortags',
      version=ansicolortags.__version__,
      description='ansicolortags brings a simple and powerful way to use colours in a terminal application with Python 2 and 3.',
      long_description="""
About
=====

The ``ansicolortags`` module provides *efficient* and useful functions to use colours, in a *HTML-tag* like style : ``<red>text<white>`` will put ``text`` in red.

All ANSI colors code are defined with this tag-like style.
**This point is the main interest of this module,**
because all others modules define function to print with some colours.

The ``reset`` tag is a special tag to reinitialize all previously changed parameters.

Colours
=======

Foregrounds
-----------

You can choose one of the 8 basic ANSI colours: black, red, green, yellow, blue,
magenta, cyan, white.
The names beginning with a *lowerscript* design **foreground** colours.

For example ::

 ansicolortags.printc('<reset>This is default. <red>This is red<yellow> and yellow in foreground now<reset>').

Backgrounds
-----------

You can choose one of the 8 basic ANSI colours: Black, Red, Green, Yellow, Blue,
Magenta, Cyan, White.
The names beginning with a *upperscript* design **background** colors.

For example ::

 ansicolortags.printc('<Default>this is default. <Blue>this have a blue background<Black> and black in background now<reset>').

Other tags
-------------

The following tags are also available :
 * ``italic``, ``Italic`` : to turn on and off the *italic* mode (not always supported),
 * ``b``, ``B`` : to turn on and off the *bold* mode (not always supported),
 * ``u``, ``U`` : to turn on and off the *underline* mode (not always supported),
 * ``neg``, ``Neg`` : to turn on and off the *reverse video* mode,
 * ``blink``, ``Blink`` : to turn on and off the *blink* mode (not always supported),
 * ``el`` : to erase the current line,
 * ``bell`` : to make the terminal's bell ring (not always supported).

Macros
------

Some macros are also provided, like the tags ``<ERROR>``, ``<INFO>`` or ``<WARNING>``.

And also ``<warning>`` and ``<question>``, which respectively give a colored ``!`` and ``?``.

Writing to a file
-----------------

This is possible with the ``writec`` function. For example ::

 import sys
 ansicolortags.writec('<ERROR><u><red>The computer is going to explode!<reset>', fn=sys.stderr)
 # sys.stderr.flush()
 # this is useless : writec flush itself.

Auto detection
==============
Of course, the colors are disabled if the output does not support them.

It works perfectly on GNU/Linux (Ubuntu 10+) and Windows (with or without Cygwin),
and should work fine one MAC OS X or on other UNIX-like.

Other features
==============

Other functions
---------------

There is also the ``xtitle`` function, to change the title of the terminal.
This try to use the command-line tool ``xtitle``, and if it fails it tries to use an *ANSI code* to change the title.

There is also a ``notify`` function to display a system notification (using the command-line tool ``notify-send``).

Script
------

``ansicolortags.py`` is also a script.
You can have his description (or use it) directly with: ::

    python -m ansicolortags --help

For testing
~~~~~~~~~~~

It can be used to run some tests (with the ``--test`` option).

With GNU/Bash
~~~~~~~~~~~~~

It can be used to generate a GNU/Bash colour profile
(with the ``--generate --file colour.sh`` options).

This ``sh`` file can be imported with ``$ . colour.sh`` in any GNU/Bash scripts, or even in your ``~/.bashrc`` file.

License ?
=========

This module is licensed under the term of the **MIT License**, see the file *LICENSE* for more details.
""",
      author='Lilian Besson',
      author_email='naereen@crans.org',
      url='https://bitbucket.org/lbesson/ansicolortags',
      download_url='https://bitbucket.org/lbesson/ansicolortags',
      license='MIT',
      platforms=['Windows', 'Windows Cygwin', 'GNU/Linux'],
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: User Interfaces',
          'Topic :: Terminals',
          'Topic :: Utilities'
      ],
      py_modules=['ansicolortags'],
      )

# End of setup.py
