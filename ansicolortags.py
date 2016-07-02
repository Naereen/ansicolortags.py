#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
An efficient and simple ANSI colors module (and also a powerful script), with functions to print text using colors.
https://bitbucket.org/lbesson/ansicolortags.py


The names of the colors follow these conventions:

* for the eight ANSI colors (:black:`black`, :red:`red`, :green:`green`, :yellow:`yellow`, :blue:`blue`, :magenta:`magenta`, :cyan:`cyan`, :white:`white`):

  + the name in minuscule is for color **with bold** (example ':yellow:`yellow`'),
  + the name starting with 'B' is for color **without bold** (example ':yellow:`Byellow`'),
  + the name starting with a **capital** letter is for the background color (example ':yellow:`Yellow`').

* for the special effects (:blink:`blink`, *italic*, **bold**, :under:`underline`, negative), they might not always be supported, but they usually are:

  + the name in minuscule is used to turn *on* the effect (example 'i' to turn on italic),
  + the name starting in capital letter is used to turn *down* the effect (example 'I' to turn off italic).

* for the other special effects (``nocolors``, ``default``, ``Default``, ``clear``, ``el``), the effect is **immediate** (and seems to be well supported).


List of functions
=================

To print a string
-----------------

* :py:func:`sprint`: give a string,
* :py:func:`printc`: like :py:func:`print`, but with interpreting tags to put colors. **This is the most useful function in this module !**
* :py:func:`writec`: like printc, but using any file object (and no new line added at the end of the string).

To clean the terminal or the line
---------------------------------

* :py:func:`erase`: erase all ANSI colors tags in the string (like sprint, but erasing and not interpreting color tags),
* :py:func:`clearLine`, :py:func:`clearScreen`: to clear the current line or screen,
* :py:func:`Reset`: to return to default foreground and background, and stopping all *fancy* effects (like blinking or reverse video).

Others functions
----------------

* :py:func:`notify`: try to display a *system* notification. **Only on GNU/Linux with notify-send installed.**
* :py:func:`xtitle`: try to set the *title* of the terminal. Warning: **not always supported**.


Example of use (module)
=======================

To store a string, use :py:func:`sprint` (i.e. print to a string, *sprint*), like this: ::

    >>> example = sprint("France flag is <blue>blue<white>white<red>red<white>, Italy flag have <green>green on it<white>.")
    >>> example
    'France flag is \x1b[01;34mblue\x1b[01;37mwhite\x1b[01;31mred\x1b[01;37m, Italy flag have \x1b[01;32mgreen on it\x1b[01;37m.'


The string ``example`` can then be printed, with colors, with: ::

    >>> print(example)  # Sorry, but in the documentation it is hard to show colors :)
    France flag is bluewhitered, Italy flag have green on it.


To directly print a string colored by tags, use :py:func:`printc` (colors will be there if you try this in your terminal): ::

    >>> printc("Batman's costum is <black>black<white>, Aquaman's costum is <blue>blue<white> and <green>green<white>.")
    Batman's costum is black, Aquaman's costume is blue and green.


.. seealso::

   This is the most useful function. To do the same, but on any file, use :py:func:`writec`.


Moreover, the function :py:func:`erase` can also be useful to simply delete all *valid* color tags: ::

    >>> print(erase("Batman's costum is <black>black<white>, Aquaman's costum is <blue>blue<white> and <green>green<white>, and this is a non-valid <tag>, so it is kept like this."))
    Batman's costum is black, Aquaman's costum is blue and green, and this is a non-valid <tag>, so it is kept like this


In this last example, an ``<el>`` tag (:py:data:`el`) is used to erase the current content of the line, useful to make a *dynamical* print: ::

   >>> writec("<red>Computing <u>len(str(2**562016))<reset>...."); tmp = len(str(2**562016)); writec("<el><green>Done !<reset>")
   Done !

The first part of the line 'Computing len(str(2**562016))....' have disappeared after the computation! (which takes about one second).


Example of use (script)
=======================

* To show the help :code:`$ ansicolortags.py --help`;

* To run a test :code:`$ ansicolortags.py --test`;

* To produce a `GNU Bash color aliases file <https://bitbucket.org/lbesson/bin/src/master/.color.sh>`_ :code:`$ ansicolortags.py --generate --file ~/.color_aliases.sh`.


Auto detection
==============

This script can normally detect if ANSI codes are supported :

  1. ``$ ansicolortags.py --help`` : will print with colors if colors seems to be supported;
  2. ``$ ansicolortags.py --help --noANSI`` : will print without any colors, even if it is possible;
  3. ``$ ansicolortags.py --help --ANSI`` : will force the use of colors, even if they seems to be not supported.

And, the module part behaves exactly like the script part.

------------------------------------------------------------------------------

Elsewhere online
================

This project can be found on-line:

* here on BitBucket: `<https://bitbucket.org/lbesson/ansicolortags.py>`_
* here on PyPi: `<https://pypi.python.org/pypi/ansicolortags>`_


And some documentation on ANSI codes:

