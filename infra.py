class Infra :
	def __init__(self, infra_id, length, infra_type, nb_houses):
		"""
 The __init__ function is called when a new instance of the class is created.
 The self parameter refers to the newly created object, and is used to set
 values for object variables (i.e., self.x = x), or other operations that are
 part of initialization.

 :param self: Represent the instance of the class
 :param infra_id: Give the infrastructure a unique id
 :param length: Set the length of the infrastructure
 :param infra_type: Determine the type of infrastructure
 :param nb_houses: Determine the number of houses that are connected to this infrastructure
 :return: An object
 :doc-author: Imene
 """
 		self.infra_id = infra_id
		self.length = length
		self.infra_type = infra_type
		self.nb_houses = nb_houses

	def repair_infra(self):
		self.infra_type = "infra_intacte"

	def get_infra_difficulty(self):
		return 0 if self.infra_type == "infra_intacte" else self.length / self.nb_houses

	def __radd__(self, other_infra):
		"""
 The __radd__ function is called when the object on the right side of an addition operation does not implement __add__.
 This function should return a value that, when added to the left operand, gives an equivalent result to adding both operands together with __add__.
 For example:

 :param self: Refer to the instance of the class
 :param other_infra: Add the difficulty of another infrastructure to the current one
 :return: The sum of the object's infra difficulty and another infrastructure
 :doc-author: Imene
 """
 		return self.get_infra_difficulty() + other_infra

	def __repr__(self):
		"""
 The __repr__ function is the official string representation of an object.
 It's what you get when you type the object name at the Python prompt, or pass it to str().
 The goal of __repr__ is to be unambiguous: if eval(repr(x)) == x, then __repr__ should return a string that looks like a valid Python expression that could be used to recreate an object with the same value (given an appropriate environment). If this is not possible, a string formatted using %s formatting should be returned.

 :param self: Represent the instance of the class
 :return: The printable representation of the object
 :doc-author: Imene
 """
 		return f"{self.infra_id}"
