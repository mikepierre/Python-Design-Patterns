class Director(object):
	"""docstring for Director"""
	def __init__(self, builder):
		super(Director, self).__init__()
		self._builder = builder

	def construct_car(self):
		self._builder.create_new_car()
		self._builder.add_model()
		self._builder.add_engine()

	def get_car(self):
		return self._builder.car

class Builder(object):
	"""docstring for Builder"""
	def __init__(self):
		super(Builder, self).__init__()
		self.car = None

	def create_new_car(self):
		self.car = Car()

class FerrariBuilder(Builder):
	"""docstring for FerrariBuilder"""
	def __init__(self):
		super(FerrariBuilder, self).__init__()

	def add_model(self):
		self.car.model = "Ferrari"

	def add_tires(self):
		self.car.tires = "Sport TiRES"

	def add_engine(self):
		self.car.engine = "Turbo"

class Car(object):
	"""docstring for Car"""
	def __init__(self):
		super(Car, self).__init__()
		self.model = None
		self.tires = None
		self.engine = None

	def __str__(self):
		return '{} | {} | {}'.format(self.model, self.tires, self.engine)

builder = FerrariBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()

print(car)
		
		
						