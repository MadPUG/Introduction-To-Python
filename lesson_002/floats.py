from __future__ import print_function  # Ignore this line until next month
# Section 2 of Lesson 2

# Floats are a lot like decimals that you know from elementary school

1.3
0.5
-2.01

# Floats have most of the same arithmetic operations defined as integers.

# You can perform division and get new floats
one_and_three_tenths = 13.0/10
# You can devide one float by another
one_half = 1.0/2.0

# Or you can add two floats to get another float
print("A half plus one and three tenths is", one_half + one_and_three_tenths)

# As you might expect, you can also subtract two floats
print("A half less one and three tenths is", one_half - one_and_three_tenths)

# You can also multiply them
print("A half doubled is", one_half * 2)

# And you can exponentiate them
print("A half squared is", one_half ** 2)

# You can also use a float as an exponent
print("The square root of 4 is", 4 ** one_half)
