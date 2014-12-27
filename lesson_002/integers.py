from __future__ import print_function  # Ignore this line until next month
# Section 1 of Lesson 2

# Integers are simply whole numbers that can also be negative. Here are some
# examples:

-10
-9
0
1
2
3
233

# Integers can be referenced by names if you bind them to that name. You
# create a binding like so:

negative_ten = -10
zero = 0
two_hundred_thirty_three = 233

# You can now use `negative_ten`, `zero`, and `two_hundred_thirty_three`
# as references to -10, 0, and 233 respectively. For example:

print('The reference to negative_ten is:', negative_ten)
# Print allows you to show information to the user when they run your code
print('The reference to zero is:', zero)
print('The reference to two_hundred_thirty_three is:',
      two_hundred_thirty_three)

# You can also perform arithmetic on these references with other integers.

print('negative_ten - 10 =', negative_ten - 10)

one = zero + 1
print('The reference to one is:', one)

# Addition and subtraction are the most basic kinds of arithmetic. We can also
# do multiplication, division, exponentiation, and we can find remainders.

two = 4 / 2
print('two =', two)

eight = 4 * 2
print('eight =', eight)

sixteen = 4 ** 2
# Here we use ** to perform exponentiation
print('sixteen =', sixteen)

remainder = 3 % 2
# The % in this instance is referred to as modulo
print('The remainder of 3 divided by 2 is:', remainder)

# Don't you wish you had this while you were in grade school? But wait! It
# gets better! Head over to floats.py in this directory.