* The reference page for ANSI code is : `here on Wikipedia <https://en.wikipedia.org/wiki/ANSI_escape_code>`_.
* A reference page for XTitle escape code is : `here <http://www.faqs.org/docs/Linux-mini/Xterm-Title.html>`_.

Copyrigth
=========

© Lilian Besson, 2012-2016.

Complete documentation
======================

.. note:: The doc is available on-line, on `Read the Docs <https://www.readthedocs.org/>`_: `<http://ansicolortags.readthedocs.io/>`_.

"""

from __future__ import print_function, absolute_import

# %% Usual Modules
# Should we make them hidden from the interface of the script. Idea : remove from __all__ ?
import os
import sys
from subprocess import Popen

try:
    from time import sleep
except ImportError:
    def sleep(f):
        """ Replacement of time.sleep()."""
        print("time.sleep({}) should have been used.".format(f))


__author__ = 'Lilian Besson'
__version__ = '0.4'
__date__ = '2016-07-02T10:33:39'


# %% Program part

documentation_list_of_colors = """
List of all colors
==================

Bold colors: black, red, green, yellow, blue, magenta, cyan, white.

Normal colors (no bold): Bblack, Bred, Bgreen, Byellow, Bblue, Bmagenta, Bcyan, Bwhite.

Background colors: Black, Red, Green, Yellow, Blue, Magenta, Cyan, White.

Blink special caracters (Blink is faster than blink): blink, Blink:

 .. warning::

   Those are **not supported by all terminal emulator**.
   For example, gnome-terminal and terminator **doesn't** support it,
   but mintty.exe (Cygwin Windows terminal) support it.

Special characters to reinitialized ANSI codes buffer, or to do nothing: reset, nocolors.

Default foreground color, default background color: default, Default.

Italic on, off: italic, Italic. *Not always supported**

Bold on, off: b, B.

Underline on, off: u, U.

Reverse video on, off: neg, Neg. **Not always supported**.

Try to clear the screen: clear. **Not always supported**.

Try to erase the current line : el. **Not always supported**. Useful to use with ``sys.stdout.write`` and make the current printed line change !

Try to make an alarm sound. Also used to end the *xtitle* sequence: bell.

aliases for classic markup (/!\\, /?\\, 'WARNING', 'INFO' and 'ERROR').
warning, question, WARNING, INFO, ERROR:
"""


# %% Default values for new parsers
# FIXME switch to use docopt (https://github.com/docopt/docopt) instead of argparse

def _default_epilogue(version):
    """ Default epilogue used by a new parser."""
    return """\n\

