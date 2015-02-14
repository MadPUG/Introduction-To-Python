from __future__ import print_function  # Ignore this line until next month
# Section 2 of Lesson 5

# In this section we'll discuss creating our own classes. Python allows users
# to create their own classes (i.e., types) to represent data and provide
# custom methods.

# It's important to keep in mind that everything we've seen thus far has a
# class. A dictionary has the class name "dict". You'll remember we can create
# a dictionary like so:

{'a': 1}

# But we can create the same dictionary like this:

dict(a=1)

# Our custom classes will be used in a way similar to calling dict(a=1). Let's
# create the most basic class we can:


class MostBasicClassEver(object):
    pass

# This class is basically just a name and it declares no custom data
# attributes. We can make an instance of this class:

most_basic_class_ever = MostBasicClassEver()

# But we can't pass any custom data or attributes to it. If we did we'd get a
# TypeError because it doesn't take any arguments. Let's start building a
# role-playing game. We'll create an Adventurer class with some attributes:
# - name
# - health
# - experience
# - level


class Adventurer(object):
    def __init__(self, name, health, experience, level):
        self.name = name
        self.health = health
        self.experience = experience
        self.level = level

# So the first thing that should be intersting is that the method we're
# defining is __init__. If you're familiar with Java, this might be confusing.
# If you already know ruby, this should look somewhat familiar though. In
# Python, every class's initialization method is named __init__. And yes,
# __init__ is short for initialize. With that in mind, let's make our intrepid
# adventurer.

narcissus = Adventurer('Narcissus', 1000, 100, 25)

# Now let's look at what we can do with narcissus.

print("Our adventurer's name: {0}".format(narcissus.name))

# This is awesome, but we should probably have a good way of formatting our
# adventurer's information. So let's take a shot at making the class again.


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

# You'll now notice a pattern forming. __init__ and format both take a
# parameter that we're not explicitly passing in, "self". One of Python's
# guiding principles is "Explicit over implicit". In Python, whenever a method
# acts on an instance of a class, the instance is explicitly passed into the
# method by Python. "self" is always the binding to the instance of the class
# you're operating on.

# Now let's use it

narcissus = Adventurer('Narcissus', 1000, 100, 25, 'Bard')
print(narcissus.format())

# So in this case, "narcissus" is "self" inside of "format".

# We can also reuse our Adventurer class to create classes for specific
# adventurer types.


class Bard(Adventurer):
    def __init__(self, name, health, experience, level):
        super(Bard, self).__init__(name, health, experience, level, 'Bard')
