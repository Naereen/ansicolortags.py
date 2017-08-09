#!/bin/sh
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
# Use this file .color.sh in other GNU Bash scripts, simply by sourcing it with:
# $ [ -f ~/.color.sh ] && source ~/.color.sh
# And then:
# $ echo -e "French flag is ${blue}blue${white}, white, ${red}red${white}."
#
# Copyrigth
# =========
# (C) Lilian Besson, 2012-2017.
#
# List of colors
# ==============
export black="\033[01;30m"
export red="\033[01;31m"
export green="\033[01;32m"
export yellow="\033[01;33m"
export blue="\033[01;34m"
export magenta="\033[01;35m"
export cyan="\033[01;36m"
export white="\033[01;37m"
export Bblack="\033[02;30m"
export Bred="\033[02;31m"
export Bgreen="\033[02;32m"
export Byellow="\033[02;33m"
export Bblue="\033[02;34m"
export Bmagenta="\033[02;35m"
export Bcyan="\033[02;36m"
export Bwhite="\033[02;37m"
export Black="\033[40m"
export Red="\033[41m"
export Green="\033[42m"
export Yellow="\033[43m"
export Blue="\033[44m"
export Magenta="\033[45m"
export Cyan="\033[46m"
export White="\033[47m"
export blink="\033[05m"
export Blink="\033[06m"
export nocolors="\033[0m"
export default="\033[39m"
export Default="\033[49m"
export italic="\033[3m"
export Italic="\033[23m"
export b="\033[1m"
export B="\033[2m"
export u="\033[4m"
export U="\033[24m"
export neg="\033[7m"
export Neg="\033[27m"
export clear="\033[2J"
export el="\r\033[K"
export reset="\033[0;39;49m"
export bell="\007"
export title="\033]0;"
export warning="\033[01;31m\033[4m/!\\033[24m\033[0;39;49m"
export question="\033[01;33m\033[4m/?\\033[24m\033[0;39;49m"
export ERROR="\033[0;39;49m\033[01;31mERROR\033[0;39;49m"
export WARNING="\033[0;39;49m\033[01;33mWARNING\033[0;39;49m"
export INFO="\033[0;39;49m\033[01;34mINFO\033[0;39;49m"
# DONE
