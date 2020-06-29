import unittest.mock 
import pytest
from api.domain.graph_entity import Graph

# teste criar grafo sem passar valores
def test_create_graph_without_data():
    data = []
    with pytest.raises(ValueError):
        graph = Graph(data)

# teste criar grafo sem vertices
def test_create_graph_with_nodes_without_edges():
    data = [('GRU'), ('BRC'),('SCL'), ('ORL'), ('CDG')]
    with pytest.raises(ValueError):
        graph = Graph(data)

# test criar e obter um grafo
def test_create_graph():
    data = [('GRU', 'CDG', 75), ('GRU', 'BRC', 10),('GRU', 'SCL', 20), ('GRU', 'ORL', 56), ('BRC', 'SCL', 5), ('SCL', 'ORL', 20), ('ORL', 'CDG', 5)]
    graph = Graph(data)
    expected_graph = {  "GRU":{
                            "CDG":75,
                            "BRC":10,
                            "SCL":20,
                            "ORL":56
                        },
                        "CDG":{},
                        "BRC":{
                            "SCL":5
                        },
                        "SCL":{
                            "ORL":20
                        },
                        "ORL":{
                            "CDG":5
                        }
                    }

    assert graph.get_graph() == expected_graph

# teste add um novo node no 
def test_add_new_node_to_graph():
    data = [('GRU', 'CDG', 75)]
    graph = Graph(data)
    node = "NEW"
    edges = {"NODE":1}
    graph.add_node(node, edges)
    expected_graph={'GRU': {'CDG': 75},
                    'CDG': {},
                    'NEW': {'NODE': 1},
                    'NODE' : {}
                    }

    assert graph.get_graph() == expected_graph

# teste não passar valores
def test_add_new_edge_to_node():
    data = [('GRU', 'CDG', 75), ('NEW', 'NODE', 1)]
    graph = Graph(data)
    node = "NEW"
    edges = {"EDGE":2}
    graph.add_node(node, edges)
    expected_graph={'GRU': {'CDG': 75},
                    'CDG': {},
                    'NEW': {'NODE': 1,'EDGE' : 2},
                    'NODE' : {},
                    'EDGE' : {}
                    }

    assert graph.get_graph() == expected_graph
