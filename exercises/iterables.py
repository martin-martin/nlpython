# ----------------------------------
# using the iter() function
# ----------------------------------
chars = list('casey')  # quick way to make a list from a string

# iter() creates an 'iterator object'
print(iter(chars))

# so you can iterate over it!
for c in iter(chars):
    print(c)

# ----------------------------------

# same goes with some other data types, e.g. zip objects
zeeep = zip(list('hello'), chars)

print(zeeep)

for i in iter(zeeep):
    print(i)  # as expected, the zip() object consists of tuples

# ----------------------------------

# however, when creating a dictionary from it, things can get hairy:

d = dict(zeeep)
print(d) # the dictionary is empty! why so?

for k, v in iter(d.items()):  # iterating on an empty dict won't do much
    print(k, v)

# buuuut: what about this! why is the below working as expected,
# while the above is not?

zeeep2 = zip(chars, list('hello'))

d2 = dict(zeeep2)
print(d2)

for k, v in iter(d2.items()):
    print(k, v)

# HINT: what is a requirement for a key in order to live in a dictionary?
