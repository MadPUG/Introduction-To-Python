from __future__ import print_function  # Ignore this line until next month
# Section 3 of Lesson 2

# At this point you've already seen strings. A string looks like the
# following:
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

# There's so much more that can be done with strings but we don't have the
# time to work through all of them. At this point the presentation will move
# on, but below are a bunch more examples that we would like to encourage you
# to experiment with and enjoy.
