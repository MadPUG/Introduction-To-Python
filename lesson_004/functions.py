from __future__ import print_function  # Ignore this line until next month
# Section 1 of Lesson 4

# We've already used functions in every part of the presentation thus far.
# Each time we do print(...) we're using a function, but we haven't created
# our own functions.

# First let's talk about why functions are useful. Any time you're repeating
# some block of code you're immediately writing way too much code. Remember in
# our dictionaries lesson where we were doing
# print(alpha_ordering.get('z', 'There is no letter that'),
#       "comes after 'z' in the alphabet")
# And we had to copy and paste that for any other letter we wanted to give the
# same treatement to? That would be the perfect candidate for a function.
# Let's make this our first function.

# First we'll bring our dictionary over here.
alpha_ordering = {
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
}


# Now let's start writing our function. Functions are *def*ined and given
# names. To create a function you start with "def" followed by the function
# name. We'll call our function "print_next_letter". Function names have to
# start with a letter (upper- or lower-case) or underscore ("_") and then can
# be followed by a letter, number, or underscore. After the function we use
# parentheses to start the list of arguments a function requires.
def print_next_letter(alphabet_dictionary, previous_letter):
    # Then we put the actual instructions for the function inside, indented
    # once.
    default = 'There is no letter that'
    # We can use a variable to store the default return value here.
    print(alphabet_dictionary.get(previous_letter, default),
          "comes after '{0}' in the alphabet.".format(previous_letter))


# When defining our function we chose to require that the alphabet_dictionary
# be provided as the first argument, and which letter we want to find the next
# value for. Let's use it!
print_next_letter(alpha_ordering, 'a')
print_next_letter(alpha_ordering, 'z')
# It works!
# But there's something that's bothering me here. The output looks like:
# "b comes after 'a' in the alphabet."
# and I would much rather it look like:
# "'b' comes after 'a' in the alphabet."
# Let's make a new function that does this!


# We'll call this one print_next_letter2
def print_next_letter2(alphabet_dictionary, previous_letter):
    default = 'There is no letter that'
    try:
        first_part = "'{0}'".format(alphabet_dictionary[previous_letter])
    except KeyError:
        first_part = default
    print(first_part,
          "comes after '{0}' in the alphabet.".format(previous_letter))


# Let's see how that looks:
print_next_letter2(alpha_ordering, 'd')
print_next_letter2(alpha_ordering, 'z')

# MUCH BETTER!

# There are more advanced things we can do with functions so read on below.
# The presentation will be moving on now because we're probably very close to
# being out of time at this point.

# Extra material


# Function paramters (or arguments) can have default values. For example,
# we don't really need to pass alpha_ordering in every time we want to print
# the next letter in the alphabet. That would be really tedious after a while.
# Let's make a new function.
def print_next_letter3(previous_letter, alphabet_dictionary=alpha_ordering):
    # So we don't end up copying and pasting code, let's reuse
    # print_next_letter2
    print_next_letter2(alpha_ordering, previous_letter)


# Now let's use it
print_next_letter3('g')
print_next_letter3('z')

# It works! Notice, though, that we had to change the ordering of the
# arguments for this new function. Arguments with default values have to come
# after arguments without default values. We can also create a new dictionary
# for uppercase letters and still use print_next_letter3.

upper_alpha_ordering = {}
for (key, value) in alpha_ordering.items():
    upper_alpha_ordering[key.upper()] = value.upper()

# Now we can do any of the following:
print_next_letter3('I', alphabet_dictionary=upper_alpha_ordering)
print_next_letter3('M', upper_alpha_ordering)
# Or
print_next_letter2(upper_alpha_ordering, 'Y')
# Both are equivalent and both are correct.

# I personally prefer either the first or the last to the second option. When
# passing a value to an argument with a default value it is nice to name it
# for your future self and for others.
# In fact as long as you know the names of parameters, you can name each
# parameter you pass. For example, we could write
# print_next_letter2(upper_alpha_ordering, 'Y')
# as
print_next_letter2(alphabet_dictionary=upper_alpha_ordering,
                   previous_letter='Y')
# In fact, if we're passing the values by name explicitly, we can even reorder
# them!
print_next_letter2(previous_letter='Y',
                   alphabet_dictionary=upper_alpha_ordering)

# This does not mean we can do
# print_next_letter2('Y', alphabet_dictionary=upper_alpha_ordering)
# Or
# print_next_letter2('Y', upper_alpha_ordering)

# There is even more to learn about functions but we'll save that for another
# time.
