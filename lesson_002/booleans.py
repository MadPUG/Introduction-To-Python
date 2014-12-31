from __future__ import print_function  # Ignore this line until next month
# Section 7 of Lesson 2

# There are only two boolean values
True
False

# Booleans are very important for our next topic, but let's see where they
# can come from

print("1 == 1:", 1 == 1)
print("1 == 2:", 1 == 2)

# Okay so when we say 1 equals-equals 1 we get True but if we say something
# similar about 1 and 2 we get False. So == compares two things for equality.
# What about this

print("1 < 1:", 1 < 1)
print("1 < 2:", 1 < 2)
print("1 > 2:", 1 > 2)
print("1 >= 1:", 1 >= 1)
print("1 <= 2:", 1 <= 2)

# This works with strings too!

print('"foo" == "foo":', "foo" == "foo")

# So does this work with lists or tuples or anything like that? Yes!

my_list = [1, 2, 3]
print("my_list == [1, 2, 3]:", my_list == [1, 2, 3])
print("my_list == [1, 2]:", my_list == [1, 2])
print("my_list == [1, 2]:", my_list == [1, 2])
print("my_list >= [1, 2]:", my_list >= [1, 2])

# Woah! Wait! We can compare something other than equality?! That's pretty
# awesome. What happens if we do:
print("my_list >= [1, 2, 4]:", my_list >= [1, 2, 4])
print("my_list < [1, 2, 4]:", my_list < [1, 2, 4])

# Cool stuff, right?
# You can modify the above examples to use tuples instead of lists as an
# exercise. Then mix some strings in. Then try and see what happens with
# dictionaries.

# So here's another fun fact, we can create booleans from other booleans
print("not True:", not True)
print("not False:", not False)
print("True and True:", True and True)
print("True and False:", True and False)
print("True or False:", True or False)
print("False or False:", False or False)
print("False and False:", False and False)

# In fact we can do this a lot
print("True and True and True:", True and True and True)
print("True and True and False:", True and True and False)

# We can do t his all day, but we won't.
# Moving on ...
