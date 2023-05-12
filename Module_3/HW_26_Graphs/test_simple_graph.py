from simple_graph import Vertex, Graph
import pytest


@pytest.fixture
def vertex_a():
    return Vertex('a', None)


@pytest.fixture
def vertex_b():
    return Vertex('b', None)


def test_vertex(vertex_a, vertex_b):
    v1 = Vertex('a', None)
    assert v1.name == 'a'
    assert v1.data is None
    assert v1 == vertex_a
    assert v1 != vertex_b


def test_new_neighbour(vertex_a):
    assert vertex_a.neighbours == {}
    assert vertex_a.new_neighbour('b', 2) is True
    assert vertex_a.neighbours == {'b': 2}
    assert vertex_a.new_neighbour('b', 2) is False
    assert vertex_a.neighbours == {'b': 2}
    assert vertex_a.show_neighbours() == ['b']
    assert vertex_a.show_connections() == '(a) <- 2 -> (b) '


@pytest.fixture
def graph():
    return Graph()


@pytest.fixture
def graph_with_vertexes():
    g = Graph()
    g.add_vertex('a', None)
    g.add_vertex('b', None)
    g.add_edge('a', 'b', 1)
    return g


def test_empty_graph(graph):
    assert graph.size == 0
    assert graph.edges_amount == 0
    assert graph.vertexes == {}
    assert graph.get_vertexes() == []
    assert graph.get_edges() == ()


def test_add_vertex(graph):
    assert graph.add_vertex('a', 'data') is True
    assert graph.add_vertex('a', 'another data') is False
    assert graph.add_vertex('b', None) is True
    assert graph.size == 2
    assert graph.edges_amount == 0
    assert graph.get_vertexes() == ['a', 'b']
    assert graph.get_edges() == ()


def test_connect_vertexes(graph):
    graph.add_vertex('a', None)
    graph.add_vertex('b', None)
    graph.add_vertex('c', None)
    assert graph.add_edge('a', 'b', 2) is True
    assert graph.add_edge('test_1', 'test_2', 2) is False
    assert graph.edges_amount == 1
    assert graph.add_edge('a', 'c', 4) is True
    assert graph.edges_amount == 2
    assert graph.get_edges() == (('a', 2, 'b'), ('a', 4, 'c'), ('b', 2, 'a'), ('c', 4, 'a'))


def test_remove_vertex(graph_with_vertexes):
    assert graph_with_vertexes.remove_vertex('not existed vertex') is False
    assert graph_with_vertexes.remove_vertex('b') is True
    assert graph_with_vertexes.get_vertexes() == ['a']
    assert graph_with_vertexes.vertexes['a'].neighbours == {}
    assert graph_with_vertexes.get_edges() == ()


def test_brake_edge(graph_with_vertexes):
    assert graph_with_vertexes.edges_amount == 1
    assert graph_with_vertexes.get_edges() == (('a', 1, 'b'), ('b', 1, 'a'))
    assert graph_with_vertexes.brake_edge('not existed vertex 1', 'not existed vertex 2') is False
    assert graph_with_vertexes.brake_edge('a', 'b') is True
    assert graph_with_vertexes.get_vertexes() == ['a', 'b']
    assert graph_with_vertexes.edges_amount == 0
    assert graph_with_vertexes.get_edges() == ()
