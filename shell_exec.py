import sys
from api.domain.route_domain import RouteDomain


def exec_shell(filepath):
	'''
	'''
	try:
		route_domain = RouteDomain(filepath)
	except KeyError as e:
		return "File not supported! Use only files .txt or .csv."
	except FileNotFoundError as e:
		return "File not found."

	try:
		print("Please use - to separate the locations. Ex.: ONE - ANOTHER")
		from_node, to_node = list(map(str, input("please enter the route:").split('-')))
	except ValueError as e:
		return "Invalid input."

	from_node = from_node.replace(" ", "").upper()
	to_node = to_node.replace(" ", "").upper()

	try:
		best_path, cost = route_domain.best_path(from_node, to_node)
	except ValueError as e:
		return "The nodes are not connected."
	except AttributeError as e:
		return "Please, send two valid locations to verify: origin and destination."
	
	response = f"{best_path} > ${cost}"
	return response


if __name__ == '__main__':
	filepath = sys.argv[1]
	print(exec_shell(filepath))

