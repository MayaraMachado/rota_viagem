class Graph:

	def __init__(self, data):
		self.__graph = {}
		self.__format_to_graph(data)

	def __format_to_graph(self, values):
		'''
		'''
		if not values:
			raise ValueError('Grpah without values.')

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

	def add_node(self, node, edges={}):
		if node in self.__graph:
			self.__graph[node].update(edges)
		else:
			self.__graph[node] = edges
		
		# Add the connection to the graph, if its node
		# doesn't exists.
		for edge in edges.keys():
			if edge not in self.__graph:
				self.__graph[edge] = {}

	def get_graph(self):
		return self.__graph
