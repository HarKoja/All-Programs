class human(object):
	def __init__(self):
		self.___name = None
		self.___family = None
		self.___age = None
		self._unnamed_car_ = []
		"""@AttributeType car*
		# @AssociationType car[]
		# @AssociationMultiplicity *"""

class car(object):
	def __init__(self):
		self.___model = None
		self.___color = None
		self.___plack = None
		self._unnamed_human_ = None
		"""@AttributeType human
		# @AssociationType human
		# @AssociationMultiplicity 1"""


