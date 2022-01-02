import pytest
from data_structures.graph import Graph


@pytest.fixture()
def basic_graph():
    adj_list = {
        "A": ["B", "F"],
        "B": ["A", "C"],
        "C": ["B", "D", "E", "F"],
        "D": ["C", "E"],
        "E": ["C", "F", "D"],
        "F": ["A", "C", "E"],
        "G": [],
        "H": ["I", "J"],
        "I": ["H", "J"],
        "J": ["H", "I"]
    }

    return Graph(adj_list)


def test_graph_init():
    default_init_graph = Graph()
    isinstance(default_init_graph, Graph)


def test_graph_init_with_default_values():
    adj_list = {"A": ["B", "C"], "B": ["A"], "C": ["A"]}
    adj_list_init_graph = Graph(adj_list)
    isinstance(adj_list_init_graph, Graph)
    assert adj_list_init_graph.get_adjacency_list() == adj_list


def test_graph_init_err():
    with pytest.raises(TypeError):
        _ = Graph("not a dict")


def test_graph_add_vertex():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("A")
    assert graph.get_vertices() == ["A", "B"]


def test_graph_add_edge():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B")
    assert graph.get_edges() == [["A", "B"]]


def test_graph_add_edge_err():
    graph = Graph()
    graph.add_vertex("A")
    with pytest.raises(ValueError):
        graph.add_edge("A", "B")


def test_graph_bfs(basic_graph):
    assert basic_graph.bfs("A") == {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 2, "F": 1
    }
    assert basic_graph.bfs("D") == {
        "A": 3, "B": 2, "C": 1, "D": 0, "E": 1, "F": 2
    }


def test_graph_bfs_err(basic_graph):
    with pytest.raises(ValueError):
        basic_graph.bfs("L")


def test_graph_distance(basic_graph):
    assert basic_graph.distance("A", "A") == 0
    assert basic_graph.distance("D", "B") == 2
    assert basic_graph.distance("A", "G") == -1
    assert basic_graph.distance("A", "H") == -1


def test_graph_distance_error(basic_graph):
    with pytest.raises(ValueError):
        basic_graph.distance("A", "L")
