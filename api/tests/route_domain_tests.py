import unittest.mock 
import pytest
from api.domain.route_domain import RouteDomain

# teste não passar arquivo na criação 
def test_create_route_domain_object():
    filepath = "files/input-file-test.csv"
    route_domain = RouteDomain(filepath)
    assert route_domain.file == "files/input-file-test.csv"

# teste passar um arquivo que não existe
def test_create_route_domain_with_inexistent_file():
    filepath = "files/invalid-input-file-test.csv"
    with pytest.raises(FileNotFoundError):
        route_domain = RouteDomain(filepath)

# teste passar uma extensão que não é suportada
def test_create_route_domain_with_inexistent_file():
    filepath = "files/invalid-input-file-test.pdf"
    with pytest.raises(KeyError):
        route_domain = RouteDomain(filepath)

# inserir uma linha no arquivo
def test_insert_invalid_new_route():
    filepath = "files/input-file-test.csv"
    origin, end, cost = 'NewOrigin', 'NewDestination', "invalid"
    route_domain = RouteDomain(filepath)
    with pytest.raises(ValueError):
        route_domain.insert(origin,end, cost)

# inserir conexão com custo float, deve tornar inteiro
def test_insert_invalid_new_route():
    filepath = "files/input-file-test.csv"
    origin, end, cost = 'NewOrigin', 'NewDestination', 3.5
    route_domain = RouteDomain(filepath)
    with pytest.raises(ValueError):
        route_domain.insert(origin,end, cost)

# teste calcular o melhor caminho
def test_get_best_path():
    filepath = "files/input-file-test.csv"
    to_node, from_node = 'GRU', 'CDG'
    route_domain = RouteDomain(filepath)
    best_path_response, total_cost_response = route_domain.best_path(to_node, from_node)
    assert best_path_response == "GRU - BRC - SCL - ORL - CDG"
    assert total_cost_response == 40

# teste local que não existe
def test_get_best_path_from_location_invalid():
    filepath = "files/input-file-test.csv"
    to_node, from_node = 'GRU', 'non_exist'
    route_domain = RouteDomain(filepath)
    with pytest.raises(AttributeError):
        best_path_response, total_cost_response = route_domain.best_path(to_node, from_node)

# inserir uma linha no arquivo
def test_insert_new_route():
    filepath = "files/input-file-test.csv"
    origin, end, cost = 'NewOrigin', 'NewDestination', 1009
    route_domain = RouteDomain(filepath)
    assert route_domain.insert(origin,end, cost) == True


# teste calcular o melhor caminho de um caminho que não conversa
def test_get_best_path_from_location_invalid():
    filepath = "files/input-file-test.csv"
    new_origin, new_end, cost = 'SCL', 'ALM', 5
    to_node, from_node = 'ALM', 'CDG'

    route_domain = RouteDomain(filepath)
    updated = route_domain.insert(new_origin, new_end, cost)

    with pytest.raises(ValueError):
        best_path_response, total_cost_response = route_domain.best_path(to_node, from_node)

