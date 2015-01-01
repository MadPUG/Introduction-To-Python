from __future__ import print_function  # Ignore this line until next month
# Section 2 of Lesson 3

# So we've seen lists, tuples, and if statements. How can we operate on each
# element of and apply the same logic to each one? We can use the for
# statement! A for statement (a.k.a, for loop) can iterate over each element
# in a list, tuple, dictionary, string (or anything similar [1]) like so:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in my_list:
    print('item:', item)

# This will print out each item in the list on a new-line. Well what if we
# want to do something else?
for item in my_list:
    print('item ** 2:', item ** 2)

# We can even use an if-statement
for item in my_list:
    if item % 3 == 0:
        print('item ** 3:', item ** 3)
    else:
        print('item ** 2:', item ** 2)

# We can do the same thing with tuples
for item in (1, 2, 3, 4, 5):
    print('item ** 5:', item ** 5)

# But what if we want to make a new list out of the old?
squared_list = []
for item in my_list:
    squared_list.append(item ** 2)
print('squared_list:', squared_list)

# This works really well and is fairly clear based on what we understand about
# lists and the append method. There's a faster and more concise way to write
# this called a "list comprehension"
cubed_list = [item ** 3 for item in my_list]
print('cubed_list:', cubed_list)
# In essence this can be unwrapped into a for-loop but this is much faster
# because we never call .append on a list. This is also the more common way of
# creating a new list from an old. It isn't always practical though.

# We can also loop through code so long as a condition is true. These are
# called while loops.
my_counter = 0
while my_counter < 100:
    my_counter = my_counter + 1
    # This can be written more concisely as my_counter += 1
    if my_counter % 10 == 0:
        print('my_counter:', my_counter)

# And really the expression can be anything that is Truthy or evaluated to
# True. This gives us one way to count up to a number. There is another way
# though:

for counter in range(0, 101):
    if counter % 10 == 0:
        print('counter:', counter)

# Notice this output is virtually the same as the while loop above.

# FOOTNOTES
# [1]: Basically there are a kind of object in Python called "iterables". What
#      makes an object iterable is a bit too advanced to discuss right now,
#      but to say the least - strings, tuples, dictionaries, and lists are
#      iterable types.