<yellow>Copyrigth
=========<reset>
Version %s, (C) 2012-2016, Lilian Besson.""" % version


#: The default description, used when generate a parser by _parser_default function !
_default_description = "WARNING: No description had been given to _parser_default..."


def _add_default_options(parser, version=__version__):
    """ _parser_default(parser, version, date, author) -> argparse.ArgumentParser instance.

    Return the parser *parser*, modified by adding default options for the project,
    which put the options : ``--version, ``--verbose, ``--noANSI and ``--ANSI`` and others basic options.
    """
    parser.add_argument('--version', action='version', version='%(prog)s ' + version)
    # Let those two lines, just to remember that others stuffs.
    parser.add_argument('--noANSI', help="If present, ANSI escape code from ansicolortags are *disabled*.", action='store_true', default=False)
    parser.add_argument('--ANSI', help="If present, ANSI escape code from ansicolortags are *forced* to be printed (even if the output is detected to be a pipe).", action='store_true', default=False)
    return parser


# To make a default parser.
def _parser_default(description=_default_description,
                    epilogue="WARNING: No extra epilogue had been given to _parser_default...",
                    version=__version__, preprocessor=str):
    """ _parser_default(parser, version, date, author) -> argparse.ArgumentParser instance.

    Make a new *parser*, initialized by adding default options for the project (with :py:func:`_add_default_options`).

    * The default description is :py:data:`_default_description`,
    * The epilogue will be *epilogue*, then _default_epilogue(version, date, author).
    * preprocessor can be :py:func:`sprint` or :py:func:`str` (default value), *i.e.* a string -> string function, and it will be used as a **preprocessor** for ``description`` and ``epilogue`` value.

    Example:

    >>> parser = _parser_default(description='<DELETE>A description.',
    ... epilogue='The description will no begin by the tag DELETE, thanks to sprint preprocessing.',
    ... preprocessor=lambda s: s.replace('<DELETE>', ''))
    """
    # Passing RawDescriptionHelpFormatter as formatter_class= indicates that description and epilogue are already correctly formatted and should not be line-wrapped:
    # RawTextHelpFormatter maintains whitespace for all sorts of help text, including argument descriptions.
    # The other formatter class available, ArgumentDefaultsHelpFormatter, will add information about the default value of each of the arguments:
    try:
        import argparse
        parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                         description=preprocessor(description),
                                         prefix_chars='-+',
                                         epilog=preprocessor(epilogue + _default_epilogue(version)))
        # change the function *_add_default_options*, not this one.
        parser = _add_default_options(parser, version)
        return parser
    except ImportError:
        sys.stderr.write("""ERROR : when I tried to import the 'argparse' module.
        The first possible reason is that you are using a version of Python too old (< 2.7).
        The other possible reason is a other version of Python that the usual CPython :
        - Jython,
        - IronPython,
        - PyPy,
        for instance, are NOT supported.
        """)
        sys.stderr.flush()
        sys.exit(1)


# %% Auto detection ?

ANSISupported = True
try:
    #: If false, the module do almost NOTHING.
    ANSISupported = 'TERM' in os.environ and os.environ['TERM'] != 'unknown'
    if ('--noANSI' in sys.argv) or (not sys.stdout.isatty()):
        ANSISupported = False
    if '--ANSI' in sys.argv:
        ANSISupported = True
except Exception as e:
    print("I failed badly when trying to detect if ansicolortags are supported, reason = %s" % e)
    ANSISupported = False

# print("DEBUG: ANSISupported =", ANSISupported)

# colors bold
black = "\033[01;30m"    #: :black:`Black` and bold.
red = "\033[01;31m"      #: :red:`Red` and bold.
green = "\033[01;32m"    #: :green:`Green` and bold.
yellow = "\033[01;33m"   #: :yellow:`Yellow` and bold.
blue = "\033[01;34m"     #: :blue:`Blue` and bold.
magenta = "\033[01;35m"  #: :magenta:`Magenta` and bold.
cyan = "\033[01;36m"     #: :cyan:`Cyan` and bold.
white = "\033[01;37m"    #: :white:`White` and bold.

# colors not bold
Bblack = "\033[02;30m"    #: :black:`Black` and not bold.
Bred = "\033[02;31m"      #: :red:`Red` and not bold.
Bgreen = "\033[02;32m"    #: :green:`Green` and not bold.
Byellow = "\033[02;33m"   #: :yellow:`Yellow` and not bold.
Bblue = "\033[02;34m"     #: :blue:`Blue` and not bold.
Bmagenta = "\033[02;35m"  #: :magenta:`Magenta` and not bold.
Bcyan = "\033[02;36m"     #: :cyan:`Cyan` and not bold.
Bwhite = "\033[02;37m"    #: :white:`White` and not bold.

# Background colors : not very useful
Black = "\033[40m"    #: :black:`Black` background.
Red = "\033[41m"      #: :red:`Red` background.
Green = "\033[42m"    #: :green:`Green` background.
Yellow = "\033[43m"   #: :yellow:`Yellow` background.
Blue = "\033[44m"     #: :blue:`Blue` background.
Magenta = "\033[45m"  #: :magenta:`Magenta` background.
Cyan = "\033[46m"     #: :cyan:`Cyan` background.
White = "\033[47m"    #: :white:`White` background.

# Others : blink and Blink are NOT SUPPORTED BY ALL TERMINAL
blink = "\033[05m"    #: Make the text blink. NOT SUPPORTED BY ALL TERMINAL. On Windows (with mintty) it's ok. On Linux (with ttys, gnome-terminal or pyterminal, it's not).
Blink = "\033[06m"    #: Make the text not blink (*i.e.* stop blinking).

# nocolors, then default, then Default
nocolors = "\033[0m"  #: Nothing, base ANSI code.
default = "\033[39m"  #: Default foreground.
Default = "\033[49m"  #: Default background.

italic = "\033[3m"    #: *Italic*.
Italic = "\033[23m"   #: No *italic*.
b = "\033[1m"     #: **Bold**.
B = "\033[2m"     #: No **bold**.
u = "\033[4m"     #: :under:`Underline`.
U = "\033[24m"    #: No :under:`underline`.
neg = "\033[7m"   #: Negative.
Neg = "\033[27m"  #: No negative.

# New ones
clear = "\033[2J"  #: Clear the screen.
el = "\r\033[K"   #: Clear the *current line*.
reset = "\033[0;39;49m"   #: Reset the current foreground and background values to default, and disable all effects.

bell = "\007"  #: BEL is the bell character (``\007``). It *might* be interpreted and a sound signal might be heard (but not with every terminals).
title = "\033]0;"  #: Use it like : ``writec("<title>My title<bell>")``, **and only** with ending the sequence with ``<bell>``.

# Not specially tags, but aliases.
warning = "%s%s/!\\%s%s" % (red, u, U, reset)  #: A well colored Warning symbol (/!\\), in :red:`red` and underlined.

question = "%s%s/?\\%s%s" % (yellow, u, U, reset)  #: A well colored question symbol (/?\\), in :yellow:`yellow` and underlined.

ERROR = "%s%sERROR%s" % (reset, red, reset)   #: A well colored ERROR word, in :red:`red`.

WARNING = "%s%sWARNING%s" % (reset, yellow, reset)    #: A well colored WARNING word, in :yellow:`yellow`.

INFO = "%s%sINFO%s" % (reset, blue, reset)    #: A well colored INFO word, in :blue:`blue`.


#: List of all authorized colors. The dictionary :py:data:`colorDict` is more used.
colorList = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'Bblack', 'Bred', 'Bgreen', 'Byellow', 'Bblue', 'Bmagenta', 'Bcyan', 'Bwhite', 'Black', 'Red', 'Green', 'Yellow', 'Blue', 'Magenta', 'Cyan', 'White', 'Blink', 'blink', 'nocolors', 'default', 'Default', 'italic', 'Italic', 'b', 'B', 'u', 'U', 'neg', 'Neg', 'clear', 'el', 'reset', 'bell', 'title', 'warning', 'question', 'ERROR', 'WARNING', 'INFO']
#: List of all simple colors.
simpleColorList = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

# # Backup all colors.
# for name in colorList:
#     exec('_%s = %s' % (name, name))  # Bad to use exec !
#     # exec('colorDict["%s"] = %s' % (name, name))

# FIXED I could avoid this exec by building the colorDict manually
#: The key element of my script... A dictionary mapping color names to ANSI color code. Used in :py:func:`tocolor`.
colorDict = {
    'black': black,
    'red': red,
    'green': green,
    'yellow': yellow,
    'blue': blue,
    'magenta': magenta,
    'cyan': cyan,
    'white': white,
    'Bblack': Bblack,
    'Bred': Bred,
    'Bgreen': Bgreen,
    'Byellow': Byellow,
    'Bblue': Bblue,
    'Bmagenta': Bmagenta,
    'Bcyan': Bcyan,
    'Bwhite': Bwhite,
    'Black': Black,
    'Red': Red,
    'Green': Green,
    'Yellow': Yellow,
    'Blue': Blue,
    'Magenta': Magenta,
    'Cyan': Cyan,
    'White': White,
    'Blink': Blink,
    'blink': blink,
    'nocolors': nocolors,
    'default': default,
    'Default': Default,
    'italic': italic,
    'Italic': Italic,
    'b': b,
    'B': B,
    'u': u,
    'U': U,
    'neg': neg,
    'Neg': Neg,
    'clear': clear,
    'el': el,
    'reset': reset,
    'bell': bell,
    'title': title,
    'warning': warning,
    'question': question,
    'ERROR': ERROR,
    'WARNING': WARNING,
    'INFO': INFO
}


# Turn off color tags interpretation if they are not supported
if not ANSISupported:
    # for name in colorList:
    #     exec('%s = \"\"' % name)  # Bad to use exec !
    # print("DEBUG: removing colors!")
    for key in colorDict:
        colorDict[key] = ''

# print("DEBUG: colorDict =", colorDict)


def tocolor(mystring):
    """ tocolor(mystring) -> string

    Convert a string to a color.
    ``mystring`` **have** to be in :py:data:`colorDict` to be recognized (and interpreted).
    Default value if ``mystring`` is not one of the color name is ``""`` the empty string.
    """
    res = ""
    # if mystring in colorList:
    if mystring in colorDict:
        # print("DEBUG: Calling exec('res = %s' % {})".format(mystring))  # Bad to use exec !
        # exec("res = %s" % mystring)  # Bad to use exec !
        res = colorDict[mystring]
        # print("DEBUG: res =", res)
    # print("DEBUG: tocolor({}) -> {}".format(mystring, res))
    return res


def sprint(chainWithTags, left='<', right='>', verbose=False):
    """ sprint(chainWithTags, left='<', right='>', verbose=False) -> string

    Parse a string containing color tags, when color is one of the previous define name,
    and then return it, with color tags changed to concrete ANSI color codes.

    **Tags are delimited** by ``left`` and ``right``.
    By default, it's `HTML / Pango style <https://developer.gnome.org/pygtk/stable/pango-markup-language.html>`_ whit '<' and '>', but you can change them.

    For example, a custom style even closer to HTML could be: ``left='<span color='`` and ``right = '</span>'`` is also possible.

    .. warning::

       It is more prudent to put nothing else than ANSI Colors (i.e. values in :py:data:`colorList`) between ``'<'`` and ``'>'`` in ``chainWithTags``.
       The behavior of the function in case of false tags **is not perfect**.
       Moreover, a good idea could be to try not to use '<' or '>' for anything else than tags.
       I know, it's not perfect.
       But, the syntax of color tags is so simple and so beautiful with this limitation that you will surely forgive me this, *won't you* ;) ?


    Example (where unknown tags are left unmodified, and the colors should be there): ::

        >>> print(sprint("<blue>This is blue.<white> And <this> is white.<red> Now this is red because I am <angry> !<green><white>"))
        This is blue. And <this> is white. Now this is red because I am <angry> !


    This function is used in all the following, so all other function can also use ``left`` and ``right`` arguments.
    """
    # TODO improve efficiency of this core algorithm?
    ls = chainWithTags.split(left)
    if verbose:
        print("\tls =", ls)
    lls = list()
    for s2 in ls:
        if verbose:
            print("\ts2 =", s2)
        inte = s2.split(right)
        if verbose:
            print("\tinte =", inte)
        if inte[0] in colorList:
            inte[0] = tocolor(inte[0])
        else:
            if len(inte) > 1:
                inte[0] = left + inte[0] + right
        if verbose:
            print("\tinte =", inte)
        lls.append(inte)
    if verbose:
        print("\tlls =", lls)
    res = ""
    for _, llsii in enumerate(lls):
        for _, llsiij in enumerate(llsii):
            res += llsiij
    return res


def erase(chainWithTags, left='<', right='>', verbose=False):
    """ erase(chainWithTags, left='<', right='>', verbose=False) -> string

    Parse a string containing color tags, when color is one of the previous define name,
    and then return it, with color tags **erased**.

    Example:

      >>> print(erase("<blue>This is blue.<white> And <this> is white.<red> Now this is red because I am <angry> !<reset>"))
      This is blue. And <this> is white. Now this is red because I am <angry> !

    This example seems exactly the same that the previous one in the documentation, but it's not (it is impossible to put color in the output of a Python example in Sphinx documentation, so there is **no color in output** in the examples... but be sure there is the real output !).

    .. warning:: This function can mess up a string which has unmatched opening and closing tags (``<`` without a ``>`` or ``>`` without a ``<``), use it carefully.
    """
    ls = chainWithTags.split(left)
    if verbose:
        print("\tls =", ls)
    lls = list()
    for s2 in ls:
        if verbose:
            print("\ts2 =", s2)
        inte = s2.split(right)
        if verbose:
            print("\tinte =", inte)
        if inte[0] in colorList:
            inte[0] = ''  #: Here the 'erasure' is made.
        else:
            if len(inte) > 1:
                inte[0] = left + inte[0] + right
        if verbose:
            print("\tinte =", inte)
        lls.append(inte)
    if verbose:
        print("\tlls =", lls)
    res = ""
    for _, llsii in enumerate(lls):
        for _, llsiij in enumerate(llsii):
            res += llsiij
    return res


# FIXED how to add this *objects in Python 2 ?
# def printc(chainWithTags, *objects, left='<', right='>', sep=' ', end='\n', erase=False, **kwargs):
# I removed the keywords arguments
#          left='<', right='>', sep=' ', end='\n', erase=False,
# and define them manually by poping keys from kwargs...
# Cf. https://www.python.org/dev/peps/pep-3102/
# https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists

def printc(chainWithTags, *objects, **kwargs):
    """ printc(chainWithTags, *objects, left='<', right='>', sep=' ', end='\\n', erase=False, **kwargs) -> unit

    Basically a shortcut to ``print(sprint(chainWithTags))`` : it analyzes all tags (i.e., it converts the tags like ``<red>`` to their ANSI code value, like :py:data:`red`), and then it prints the result.

    Example (in a terminal the colors, and the bold and underlining effects would be there):

    >>> printc("<reset><white>« <u>Fifty shades of <red>red<white><U> » could be a <green>good<white> book, <b>if it existed<B>.")
    « Fifty shades of red » could be a good book, if it existed.


    It accepts one or more "things" to print, exactly like :py:func:`print`: for each value ``arg_i`` in ``*objects``:

     - if ``arg_i`` is a string, it is converted using ``sprint(arg_i, left=left, right=right)`` (:py:func:`sprint`), and then passed to :py:func:`print`.
     - otherwise ``arg_i`` is passed to :py:func:`print` without modification (in the same order, of course).

    Example with more than one object:

    >>> print("OK n =", 17, "and z =", 1 + 5j, ".")
    OK n = 17 and z = (1+5j) .
    >>> printc("<green>OK<white> n =<magenta>", 17, "<white>and z =<blue>", 1 + 5j, "<reset>.")  # in a terminal, the output will have colors:
    OK n = 17 and z = (1+5j) .


    This is the more useful function in this package.

    - If ``erase = True``, then :py:func:`erase` is used instead of :py:func:`sprint`

    .. hint::

       I suggest to use `ansicolortags.py <https://pypi.python.org/pypi/ansicolortags>`_ in your own project with the following piece of code:

       .. code:: python

           try:
               from ansicolortags import printc
           except ImportError:
               print("WARNING: ansicolortags was not found, disabling colors instead.\\nPlease install it with 'pip install ansicolortags'")
               def printc(*a, **kwargs):
                   print(*a, **kwargs)


    .. hint::

       During the last 4 years, `a lot of the small Python scripts I wrote <https://bitbucket.org/lbesson/bin/src/master/>`_ try to use this module to add some colors:
       for example, `FreeSMS.py <https://bitbucket.org/lbesson/bin/src/master/FreeSMS.py>`_,
       `plotnotes.py <https://bitbucket.org/lbesson/bin/src/master/plotnotes.py>`_,
       `strapdown2html.py <https://bitbucket.org/lbesson/bin/src/master/strapdown2html.py>`_,
       `calc_interets.py <https://bitbucket.org/lbesson/bin/src/master/calc_interets.py>`_...
    """
    left = kwargs.pop('left') if 'left' in kwargs else '<'
    right = kwargs.pop('right') if 'right' in kwargs else '>'
    sep = kwargs.pop('sep') if 'sep' in kwargs else ' '
    end = kwargs.pop('end') if 'end' in kwargs else '\n'
    doerase = kwargs.pop('erase') if 'erase' in kwargs else False
    # # DEBUG
    # print("chainWithTags:")
    # print(chainWithTags)
    # print("objects:")
    # print(objects)
    # print("kwargs:")
    # print(kwargs)
    # print("left:", left)
    # print("right:", right)
    # print("sep:", sep)
    # print("end:", end)
    # print("doerase:", doerase)
    # DONE for argument handling
    if len(objects) == 0:
        print(sprint(chainWithTags, left=left, right=right), sep=sep, end=end, **kwargs)
    else:
        fullargs = (chainWithTags,) + objects
        # DEBUG
        # print("fullargs:")
        # print(fullargs)
        if doerase:  # XXX cannot be called erase, it is already the function
            print(*(erase(s, left=left, right=right) if isinstance(s, str) else s for s in fullargs), sep=sep, end=end, **kwargs)
        else:
            print(*(sprint(s, left=left, right=right) if isinstance(s, str) else s for s in fullargs), sep=sep, end=end, **kwargs)


def writec(chainWithTags="", out=sys.stdout, left='<', right='>', flush=True):
    """ writec(chainWithTags="", out=sys.stdout, left='<', right='>', flush=True) -> unit

    Useful to print colored text **to a file**, represented by the object ``out``.
    Also useful to print colored text, but without any trailing '\\n' character.

    In this example, before the long computation begin, it prints 'Computing 2**(2**(2**4)).....',
    and when the computation is done, erases the current line (with ``<el>`` tag, :py:data:`el`),
    and prints ' Done !' in green, and the result of the computation: ::

         >>> writec("<red>Computing<reset> 2**(2**(2**4))....."); tmp = 2**(2**(2**4)); writec("<el><green>Done !<reset>")
         Done !


    This example show how to use this module to write colored data in a file.
    Be aware that this file now contains ANSI escape sequences.
    For example, :code:`$ cat /tmp/colored-text.txt` will well print the colors, but editing the file will show *hard values* of escape code: ::

        >>> my_file = open('/tmp/colored-text.txt', mode = 'w')  # Open an random file.
        >>> write("<blue>this is blue.<white>And <this> is white.<red>Now this is red because I am <angry> !<green><white>", file = my_file)
        >>> # Now this file '/tmp/colored-text.txt' has some ANSI colored text in it.

    Remark:
    It can also be used to simply reinitialize the ANSI colors buffer, but the function :py:func:`Reset` is here for this: ::

        >>> writec("<reset>")


    .. warning::

       The file ``out`` **will be flushed** by this function if ``flush`` is set to ``True`` (this is default behavior).
       If you prefer no to, use ``flush=False`` option: ::

           >>> writec(chainWithTags_1, out=my_file, flush=False)
           >>> # many things...
           >>> writec(chainWithTags_n, out=my_file, flush=False)
           >>> my_file.flush()  # only flush here!
