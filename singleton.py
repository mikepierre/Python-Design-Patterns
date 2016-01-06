class Borg(object):
	"""docstring for Borg"""
	_shared_data = {}

	def __init__(self):
		super(Borg, self).__init__()
		self.__dict__ = self._shared_data
		
class Singleton(Borg):
	"""docstring for Singleton"""
	def __init__(self, **kwargs):
		Borg.__init__(self)
		self._shared_data.update(kwargs)

	def __str__(self):
		return str(self._shared_data)

x = Singleton(HTTP="That Hyper Text Protocol")
print(x)

y = Singleton(MIKE="Michael")
print(y)

		