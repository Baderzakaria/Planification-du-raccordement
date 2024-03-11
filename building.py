class Building:
	def __init__(self, id_building, list_infras):
		"""
 The __init__ function is called when the class is instantiated.
 It sets up the object with all of its properties and methods.

 :param self: Represent the instance of the class
 :param id_building: Identify the building
 :param list_infras: Store the list of infrastructures in a building
 :return: Nothing
 :doc-author: Trelent
 """
 		self.id_building = id_building
		self.list_infras = list_infras

	def get_building_difficulty(self):
		"""
 The get_building_difficulty function returns the sum of all the infrastructure values in a list.
 	This is used to determine how difficult it is to build a building.

 :param self: Refer to the object itself
 :return: The sum of all the infrastructure levels in a building
 :doc-author: Trelent
 """
		return sum(self.list_infras)

	def __lt__(self, building):
		return self.get_building_difficulty() < building.get_building_difficulty()

	def __repr__(self):
		return f"{self.id_building}"