from __future__ import print_function  # Ignore this line until next month
# Section 5 of Lesson 2

# The following are lists
['here', 'is', 'a', 'list', 'of', 'strings']
['one element list']
[]  # Empty list

# Unlike strings and tuples, lists *are* mutable.
fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34]
print('Before:', fibonacci)
fibonacci[0] = 0
print('After:', fibonacci)

# Just like strings and tuples support arbitrary access of elements and slices
print('fibonacci[5]:', fibonacci[5])
print('fibonacci[5:8]:', fibonacci[5:8])

# Unlike strings you can replace a slice with a new list of any length
fibonacci[5:8] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('fibonacci:', fibonacci)

# This is typically kind of slow though for reasons you don't need to
# understand right now.

# Now if we were to remove the octothorpe signs (a.k.a., uncomment) from the
# following lines, we would see Python halt suddenly and print a message about
# a TypeError.

# fibonacci_tuple = (1, 1, 2, 3, 5, 8, 13, 21, 34)
# fibonacci_tuple[0] = 1
# fibonacci_tuple[5:8] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Since tuples are immutable, attempting to modify them causes Python to
# complain loudly. The same happens if you were to uncomment the following
# lines.

# my_string = "This is my string"
# my_string[0] = 't'
# my_string[0:5] = "THIS"

# Lists support adding items to the end without using +. We use the append
# method for this.

fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34]
fibonacci.append(55)
print('After append:', fibonacci)

# We can also extend a list with a new list using the extend method.

fibonacci.extend([89, 144, 233])
print('After extend:', fibonacci)

# You can use + to create a new list from two existing lists

more_fibonacci = [377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
new_fibonacci = fibonacci + more_fibonacci
print('fibonacci:', fibonacci)
print('new_fibonacci:', new_fibonacci)

# We will see more lists later. At this point we'll be moving on with the
# presentation but there is extra material below about some of the very useful
# methods that come with every list you'll ever use.

# EXTRAS

# Let's make a new list. I'm getting tired of typing fibonacci fibonacci
# fibonacci fibonacci fibonacci.
my_list = [1, 2, 3, 5]
print('my_list:', my_list)

# Oh no! We missed 4. No worries, we can just use the insert method and shove
# a 4 right into the list.
# To insert something into my_list, we first need to give the insert method
# the position to insert the item before. We want to insert this before the
# last item in the list so the first value we will pass to insert is 3. The
# second value we pass to insert is the value we want to insert into the list.
# Now we have:
my_list.insert(3, 4)
print('my_list after inserting 4:', my_list)

# Now we want to remove any number that isn't either 1 or prime. Well, I guess
# we have to say goodbye to 4 now.
my_list.remove(4)
print('my_list after removing 4:', my_list)

# Oh now we want to remove the first element of the list regardless of what it
# actually is.
my_list.pop(0)
# Oh but let's also remove the last item too. For that we don't need to pass
# anything to pop.
my_list.pop()
print('my_list after popping twice:', my_list)

# Now let's make a new list for fun
new_list = my_list + my_list + my_list + my_list
# I wonder how many 2's are present in new_list
print("There are {0} 2's in new_list".format(new_list.count(2)))

# We can sort our new list too!
new_list.sort()
print('sorted list:', new_list)

# And finally let's reverse it
new_list.reverse()
print('reversed list:', new_list)
