# An example of instance attributes, available on the instance only.
# Class level attributes available on the instance or class
# Class methods, available on instance or class
# and static methods, that don't take anything in other than the parameters
# that we pass it. They are accessible on the instance and the class itself.null=True


class Cyclist:
	'''defining a class of cyclists'''

	'''Defining a class level attribute, the same for all instnances of pro cyclists'''
	cardiovascular_fitness = 'extremely high'

	'''defining our init function, with instance level attributes'''
	def __init__(self, name, nationality, team, speciality):
		self.name = name
		self.nationality = nationality
		self.team = team
		self.speciality = speciality

	def TDF(self):
		return (f'{self.name} is riding in the the Tour de France')
	""" defining a class method"""
	
	@classmethod
	def commons(fit):
		return f'All pro cyclists have an {fit.cardiovascular_fitness} level of fitness because of doping.'

	@staticmethod
	def dur(duration = "twenty-one days"):
		return f'The Tour de France lasts {duration}'

Lemond = Cyclist('Greg Lemond', 'American', 'La Vie Claire', 'All arounder')
print(f"The rider's name is {Lemond.name}")
print(f'He is {Lemond.nationality}')
print(f'His team is {Lemond.team}')
print(f'He is known as the first and (perhaps only) Americna to win the Tour, but he is really an {Lemond.speciality}')
print(Lemond.TDF())

Cavendish = Cyclist('Mark Cavendish', 'British', 'Quick Step', 'Sprinter')
print(f"The rider's name is {Cavendish.name}")
print(f" He is {Cavendish.nationality}")
print(f'His team is {Cavendish.team}')
print(f'He is known for his achievements as a {Cavendish.speciality}')
print(Cavendish.TDF())

Pöstlberger = Cyclist('Pöstlberger', 'Austrian', 'Bora', 'Road Race')
print(f"The rider's name is {Pöstlberger.name}")
print(f'He is {Pöstlberger.nationality}')
print(f'He rides for the {Pöstlberger.team}')
print(f'He is known for his victory in the 2018 Austrian national {Pöstlberger.speciality}')
print(Pöstlberger.TDF())

print(f'All of these riders have an {Cyclist.cardiovascular_fitness} level of fitness')
print(Cyclist.commons())
print(Cyclist.dur())


