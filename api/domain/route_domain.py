import logging
import random
from django.core.exceptions import ObjectDoesNotExist

from api.infrastructure.fileCSV import FileCSV
from api.infrastructure.fileTXT import FileTXT
from .graph_entity import Graph

class RouteDomain():

	def __init__(self, filepath):
		'''

			raises:
			----
			TypeError
			FileNotFoundError
		'''
		file_accepted = {
			"csv" : FileCSV,
			"txt" : FileTXT
		}

		ext = filepath.split('.')[-1]
		self.file_entity = file_accepted[ext](filepath)
		data = self.file_entity.get_lines()
		self.graph = Graph(data)
	
	def insert(self, origin, end, cost):
		'''
		'''
		line = [[origin, end, str(cost)]]
		success = False

		try:
			self.file_entity.write_file(line)
		except Exception as e:
			logging.warning(e)
			return success

		success = self.graph.add_node(line[0])

		return success

	def __calculate_path(self, start, end):
		'''
			Dijkstra's algorithm implementation to search the best path in a graph with weight.

			Args:
			---

			graph (Object): Graph Object where the function is going to search.
			start (str): The initial node where the function will go through.
			end (str): The final node where the function will consider the path complete.

			Returns:
			---

			Tuple containing a list of the shortest path and an integer for the calculated weight of the shortest path.
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
			# Select as the new current, the closest one of the open nodes
			current_node = min(open_nodes.items(), key=lambda x: x[1])
			del open_nodes[current_node[0]]
			

		return discovered_path

	def __get_best_path(self, calculated_connections, node, node_neighbor):
		'''
		'''
		
		if node == node_neighbor:
			return node
		elif node_neighbor in calculated_connections and isinstance(calculated_connections[node_neighbor], tuple):
			return f"{self.__get_best_path(calculated_connections, node, calculated_connections[node_neighbor][0])} - {node_neighbor}"
		else:
			raise ValueError("The nodes are not connected.")

	def best_path(self, to, end):
		node_exists = self.graph.verify_node_exists(to) and self.graph.verify_node_exists(end)

		if not node_exists:
			raise ObjectDoesNotExist("Node doesn't exists.")

		calculated_connections = self.__calculate_path(to, end)
		path = self.__get_best_path(calculated_connections, to, end)
		total_cost = calculated_connections.get(end)[1]
		return path, total_cost