"""
    out.write(sprint(chainWithTags, left=left, right=right))
    if flush:
        out.flush()


def clearScreen():
    """ clearScreen() -> unit

    **Try to** clear the screen using ANSI code :py:data:`clear`.
    """
    writec("<clear>")


def clearLine():
    """ clearLine() -> unit

    **Try to** clear the current line using ANSI code :py:data:`el`.
    """
    writec("<el>")


def Reset():
    """ Reset() -> unit

    **Try to** reset the current ANSI codes buffer, using :py:data:`reset`.
    """
    writec("<reset>")


# Other tools for the interface

def notify(msg="", obj="Notification sent by ansicolortags.notify", icon=None, verb=False):
    """ notify(msg='', obj='Notification sent by ansicolortags.notify', icon=None, verb=False) -> bool

    Notification using :py:mod:`subprocess` and ``notify-send`` (GNU/Linux command-line program).
    Also print the informations directly to the screen (only if verb=True).

    .. warning::

       This does not use any *ANSI escape* codes, but the common *notify-send* GNU/Linux command line program.
       It will probably fail (but cleanly) on Windows or Mac OS X.

    - Return True if and only if the title have been correctly changed.
    - Fails simply if ``notify-send`` is not found.
    """
    try:
        if icon:
            Popen(['notify-send', obj, msg, "--icon = %s/%s" % (os.getcwd(), icon)])
            if verb:
                print("ansicolortags.notify(): A notification have been sent, with obj = %s, msg = %s, and icon = %s." % (obj, msg, icon))
        else:
            Popen(['notify-send', obj, msg])
            if verb:
                print("ansicolortags.notify(): A notification have been sent, with obj = %s, and msg = %s." % (obj, msg))
        return 0
    except Exception as e:
        if verb:
            print("ansicolortags.notify(): notify-send : not-found ! Returned exception is %s." % e)
        return -1


def xtitle(new_title="", verb=False):
    """ xtitle(new_title="", verb=False) -> 0 or 1

    **Modify the current terminal title**.
    Returns 0 if one of the two solutions worked, 1 otherwise.

    An experimental try is with **ANSI escape code**,
    if the simple way by calling the ``xtitle`` program does not work (or if it is not installed).

    .. note::

       The second solution simply uses the two *ANSI* Tags ``<title>`` (:py:data:`title`) and ``<bell>`` (:py:data:`bell`).
       So, you can also do it with: ::

           >>> ansicolortags.writec("<title>This is the new title of the terminal<bell>")


    But this function *xtitle* is better: it tries two ways, and returns a signal to inform about his success.
    """
    try:
        Popen(['xtitle', new_title])
        if verb:
            print("ansicolortags.xtitle(): The title of the current terminal has been set to '%s'." % new_title)
    except Exception as e:
        if verb:
            print("ansicolortags.xtitle(): xtitle : not-found ! Returned exception is %s." % e)
        try:
            writec("<title>%s<bell>" % erase(new_title))
        except Exception as e:
            if verb:
                print("ansicolortags.notify(): With ANSI escape code <title> and <bell> : failed. ! Returned exception is %s." % e)
            return 1
    return 0


# %% Script part

def _generate_color_sh(file_name=None):
    """ _generate_color_sh(file_name=None) -> string | unit.

    Used to print or generate (if file_name is present and is a valid URI address)
    a profile of all the colors defined in this file.

    Print all ANSI Colors as :code:`export NAME="VALUE"`.
    Useful to automatically generate a :download:`.color.sh` file, to be used with Bash:
    and now you can easily colorized your Bash script with :code:`. color.sh` to import all colors.

    The file is a list of :code:`export NAME="VALUE"`, to be used with GNU Bash.


    .. note::

       For example, to generate the :code:`color.sh` file with this script, use the ``-g`` or ``--generate`` option, with ``-f FILE`` or ``--file FILE``:

       .. code:: bash

          $ python -m ansicolortags -g -f color.sh

    .. hint::

       I suggest to save this :download:`.color.sh` file to your home, like :code:`~/.color.sh`, so it will be available for any GNU Bash script.
       During the last 4 years, `all the Bash scripts I wrote <https://bitbucket.org/lbesson/bin/src/master/>`_ that uses this color profile (or assume it to be enabled, e.g. from `your .bashrc file <https://bitbucket.org/lbesson/bin/src/master/.bashrc#.bashrc-205>`_) assume it to be saved as :code:`~/.color.sh`.

       For instance,
       `PDFCompress <https://bitbucket.org/lbesson/bin/src/master/PDFCompress>`_,
       `git-blame-last-commit.sh <https://bitbucket.org/lbesson/bin/src/master/git-blame-last-commit.sh>`_,
       `mymake.sh <https://bitbucket.org/lbesson/bin/src/master/mymake.sh>`_,
       `makequotes.sh <https://bitbucket.org/lbesson/bin/src/master/makequotes.sh>`_,
       `photosmagic.sh <https://bitbucket.org/lbesson/bin/src/master/photosmagic.sh>`_,
       `remove_trailing_spaces.sh <https://bitbucket.org/lbesson/bin/src/master/remove_trailing_spaces.sh>`_,
       `series.sh <https://bitbucket.org/lbesson/bin/src/master/series.sh>`_,
       `strapdown2pdf.sh <https://bitbucket.org/lbesson/bin/src/master/strapdown2pdf.sh>`_,
       `Volume.sh <https://bitbucket.org/lbesson/bin/src/master/Volume.sh>`_ etc.

       In a Bash script, I suggest to source this :download:`.color.sh` file like this (it checks if the file exists before sourcing it):

       .. code:: bash

          [ -f ~/.color.sh ] && . ~/.color.sh
    """
    if file_name:
        writec("<green> The file %s is creating.<reset> (C) Lilian Besson, 2012-2016.\t" % file_name)
    writec("<blue><u>Listing of all ANSI colors...<reset>")
    sleep(0.5)
    writec("<el>...")
    for s in colorList:
        writec("<green><u>%s<reset>..." % s)
        sleep(0.05)
        writec("<el>...")
    writec("<reset>Listing of all ANSI colors...><red><u> DONE !<reset>...")
    sleep(0.5)
    writec("<el>")
    if file_name:
        mfile = open(file_name, 'w')
    else:
        mfile = sys.stdout
    mfile.write("""#!/bin/sh
