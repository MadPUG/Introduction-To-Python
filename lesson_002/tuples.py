from __future__ import print_function  # Ignore this line until next month
# Section 4 of Lesson 2

# The following are tuples
('this', 'is', 'a', 'tuple')
('this', 'is', 'also', 'a', 'tuple')
(1, 2, 3, 4, 5, 6)

# Tuples are immutable, much like strings

# You can also bind tuples to names (like everything we've seen thus far)
fibonacci = (1, 1, 2, 3, 5, 8, 13, 21, 34)

# We can print tuples too
print(fibonacci)

# We can get elements from a tuple as well
print(fibonacci[2])
print(fibonacci[5])

# We can also get a subset of the elements of the tuple using slices
print(fibonacci[3:8])

# We can concatenate two (or more) tuples using the + symbol
print(fibonacci + (55, 89) + (144, 233))

# Note that fibonacci hasn't changed
print(fibonacci)

# Tuples can have 1 or more elements
print((10,))

# You can mix types inside a tuple too (although it isn't recommended)
mixed_types = (1, 2.0, "string")

# Tuples behave a lot like our next topic: lists.
