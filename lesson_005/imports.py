# Section 1 of Lesson 5

# Up until now, everything we've seen in python just exists. You also may have
# come to this presentation having heard that Python comes with "batteries
# included". When people say that Python has "batteries included" they mean
# that Python comes with a standard set of well-built modules of code for you.
# This set is often called the standard library (or stdlib). The contents of
# these modules are not automatically available to you whenever you need them
# though. To use a library (or module) you have to "import" it. You can also
# import specific things from a library or module.

# Let's look at some cool standard libraries.

# The first one we'll look at allows you to open URLs in the operating
# system's default web browser
import webbrowser
# Once we've importanted, we use a '.' to access functions and other things
# contained in the module. In this case the module offers us an 'open'
# function. We can use this function much like a method on a list or
# dictionary.
webbrowser.open('https://docs.python.org/library/webbrowser')
# That should have opened up the online documentation for the webbrowser
# module. It should show you other functions inside the module that you
# can use to experiment with.

# Next we'll look at a module that does pretty printing for you. We really
# only want one function from this library though: the 'pprint' function.
# Let's only import that from the module like so:
from pprint import pprint
# We can now pass in a large dictionary to pretty print... like:
pprint({
    'a': 'b',
    'b': 'c',
    'c': 'd',
    'd': 'e',
    'e': 'f',
    'f': 'g',
    'g': 'h',
    'h': 'i',
    'i': 'j',
    'j': 'k',
    'k': 'l',
    'l': 'm',
    'm': 'n',
    'n': 'o',
    'o': 'p',
    'p': 'q',
    'q': 'r',
    'r': 's',
    's': 't',
    't': 'u',
    'u': 'v',
    'v': 'w',
    'w': 'x',
    'x': 'y',
    'y': 'z',
})

# If we were to print our trusty alphabetic dictionary otherwise, it would
# probably look kind of terrible.

# There are a lot more cool and useful modules in the standard library but I
# really wanted to show you all ones that would be relevant to your interests.
# I can't think of any other very generic ones so feel free to use the rest of
# tonight to ask me about anything we've done thus far and for recommendations
# about modules.

# So far every lesson has had "from __future__ import print_function" at the
# top of each file. If you recall, I suggested you install Python 2.7 before
# the first meeting. Python 2.5, 2.6, and 2.7 all provide the __future__
# module to retrieve planned features for future versions of Python. We've
# been using the enhanced and easier to understand print_function from the
# future versions of Python. You'll notice we don't have it at the top of this
# file. If we did the following would cause a SyntaxError:

print "Hello from the print statement"

# In Python 2 "print" is a statement, which means it is similar to "if",
# "else", "for", "while", and other similar words.

# Extra credit

# You also have a lot of modules that exist but which do not come with Python
# by default. The most common place to find these modules is at
# https://pypi.python.org/
# To install modules from there, you should save the file found at
# https://bootstrap.pypa.io/get-pip.py
# And then run it like so:
# python get-pip.py
# python.exe get-pip.py
# Then you can install a package from PyPI (The Python Package Index) and use
# it as if it were part of Python (like we were using modules above). We will
# talk about this more next month.
