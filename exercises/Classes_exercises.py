class Planet:

	def __init__(self):
# Self parameter which refers to the instnance of the object w'ere creating
# When we create a new object,  this self refers to the instance of the object we're creating
# So inside this method we can attach some attributes to the instance we will be creating.
		self.name = 'Hoth'
		self.radius = 2000000
		self.gravity = 5.5
		self.system = "Hoth System"

	def orbit(self):
		return f'{self.name} is orbiting in the {self.system}'
# We have cretated a class with an init fucntion
# which we've attached 
# Let's create a new instance of the object
# How do we do that? We use the class name, followed by parenthesis to say that we are invoking
# a new instance of this class, Planet. And when we call it, we are calling the method above and attaching
# the attributes below. # So now all the different attributes we've define will be accessible on 
# this variable, hoth, below.
hoth = Planet()
print(f'Name is {hoth.name}')
print(f' Radius is {hoth.radius}')
print (f' the gravity is {hoth.gravity}')
print(hoth.orbit())


# let's run it
# We;ve created a new instance of this class
# But this class has attibutes only, not methods
# But what we can do is attach methods
# To do this we come outside of the init function
# and we define a new method, a method we want to appear on the instance, but we have to put
# it below the init function

	
# So now we are returning this string when we call this function
# The problem with this method is if we are to call Planet for a new panet
# instance, it will get the exam same propoerties. But this can be fixed! 
# See classes_eercises_2.primary_key=True
