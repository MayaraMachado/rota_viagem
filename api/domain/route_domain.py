import logging
import random
from api.infrastructure.fileCSV import FileCSV
from api.infrastructure.fileTXT import FileTXT
from .graph_entity import Graph

FILE_EXAMPLE = 'input-file-example.txt'

class RouteDomain():

	def __init__(self, filepath=None):
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

		file = filepath if filepath else FILE_EXAMPLE
		ext = file.split('.')[-1]
		self.file_entity = file_accepted[ext](file)
		data = self.file_entity.get_lines()
		self.graph = Graph(data)
	
	def insert(self, origin, end, cost):
		'''
		'''
		line = [[origin, end, str(cost)]]

		try:
			sucesso = self.file_entity.write_file(line)
		except Exception as e:
			logging.warning(e)
			sucesso = False

		return sucesso

	def __calculate_best_path(self, start, end):
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

	def best_path(self, to, end):
		path = self.__calculate_best_path(to, end)
		total_cost = path.get(end)[1]
		return 'Not implemented', total_cost