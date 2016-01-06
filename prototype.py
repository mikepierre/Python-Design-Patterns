import copy

class Prototype(object):
	"""docstring for Prototype"""
	def __init__(self):
		super(Prototype, self).__init__()
		self._objects = {}

	def register_object(self, name, obj):
		self._objects[name] = obj

	def unregister_object(self, name):
		del self._objects[name]

	def clone(self, name, **attr):
		obj = copy.deepcopy(self._objects.get(name))
		obj.__dict__.update(attr)
		return obj

class Car(object):
	"""docstring for Car"""
	def __init__(self):
		super(Car, self).__init__()
		self.name = "Ferrari"
		self.color = "Red"
		self.options = "360"

	def __str__(self):
		return '{} | {} | {}'.format(self.name, self.color, self.options)

c = Car()
prototype = Prototype()
prototype.register_object('Ferrari',c)

c1 = prototype.clone('Ferrari')

print(c1)