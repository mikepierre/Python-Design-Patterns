class Dog(object):
	"""docstring for Dog"""
	def __init__(self, name):
		super(Dog, self).__init__()
		self.name = name

	def speak(self):
		return "Ruff, ruff..."

class Cat(object):
	"""docstring for Cat"""
	def __init__(self, name):
		super(Cat, self).__init__()
		self.name = name

	def speak(self):
		return "meow?"


def get_pet(pet="dog"):
	"""Factory Method"""
	pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

	return pets[pet]

d = get_pet("dog")

print(d.speak())

c = get_pet("cat")

print(c.speak())
		
		