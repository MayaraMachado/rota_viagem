import logging
import random
from api.infrastructure.fileCSV import FileCSV
from api.infrastructure.fileTXT import FileTXT
from .graph_entity import Graph

class RouteDomain():
	'''
		This class is responsible for validating the possible routes in a graph.
	'''

	def __init__(self, filepath):
		'''
			Instantiates the RouteDomain object, and consequently calls the reading 
			of the file and calls the instantiation of the graph that will be used.

			Args:
			----
			- filepath (str) File path to be read and use to check the paths


			Raises:
			----
			- KeyError
				- Currently the API only supports .txt and .csv files, so if another 
				  type is passed, RouteDomain will throw an exception.

			- FileNotFoundError
				- If the file to be read is not found.
		'''

		file_accepted = {
			"csv" : FileCSV,
			"txt" : FileTXT
		}

		self.file = filepath
		ext = self.file.split('.')[-1]
		self.file_entity = file_accepted[ext](self.file)
		data = self.file_entity.get_lines()
		self.graph = Graph(data)
	
	def insert(self, routes):
		'''
			Insert new connections in the file and reflect these insertions in the graph.

			Args:
			----
			- lines (list of list)

			Returns:
			----

			- boolean indicating that creation was successful
		'''
		lines = []
		for route in routes:
			node, edge, cost = list(route.values())
			if not isinstance(cost, int):
				raise ValueError('Cost value invalid.')
			lines.append([node, edge, str(cost)])
			success = self.graph.add_node([node, edge, str(cost)])

		self.file_entity.write_file(lines)

		return success

	def __calculate_path(self, start, end):
		'''
			Dijkstra's algorithm implementation to search the best path in a graph with weight.

			Args:
			---
			start (str): The initial node where the function will go through.
			end (str): The final node where the function will consider the path complete.

			Returns:
			---

			dict containing the graph with the calculated best path to achieve each node.
			ex.:
			{"node1":0, "node2":("node_1", 2)}
		'''
				
		graph = self.graph.get_graph()
		# Open nodes will contain a list of tuples with the node and their respective cost. ex.[(node, cost)]
		open_nodes_exists = True
		open_nodes = {}
		discovered_path = {}
		current_node = (start, 0)

		# remove the starting node from the open ones
		discovered_path[current_node[0]] = current_node[1]

		# Iterate while there is nodes not visited yet
		# The first node to be verified will always be the first asked one.
		while open_nodes_exists:
			# iterate over the neighbors of a current node
			for node, cost in graph[current_node[0]].items():
				# calculate the weight to the neighbor through this new path
				node_weight = cost + current_node[1]
				# Verify if this path is discovered, and if it is verify if the weight is lower
				# coming from this new path. If so, mark this as the best way to reach this node.
				if not discovered_path.get(node) or discovered_path.get(node)[1] > node_weight:
					discovered_path[node] = (current_node[0], node_weight)
					open_nodes[node] = node_weight

			# If this was the last 
			if not open_nodes: 
				break    
			# Select as the new current, the less costly one of the open nodes
			current_node = min(open_nodes.items(), key=lambda x: x[1])
			del open_nodes[current_node[0]]
			

		return discovered_path

	def __get_best_path(self, calculated_connections, node, node_neighbor):
		'''
			Performs the search recursively to find the best way to reach the destination.

			Args:
			-----

			- calculated_connections (dict) contains the calculated value of the path to each 
			  node of the graph.
			- node (str) of the origin node.
			- node_neighbor (str) represents the next connected node to be searched.

			Returs:
			-----

			- string containing the list of the best path

			Raises:
			-----

			- ValueError
				- If the two nodes passed weren't connected.

		'''
		
		if node == node_neighbor:
			return node
		elif node_neighbor in calculated_connections and isinstance(calculated_connections[node_neighbor], tuple):
			return f"{self.__get_best_path(calculated_connections, node, calculated_connections[node_neighbor][0])} - {node_neighbor}"
		else:
			raise ValueError("The nodes are not connected.")

	def best_path(self, to, end):
		'''
			Check which path is least expensive from a source to a destination, and prepare 
			the message to be returned to the user

			Args:
			----
			- to (str) node to be the origin
			- end (str) node to be the destination

			Returns:
			-----
			- path (str) containing the best path
			- total_cost (int) containing the total cost from source to destination

			Raises:
			-----
			- AttributeError
				- If the node received as a parameter does not exist in the graph.

		'''

		node_exists = self.graph.verify_node_exists(to) and self.graph.verify_node_exists(end)

		if not node_exists:
			raise AttributeError("Node doesn't exists.")

		calculated_connections = self.__calculate_path(to, end)
		path = self.__get_best_path(calculated_connections, to, end)
		total_cost = calculated_connections.get(end)[1]
		return path, total_cost