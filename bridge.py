class DrawingAPIOne(object):
	"""docstring for DrawingAPIOne"""
	def __init__(self):
		super(DrawingAPIOne, self).__init__()

	def draw_cirlce(self, x, y, radius):
		print("First dawhing api with cicle at ({}, {} with a radius of {})".format(x, y, radius))

class DrawingAPITwo(object):
	"""docstring for DrawingAPITwo"""
	def __init__(self, arg):
		super(DrawingAPITwo, self).__init__()

	def draw_circle(self, x, y, radius):
		print("First dawhing api with cicle at ({}, {} with a radius of {})".format(x, y, radius))

class Circle(object):
	"""docstring for Circle"""
	def __init__(self, x, y, radius, drawing_api):
		super(Circle, self).__init__()
		self._x = x
		self._y = y
		self._radius = radius
		self._drawing_api = drawing_api

	def draw(self):
		self._drawing_api.draw_circle(self._x, self._y, self._radius)

	def scale(self, percent):
		self._radius *= percent

circle1 = Circle(1, 2, 3, DrawingAPIOne())
circle1.draw()

circle2 = Circle(2, 3, 4, DrawingAPITwo())
circle2.draw()