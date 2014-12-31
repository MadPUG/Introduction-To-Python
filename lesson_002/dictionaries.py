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

# At this point the presentation will move forward but read on for more
# information about dictionaries.

# Dictionaries are often called "dicts" for simplicity. We will continue our
# examples using dict in place of dictionary.

# You can merge any dictionary into another using the update method.
my_dict = {}
my_dict.update({'a': 'b'})
my_dict.update({'b': 'c'})
print('my_dict:', my_dict)

# You may be wondering, however, what happens when you call update with two
# dictionaries that have the same keys. A dictionary cannot have the same key
# repeated, we learned that earlier. Let's see what happens:

my_dict.update({'a': 'd'})
print("my_dict['a']:", my_dict['a'])

# So the last dictionary to be merged in wins. This can be helpful sometimes.
# Let's say you're building a website and you want to use dictionaries to
# manage a user's preferences before storing them. You could have a default
# set of preferences and then update them with what they change. For example:

default_preferences = {
    'show homepage on login': 'yes',
    'private profile': 'yes',
    'searchable email address': 'no',
    'tell friends about birthday': 'no',
    'using legal name': 'no',
}

updated_preferences = {
    'show homepage on login': 'no',
    'using legal name': 'yes',
}

users_preferences = {}
users_preferences.update(default_preferences)
users_preferences.update(updated_preferences)
print('default:', default_preferences)
print('updated:', updated_preferences)
print('current:', users_preferences)

# Note how using update on users_preferences did not affect
# default_preferences or updated_preferences.

# Until now we've only ever seen dictionaries map a string to a string, but
# that is not a requirement. The only restriction on the types dictionaries
# have is that the key must be able to consistently return the same value when
# you pass it to hash(), e.g., hash("my string") will always return the same
# integer.

# So let's look at different dictionary:
integer_to_string = {
    -1: "negative one",
    0: "zero",
    1: "one",
    2: "two",
}

# We can do the same thing that we always do:
print('integer_to_string[-1]:', integer_to_string[-1])

# Note the keys do not all have to be the same type, but it is considered good
# practice to do that. The same applies to the values that the keys map to.
# You will have an easier time reasoning about things if all of the values
# have the same type.

# Now let's look at a different method on a dictionary. This method will
# return a list of tuples of length 2 (a.k.a., 2-tuples) where the first item
# of every tuple is a key, and the second item is the value that the key
# corresponds to. For example:

print('integer_to_string.items():', integer_to_string.items())

# This should look just like
# [(-1, "negative one"), (0, "zero"), (1, "one"), (2, "two")]
# But the ordering may not be the same. This should hopefully reinforce the
# fact from earlier that tuples *can* contain items of differing type. For
# a simple usage of a tuple it is typically easier to reason about the code
# if they all have the same type, but in instances like this, it is not
# practical to expect every item in a tuple to have the same type. In this
# case it's easier to expect that each tuple has an item of the same type in
# the same position, i.e., each tuple will have a structure like:
# (integer, string)
# This practice can really be applied to tuples of any length though. We could
# have:

[(1,  "one", {"one": 1}), (2, "two", {"two": 2})]
# Where it is (integer, string, dictionary), and if we want to be more
# specific (integer, string, {string: integer})

# You can also retrieve a list of the keys in a dictionary
print('integer_to_string.keys():', integer_to_string.keys())

# And a list of values
print('integer_to_string.values():', integer_to_string.values())
