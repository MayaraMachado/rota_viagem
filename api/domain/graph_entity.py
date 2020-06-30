class Graph:
	'''
		This class is responsible for the representation of the graph. 
		It was implemented in a very simple way, and uses only dictionaries 
		to compose a graph.
	'''

	def __init__(self, data):
		self.__graph = {}
		created = self.__create_graph(data)

	def __create_graph(self, values):
		'''
			For the creation of the graph, the function receives a list of lists 
			that is the result of reading the file. Then it iterates over that list 
			and turns each line into a node in the graph, if that node already exists 
			the function will just add as a new connection to the existing node.

			Args:
			-----
			- values (list of lists): The values ​​referring to nodes, connections and weight 
			of the connection.

			Returns:
			-----
			- boolean indicating that creation was successful

			Raises:
			-----
			- ValueError
				- If no value is passed;
				- If line values ​​are not formatted in the list of tuple like ("node, edge, cost")
				  pattern, an exception will be thrown over invalid value.
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
		'''
			In this function it is possible to add a new node and / or edge to the graph.

			Args:
			----
			- line (list of string) with the node, edge e cost values.

			Returns:
			----

			- boolean indicating that creation was successful
		'''
		node, edge, cost = line
		connection = {edge:int(cost)}

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
		'''
			This function returns the graph created.

			Returns:
			----
			graph (dicts of dicts)
		'''
		return self.__graph

	def verify_node_exists(self, node):
		'''
			Checks if a node exists in the graph		.

			Args:
			----
			- node (str)

			Returns:
			----
			- boolean indicating whether or not there is.
		'''
		return node in self.__graph