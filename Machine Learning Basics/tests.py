class Node():
	def __init__(self, input_power):
		self.input_power = input_power

	def measure_input(self):
		input_p = self.input_power
		return input_p



x = Node(11)
print x.measure_input()