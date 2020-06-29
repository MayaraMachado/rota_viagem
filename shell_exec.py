import sys
from api.domain.route_domain import RouteDomain


def exec_shell(filepath):
	'''
	'''
	try:
		route_domain = RouteDomain(filepath)
	except TypeError as e:
		return "File not supported! Use only files .txt or .csv."
	except FileNotFoundError as e:
		return "File not found."

	from_node, to_node = list(map(str, input("please enter the route:").split('-')))
	best_path, cost = route_domain.calculate_best_path(from_node, to_node)
	
	best_path_fmt = " - ".join(best_path)
	response = f"{best_path_fmt} > ${cost}"

	return response



if __name__ == '__main__':
	filepath = sys.argv[1]
	print(exec_shell(filepath))

