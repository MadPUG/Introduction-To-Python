from __future__ import print_function  # Ignore this line until next month
# Section 6 of Lesson 2

# The following are dictionaries
{}  # Empty dictionary
{'this is a key': 'this is a value'}
{'a': 'b', 'b': 'c', 1: 2, 2: 3}

# Dictionaries are a way of mapping one thing to another. For example if you
# had the alphabet and you wanted to link each letter to the letter that comes
# after it you could do:
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

# We can now look up what letter comes after e in the alphabet:
print(alpha_ordering['e'], "comes after 'e' in the alphabet")

# Note that the way we look this up is by using the same value as exists on
# the left side of the :. The : tells Python what is the key and what is the
# value in a dictionary.

# Note that there is no value for z though. Because of this, if we tried to
# do:
# alpha_ordering['z']
# The program would crash. If we want to avoid crashes, we have to use a
# method called 'get'.
print(alpha_ordering.get('z', 'There is no letter that'),
      "comes after 'z' in the alphabet")

# The first argument to get is what we're hoping to find. The second argument
# is what get should return if the key is not present.
print(alpha_ordering.get('b', 'There is no letter that'),
      "comes after 'b' in the alphabet")

# Dictionaries do not allow you define the same key twice. Specifying it twice
# is undefined behaviour.
duplicates = {
    'a': 'b',
    'a': 'c',
}

# There's no guarantee if duplicates['a'] will return 'b' or 'c'

# Dictionaries are mutable, like lists. You can change the value associated
# with a key at any time.

my_dictionary = {
    'my key': 'my value'
}
print("my_dictionary['my key']:", my_dictionary['my key'])
my_dictionary['my key'] = 'a new value'
print("my_dictionary['my key']:", my_dictionary['my key'])

# You can also add new keys and values to your dictionary at any time.

my_dictionary['a new key'] = 'dictionaries are fun'
print("my_dictionary['a new key']:", my_dictionary['a new key'])

# You can merge any dictionary into another using the update method.
