# The __init__() function
# so in the last exercise we created this class planet. And based on this
# class, we created an object , which had all these attributes and a method
# as well. But we said if we created a new instance, it would have all the same
# property values.
# So what's the point of creating multiple instances?

class Planet:
    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    def __str__(self):
        return f"The planet's name is {self.name} with a radius of {self.radius} and gravity of {self.gravity}, in the {self.system}"

    def __repr__(self):
        return f'Planet Object: {self.name}, {self.radius}, {self.gravity}, {self.system}'

    # we need to implement another dunder method: __eq__()
    # this is another nice example that gives us a view through the
    # back door of how python works: everything is an object, defined
    # by classes, and all the class methods need to be written to work!
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


naboo = Planet('Naboo', 400000, 10, 'Naboo System')
#print(naboo)

# So what we're doing is creating is multiple instannces as this class


# --------------------------- #
#    EQUALITY AND IDENTITY    #
# --------------------------- #

# but after implementing the __eq__ dunder method, all is well! :)
# https://docs.python.org/3.6/reference/datamodel.html#object.__eq__
print(f"planets\n{'-' * 10}")
hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
another_hoth = hoth  # creating an ALIAS (a reference to the same object)
# both 'hoth' and 'another_hoth' refer to the same object
print(another_hoth == hoth)  # equality = same value
print(another_hoth is hoth)  # identity = same memory address (same object)
print(id(hoth))
print(id(another_hoth))  # same memory address

# EFFECTS OF ALIASING
# changing something through one variable, mutates the OBJECT
# therefore changes are also represented in the other variable
print(another_hoth.gravity, hoth.gravity)
hoth.gravity = 1  # assigning a new value to an alias
print(another_hoth.gravity, hoth.gravity)  # the value changed
# the reason why is IDENTITY: 'is' means same memory address (same object)
print(another_hoth is hoth)

# what about creating a new mirror Planet with the exact same parameters?
another_hoth = Planet(hoth.name, hoth.radius, hoth.gravity, hoth.system)
# alternatively this could also be accomplished like so:
# another_hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
# NOW: is it 'equal' (does it have all the same attributes)?
print(hoth == another_hoth)  # True: yep
# and does it have the same identity (is it the same object)?
print(hoth is another_hoth)  # False: nope
print(id(hoth))
print(id(another_hoth))  # different memory address


# --------------------------- #
# AND HERE'S THE TRICKY PART  #
# --------------------------- #

# small integers, floats and strings are CACHED in python!
# https://stackoverflow.com/a/2988271/5717580
# https://stackoverflow.com/a/306353/5717580
# https://wsvincent.com/python-wat-integer-cache/
# https://stackoverflow.com/questions/1504717/why-does-comparing-strings-in-python-using-either-or-is-sometimes-produce
# https://stackoverflow.com/questions/306313/is-operator-behaves-unexpectedly-with-integers

# this leads to unexpected results that don't make sense with the logic
# of equality and identity. uncomment the 'b = a' statements to test
# for the return values of the comparisons when creating ALIASES
# everything works consistently and makes sense (except for that caching...)
print(f"\n\nsmall ints\n{'-' * 10}")
a = 1
# b = a
b = 0 + 1
print(a == b)
print(a is b)
print(id(a))
print(id(b))  # same memory address... 😱

print(f"\n\nbig ints\n{'-' * 10}")
a = 19998989890
# b = a
b = 19998989889 + 1
print(a == b)
print(a is b)
print(id(a))
print(id(b))

print(f"\n\nsmall strings\n{'-' * 10}")
a = 'cheese'
# b = a
b = 'cheese'
print(a == b)
print(a is b)
print(id(a))
print(id(b))  # same memory address... 😱

print(f"\n\nbig strings\n{'-' * 10}")
a = 'cheese' * 100
# b = a
b = 'cheese' * 100
print(a == b)
print(a is b)
print(id(a))
print(id(b))

print(f"\n\nlists\n{'-' * 10}")
a = ['cheese', 'tomatoes']
# b = a
b = ['cheese', 'tomatoes']
print(a == b)
print(a is b)
print(id(a))
print(id(b))

print(f"\n\ntuples\n{'-' * 10}")
a = (1, 2)
# b = a
b = (1, 2)
print(a == b)
print(a is b)
print(id(a))
print(id(b))

print(f"\n\ndictionaries\n{'-' * 10}")
a = {1: 1, 2: 2}
# b = a
b = {1: 1, 2: 2}
print(a == b)
print(a is b)
print(id(a))
print(id(b))