#
# From ansicolortags.py module, auto generated with the --generate command
# More information on https://bitbucket.org/lbesson/ansicolortags.py/
#
# About the convention for the names of the colors :
# * for the eight colors black, red, green, yellow, blue, magenta, cyan, white:
#   + the name in minuscule is for color **with bold** (example 'yellow'),
#   + the name starting with 'B' is for color **without bold** (example 'Byellow'),
#   + the name starting with a capital letter is for the background color (example 'Yellow').
# * for the special effects (blink, italic, bold, underline, negative), **not always supported** :
#   + the name in minuscule is to **turn on** the effect,
#   + the name starting in capital letter is to **turn off** the effect.
# * for the other special effects (nocolors, default, Default, clear, el), the effect is **immediate** (and seems to be well supported).
#
# About
# =====
# Use this file .color.sh in other GNU Bash scripts, simply by sourcing him with
# $ source ~/.color.sh
#
# Copyrigth
# =========
# (C) Lilian Besson, 2012-2016.
#
# List of colors
# ==============
""")
    # FIXED it appeared to be failing on Python 3, now with this colorDict it works very well!
    res = ""
    for s in colorDict:
        res = colorDict[s]
        # print("""DEBUG: exec("res = ('%%s' %% %s)""" % s.replace('\x1b', '\\\\x1b'))
        # exec("res = ('%%s' %% %s)" % s.replace('\x1b', '\\\\x1b'))  # Bad to use exec !
        # Unescaping special characters.
        res = res.replace('\x1b', '\\033').replace('\r', '\\r').replace('\007', '\\007')
        # print("DEBUG 1: res =", res)
        mfile.write("export %s=\"%s\"\n" % (s, res))
        # print("""DEBUG 2: mfile.write("export %s=\\"%s\\"\\n" """ % (s, res))
        # mfile.write("export %s=\"%s\"\n" % (s, (r"%s" % res)))
        # the r"%s" above is important ?
    mfile.write("# DONE\n\n")
    if file_name:
        writec("<green> The file %s have been creating.<reset> (C) Lilian Besson 2012-2016.\n" % file_name)
        sys.exit(0)


