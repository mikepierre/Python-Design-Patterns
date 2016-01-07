class Dog(object):
	"""docstring for Dog"""
	def __init__(self):
		super(Dog, self).__init__()

	def speak(self):
		return "ruff, ruff :|"

	def __str__(self):
		return "Doggy"

class DogFactory(object):
	"""docstring for DogFactory"""
	def __init__(self):
		super(DogFactory, self).__init__()

	def get_food(self):
		return "Dog food"

	def get_pet(self):
		return Dog()

class PetStore(object):
	"""docstring for PetStore"""
	def __init__(self, pet_factory=None):
		super(PetStore, self).__init__()
		self._pet_factory = pet_factory

	def show_pet(self):
		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("This is our pet '{}'".format(pet))
		print("He/she does '{}'".format(pet.speak()))
		print("Eats '{}'".format(pet_food))

factory = DogFactory()

shop = PetStore(factory)

shop.show_pet()
		
		
		