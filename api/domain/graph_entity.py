class Graph:

	def __init__(self, data):
		self.__graph = {}
		created = self.__create_graph(data)

	def __create_graph(self, values):
		'''
			This function is responsible for the graph creation,

		'''
		if not values:
			raise ValueError('Graph values is missing.')

		for value in values:
			if not isinstance(value, tuple) and len(value) != 3:
				raise ValueError('Graph with invalid values.')

			node, edge, weight = value

			if node in self.__graph:
				# Update a nodes's connections
				self.__graph[node].update({edge:int(weight)})
			else:
				# Create a node with the connection
				self.__graph[node] = {edge:int(weight)}
			
			# Add the connection to the graph, if its node
			# doesn't exists.
			if edge and edge not in self.__graph:
				self.__graph[edge] = {}

		return True

	def add_node(self, line):

		node, edge, cost = line
		connection = {edge:cost}

		if node in self.__graph:
			self.__graph[node].update(connection)
		else:
			self.__graph[node] = connection
		
		# Add the connection to the graph, if its node
		# doesn't exists.
		if edge not in self.__graph:
			self.__graph[edge] = {}

		return True

	def get_graph(self):
		return self.__graph

	def verify_node_exists(self, node):
		'''
		'''
		return node in self.__graph