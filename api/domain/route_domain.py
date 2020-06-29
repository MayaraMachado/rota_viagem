import logging
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

	def calculate_best_path(self, start, end):
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
		open_nodes = list(graph.keys())
		discoverd_path = {}
		best_path = []
		current_node = (start, 0)

		# remove the starting node from the open ones
		open_nodes.remove(current_node[0])
		best_path.append(start)

		while len(open_nodes) > 0:
			neighbor_nodes = {}
			for node, cost in graph[current_node[0]].items():
				node_weight = cost + current_node[1]
				neighbor_nodes[node] = node_weight
				if not discoverd_path.get(node) or discoverd_path.get(node) > node_weight:
					discoverd_path[node] = node_weight

			if end in list(neighbor_nodes.keys()):
				current_node = (end, neighbor_nodes[end])
				break
			else:
				current_node = min(neighbor_nodes.items(), key=lambda x:x[1])
				best_path.append(current_node[0])
			open_nodes.remove(current_node[0])

		best_path.append(current_node[0])
		best_cost = current_node[1]
		return best_path, best_cost
