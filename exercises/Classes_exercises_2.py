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


naboo = Planet('Naboo', 400000, 10, 'Naboo System')
print(naboo)
print(repr(naboo))

hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
print(hoth)
print(repr(hoth))

# So what we're doing is creating is multiple instannces as this class