def _run_complete_tests():
    """ _run_complete_tests() -> unit.

    Launch a complete test of all ANSI Colors code in the list :py:data:`colorList`.
    """
    printc("Launching full test for ANSI Colors.<default><Default><nocolors> now the text is printed with default value of the terminal...")
    for s in colorList:
        printc("The color '%s'\t is used to make the following effect : <%s>!! This is a sample text for '%s' !!<default><Default><nocolors>..." % (s, s, s))


# %% Main part, executed only if the script is executed

if __name__ == '__main__':
    #: Generate the parser, with another module.
    #: This variable is the preprocessor, given to description and epilogue by ParseCommandArgs,.
    #:  * erase: to print with no colors.
    #:  * sprint: to print with colors.
    # preprocessor = __builtin__.str, if you wanna to *see* the tags.
    mypreprocessor = sprint if ANSISupported else erase
    #: Generate the parser, with another module.
    myparser = _parser_default(
        description='<green>ANSI Colors utility <red>module<reset> and <blue>script<reset> (ansicolortags.py).',
        epilogue="""
Use this file <u>~/.color.sh<U> with other GNU Bash scripts, simply by sourcing him with:
<b><black>source ~/.color.sh<reset>  # in a GNU Bash script

<b>About the <u>convention<U> for the names of the colors:<reset>
- for the eight colors black, red, green, yellow, blue, magenta, cyan, white:
  + the name in minuscule is for color <u>with bold<reset> (example <yellow>'yellow'<reset>),
  + the name starting with 'B' is for color <u>without bold<reset> (example <Byellow>'Byellow'<reset>),
  + the name starting with a capital letter is for the background color (example <Yellow>'Yellow'<reset>);
- for the special effects (blink, italic (i), bold (b), underline (u), negative), <u>not always supported<reset>:
  + the name in minuscule is to <u>turn on<reset> the effect (for example 'u' to <u>underline<U>),
  + the name starting in capital letter is to <u>turn down<reset> the effect (for example 'U' to stop underline);
- for the other special effects (nocolors, default, Default, clear, el), the effect is <u>immediate<reset> (and seems to be well supported).

<yellow>About
=====<reset>
This project can be found <green>on-line<reset>:
 - here on <neg>BitBucket<Neg> : <u>https://bitbucket.org/lbesson/ansicolortags.py<U>,
 - here on <neg>PyPi<Neg> : <u>https://pypi.python.org/pypi/ansicolortags<U>,
 - and its documentation can be found here on <neg>Read the Docs<Neg> : <u>http://ansicolortags.readthedocs.io/<U>.

The reference page for ANSI code is : <u>https://en.wikipedia.org/wiki/ANSI_escape_code<U>.\n""",
        version=__version__, preprocessor=mypreprocessor)

    #: So, here become the interesting part.
    group = myparser.add_mutually_exclusive_group()
    group.add_argument("-t", "--test", help="Launch a complete test of all ANSI Colors code defined here.", action="store_true")

    #: Description for the part with '--file' and '--generate' options.
    group = myparser.add_argument_group('Generation of a GNU Bash color aliases file')
    # Add lats two options
    group.add_argument("-g", "--generate", help="Print all ANSI Colors as 'export name=\"value\"'.", action="store_true")  # , required = True)
    group.add_argument("-f", "--file", help="If present, and with --generate option, don't print the values, but export them in the file FILE (e.g. FILE = ~/.color.sh)", default=None)

    #: The parser is done.
    #: Use it to extract the args from the command line.
    args = myparser.parse_args()

    #: Use those args.
    if args.generate:
        if args.file:
            _generate_color_sh(args.file)
        else:
            _generate_color_sh()
            sys.exit(0)
    if args.test:
        _run_complete_tests()
        sys.exit(0)
    # Otherwise, print help and exit
    myparser.print_help()
    sys.exit(1)

# Remove the scripts values here
# FIXED: be sure we removed exactly the good ones
else:
    # del _generate_color_sh
    # del _run_complete_tests
    del _parser_default
    del _default_description
    del _default_epilogue
    del _add_default_options
