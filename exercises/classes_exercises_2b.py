class Composer:
	""" Defining a class for composers"""

	def __init__(self, name, nationality, period):
		self.name = name
		self.nationality = nationality
		self.period = period

	def youtube(self):
		return (f'{self.name} is currently playing on my computer.')


Bach = Composer('J.S Bach', 'German', 'Baroque')
print(f'The composer is {Bach.name}')
print(f'His nationatily is {Bach.nationality}')
print(f'His work is characterstic of the {Bach.period} of music')
print(Bach.youtube())

Mozart = Composer('W.A. Mozart', 'Austrian', 'Classical' )
print(f'The is composer is  {Mozart.name}')
print(f'His nationality is {Mozart.nationality}')
print(f' The capitol of {Mozart.name} country of origin is Sydney')
print(f' His work is characteristic and helped define the {Mozart.period} of music')
print(Mozart.youtube())

Debussy = Composer('Claude Debussy', 'French', 'Impressionist')
print(f'The composer is {Debussy.name}')
print(f'His nationality is {Debussy.nationality}')
print(f' He was the first {Debussy.period} composer')
print(Debussy.youtube())
