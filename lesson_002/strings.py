from __future__ import print_function  # Ignore this line until next month
# Section 3 of Lesson 2

# At this point you've already seen strings. A string looks like the
# following:
'a'  # <- Is a string
"This is a string"
'This is also a string'
"""This is a string too"""

# Like everything else in Python, you can bind a string to a name.
my_string = "This is my string, there are many like it, but this is mine"

# We previously used strings to help us understand what we were printing.
print(my_string)

# There are a lot of things that you can do to a string.
# You can take a string and make every letter inside of it uppercase.
my_uppercase_string = my_string.upper()
print(my_uppercase_string)
# Note that my_string does not change after this though
print('my_string:', my_string)

# Here upper is known as a "method". It is an instruction that is tied to a
# particular string. See the bottom of this file for more information.

# You can take a string and make every letter inside of it lowercase.
my_lowercase_string = my_string.lower()
print(my_lowercase_string)

# You can create a new string by adding another string to it.
# You can add to the beginning of it.
my_new_string = "I quoth, " + my_string
# Or you can add to the end of it.
my_newer_string = my_string + '.'
print(my_new_string)
print(my_newer_string)

# Even here, my_string has not changed.
print('my_string:', my_string)
# This is, in part, because strings are immutable in Python. Once you have
# created a string, you cannot change that string. You can create a new string
# with your modifications, but you can never change the existing string.

# You can replace sections of it.
my_program = my_string.replace("string", 'program')
print(my_program)

# You can replace any part of it, not just whole words.
my_i_less_string = my_string.replace('i', '')
print(my_i_less_string)

# You can access arbitrary letters in a string. If you want the 11th letter,
# you use 10 to get it.
print("my_string[10] =", my_string[10])

# The first letter of a string is found by using 0. In most programming
# languages, we begin counting at 0.
print("The first letter of my_string is", my_string[0])

# You can also take subsections of a string. Let's say you want the piece of
# the string that starts with the second letter and ends before the 7th
# letter. To get that substring you would do the following:
print(my_string[1:6])

# This is called a slice.it starts with the 2nd letter and ends at the letter
# before the 7th. So what you have is
print(my_string[1] + my_string[2] + my_string[3] + my_string[4] +
      my_string[5])

# If you wanted to get that 7th letter, you would do
print(my_string[1:7])

# You can also take the substring starting at a letter to the end by doing
print(my_string[6:])

# There's so much more that can be done with strings but we don't have the
# time to work through all of them. At this point the presentation will move
# on, but below are a bunch more examples that we would like to encourage you
# to experiment with and enjoy.

# Strings have a lot of methods. Each string has the same methods defined on
# it. This means that any string you work with will behave the same way.

# count method
# With the count method you can find the number of times a string occurs
# in another string. For example:
print("The letter 'i' appears", my_string.count('i'), "times")
print("The string 'string' appears", my_string.count("string"), "times")

# find method
# The find method looks for the existence of a string in another string.
# If we do
my_string.find('string')
# We are looking for 'string' in my_string. The find method returns an
# integer.
position = my_string.find('string')
print("This starts with 'string':", my_string[position:])

# format method
# If you were writing a form letter, you might have a salutation that you
# need to fill in like the following
salutation = 'Dear {0},'
# Where 0 will be replaced by the name of the person. We can do this using the
# format method.
print(salutation.format('Mrs. President'))
print(salutation.format('Ian and Cea'))
# You could even have multiple things you format it with.
message = 'On {0}, I found that {1} was missing from {2}.'
# Now it's time for madlibs
print(message.format('Monday', 'Mr. Whiskers the Cat', 'his car'))
# {0} is substituted with Monday
# {1} is substituted with Mr. Whiskers the Cat
# {2} is substituted with his car

# End of extra curricular activities
