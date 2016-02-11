# (re)Intro to Python
2/11/16
Madison Python Users Group
Cea Stapleton and Ian Cordasco

---

A brief introduction to Python
(a reprisal of last year, with new comments)

---

# Dictionaries

---

The following are dictionaries:

```
{}  # Empty dictionary
{'this is a key': 'this is a value'}
# Dictionaries do not have strict types.
# Both keys and values can be of any type.
{'a': 'b', 'b': 'c', 1: 2, 2: 3, 'd': 4}
```
---

Another dictionary we’ll use:

```
alpha_ordering = {
    'a': 'b',
    'b': 'c',
    'c': 'd',
    'd': 'e',
    'e': 'f',
    'f': 'g',
(you get the picture…)
    'v': 'w',
    'w': 'x',
    'x': 'y',
    'y': 'z',
}
```
---

We can look up what letter comes after e in the alphabet:


```
print(alpha_ordering['e'], "comes after 'e' in the alphabet")
```

---

If we don't know if there's a value for a key, we can use a method to
 retrieve it or return a default.

```
print(alpha_ordering.get('z', 'There is no letter that'),
      "comes after 'z' in the alphabet")
```

---

If we want to add something that comes after 'z', we can:

```alpha_ordering['z'] = 'How did I get here?’```

We can update the dictionary because it is mutable.

---

You can merge any dictionary into another using the update method.

```
words_collection = {}
words_collection.update({'a': 'b'})
words_collection.update({'b': 'c'})
print('words_collection:', words_collection)
```

---

You may be wondering, however, what happens when you call update with two dictionaries that have the same keys. A dictionary cannot have the same key repeated, we learned that earlier. Let's see what happens:


```
words_collection.update({'a': 'd'})
print("words_collection['a']:", words_collection['a'])
```

---

We can also list all key-value pairs in a dictionary

```print("words_collection.items():", words_collection.items())```

---

We can retrieve only the keys
```print("words_collection.keys():", words_collection.keys())```

---

We can retrieve only the values
```print("words_collection.values():", words_collection.values())```

---

# Lists

---

The following are lists:

```
['here', 'is', 'a', 'list', 'of', 'strings']
['one element list']
[]  # Empty list
```
---

Like dictionaries, lists are mutable.

---

```fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34]
print('Before:', fibonacci)
fibonacci[0] = 0
print('After:', fibonacci)
```

---

Lists allow for arbitrary retrieval:

```
print('fibonacci[5]:', fibonacci[5])
```

---

Lists also allow you to retrieve groups of items using "slice" syntax:

```
print('fibonacci[5:8]:', fibonacci[5:8])
```

---

You can also create a slice and skip over elements:

```print('fibonacci[2:8:2]:', fibonacci[2:8:2])```

---

You can add a single item to the end of the list:

```
fibonacci.append(55)
```

---

Or you can add a list of items to the end of the list:

```fibonacci.extend([89, 144, 233])
print('fibonacci:', fibonacci)```

---

# Tuples

---

The following are tuples

```
('this', 'is', 'a', 'tuple')
('this', 'is', 'also', 'a', 'tuple')
(1, 2, 3, 4, 5, 6)
```

---

Tuples work a lot like lists except they're immutable.
This means you cannot append an item, extend them, or replace an individual element

---

# Functions, Loops, Conditions

---

Let's say we need a way to find all of the squares of numbers less than
another number

---

```
def squares_until(upper_limit):
    squares = []
    # A `for` loop allows us to iterate over all the elements in the list
    # returned by range()
    for n in range(upper_limit / 2):
        n_squared = n ** 2
        # The if-else statement allows us to decide when we're done iterating
        # over the numbers
        if n_squared < upper_limit:
            squares.append(n_squared)
        else:
            # Here we can stop our loop early
            break
    # Here we return the values we've generated
    return squares

print('The squares less than 50 are:', squares_until(50))
```

---

# Exceptions

---

You'll see an error if you try to access a key that does not exist in a
dictionary. You can see the error (or exception) by uncommenting the
next line:

```
# {}[‘a key not in the dictionary']
```

---

You should see something like:

```Traceback (most recent call last):
...
KeyError: 'a key not in the dictionary’```

---

The last line contains the name of the error "KeyError". We can catch that exception to prevent it from stopping the program. For example,

```
try:
    {}['a key not in the dictionary']
except KeyError:
    print('Caught a KeyError')
```

---

All exceptions can be handled with the try-except syntax.
If you have something that can raise multiple exceptions you can specify
multiple except blocks, e.g.,

```
try:
    {}['a key not in the dictionary']
except KeyError:
    print('Caught a KeyError')
except IndexError:
    print('Caught an IndexError')
```

---

# Classes - because communism

---

## Let's build a role-playing game

---

```
class Adventurer(object):
    def __init__(self, name, health, experience, level, adventurer_type):
        self.name = name
        self.health = health
        self.experience = experience
        self.level = level
        self.adventurer_type = adventurer_type

    def format(self):
        format_str = ("Our adventurer's name: {0}\n"
                      "         Their health: {1}\n"
                      "     Their experience: {2}\n"
                      "          Their level: {3}\n"
                      "           Their type: {4}\n")
        return format_str.format(self.name, self.health, self.experience,
                                 self.level, self.adventurer_type)
```

---

So the first thing that should be intersting is that the method we're
defining is `__init__`.

---

If you're familiar with Java, this might be confusing.
If you already know ruby, this should look somewhat familiar though. In
Python, every class's initialization method is named `__init__`. And yes, `__init__` is short for initialize. With that in mind, let's make our intrepid adventurer.

---

```
hermione = Adventurer('Hermione', 1000, 100, 25, 'Warrior')
print(hermione.format())
```

---

We can also reuse our Adventurer class to create classes for specific
adventurer types.

```
class Bard(Adventurer):
    def __init__(self, name, health, experience, level):
        super(Bard, self).__init__(name, health, experience, level, 'Bard')


shakespeare = Bard('Shakespeare', 300, 5000, 100)


class Warrior(Adventurer):
    def __init__(self, name, health, experience, level):
        super(Warrior, self).__init__(name, health, experience, level,
                                      'Warrior')

hermione = Warrior('Hermione', 1000, 100, 25)
```

---

That’s it! (for now)

---

What else would you like to know?