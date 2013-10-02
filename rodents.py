class Rodent:

#need to first define constructor
	def __init__(self, tag_id):
		self.tag_id = tag_id
		self.weights = []

	def plot(self):
		return self.tag_id[0]

	def add_weight(self, weight):
		self.weights.append(weight)
	
