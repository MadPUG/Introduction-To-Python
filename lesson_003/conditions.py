from __future__ import print_function  # Ignore this line until next month
# Section 1 of Lesson 3

# Now let's stop and think about real-life. So often our day is based on
# conditions, e.g., If Jill has finished the Q4 reports I will work on
# putting together a summary report for the CEO. Otherwise, if Jane has
# finished their work for the newest feature to be added to the Product
# I'll spend the day reviewing it with our product owners. ... If all else
# fails, I'll catch up on email.

# There are constructs for this in programming and Python in specific. We
# will not be looking at how we use those.

# Let's say we have computed a value and bound it as "result", e.g.,
result = 42
# We may want to print something out specifically for various values of
# result. We can use "if", "elif", and "else" to do this. For example:
if result < 42:
    print("The calculated result was below the threshold.")
elif result == 42:
    print("We've found the formula for the answer to the meaning of life.")
elif result == 43:
    print("We're very close to finding the answer to life.")
elif result > 43:
    print("The calculated result was above the threshold.")
else:
    print("Something went terribly wrong. Abandon the facility!")

# We know what these comparisons return. They return booleans. So if the
# expression produces True, we do what is indented inside of that statement.
# Python depends on indentation to know what code should be run if a condition
# is met or not. This means you could have if/elif/else's inside another
# if/elif/else block. For example,

new_result = 20
if new_result < 42:
    if new_result < 10:
        print("Insufficient data to calculate new result.")
    elif 10 <= new_result <= 30:
        print("The coefficient must not be correct.")
    else:
        print("The coefficient is fine. The exponent must be wrong.")
elif new_result == 42:
    print("We've found the formula for the answer to the meaning of life.")
elif new_result == 43:
    print("We're very close to finding the answer to life.")
elif new_result > 43:
    if new_result > 100:
        print("The research facility will self-destruct in 5...")
    else:
        print("The research facility is in danger.")
else:
    print("Something went terribly wrong. Abandon the facility!")

# As you can see you do not always need an elif statement. You also don't need
# an else statement.

my_number = 99
# Let's check to see if 3 divides evenly into my_number
if my_number % 3 == 0:
    # If the number is divisible by three, we want to square it
    my_number = my_number ** 2
print('my_number:', my_number)

# At this point we're going to move on in the presentation but read on for
# more information about if/elif/else.

# Any expression that evaluates to True or False can be places between "if "
# and ":". These statements, however, also accept values that aren't
# explicitly True or False. There are values that are commonly called "truthy"
# and "falsey". Below are examples of each:

# Falsey values:
0  # 0 is falsey due to Python's roots in C
[]  # Empty lists are falsey
{}  # Empty dictionaries are falsey
()  # Empty tuples are falsey
""  # Empty strings are falsey

# Truthy values
# Any non-zero integer is truthy
10
-10
# Any list with one or more items is truthy
[1, 2]
[1]
# Any dictionary with one or more items is truthy
{1: 2, 2: 3}
# Any tuple with one or more items is truthy
(1,)
# Any string with one or more letters is truthy
"A"
"A string"

# Just like with booleans you can obtain the opposite value by placing "not"
# in front of it. For example,
not []  # => True
not [1, 2, 3]  # => False
# And the same applies for the other examples

# It can be convenient to rely on these truthy and falsey values but it's a
# convention in Python to be very explicit, even if you don't have to be.
# You could calculate a test score and store it in the variable passed
passed = 0
# If passed is 0 you failed otherwise you passed. We could then write this as
if not passed:
    print("You failed.")
else:
    print("You passed!")

# But if something changes in the future this might produce a different result
# than you intended. It would be better to write
if passed > 0:
    print("You passed!")
else:
    print("You failed.")
