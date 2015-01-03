from __future__ import print_function  # Ignore this line until next month
# Section 3 of Lesson 3

# I mentioned earlier that if you have a dictionary and try to retrieve a
# value from a key that doesn't exist, you'll see an error. You can look
# at this error by uncommenting the next line:
# {}['a key not in the dictionary']
# You should see something like:

# Traceback (most recent call last):
# ...
# KeyError: 'a key not in the dictionary'

# The last line contains the name of the error "KeyError". We can catch that
# error to prevent it from stopping the program. For example,

try:
    {}['a key not in the dictionary']
except KeyError:
    print('Caught a KeyError')

# There are similar errors when working with lists and tuples. If you try to
# get an element from an empty list or tuple, you'll get an IndexError

try:
    [][0]
except IndexError:
    print('Caught an IndexError')

# The same can happen if the index you're trying to access an index that's too
# large.

my_tuple = (1, 2, 3, 4, 5)
try:
    my_tuple[20]
except IndexError as error:
    print(error)

# We can bind the actual error to a name, like "error" as we did above and
# just print that!

# This concludes the section on exceptions. The important take away is that
# you get to define what happens when an exception is raised. Above we're only
# printing information about the exception but you can do anything inside an
# except block.
