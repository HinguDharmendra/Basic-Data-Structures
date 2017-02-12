"""
    file_name   :   graph_maze.py
    version     :   11/29/2016 19:12, v1.0
    description :   This is Graph class. It implements a graph data structure by using graph_node.
                    It basically uses an adjacency list representation for our Graph.
                    It This is modified version of code provided by instructor in mycourses
"""

__author__ = ['Dharmendra Hingu (dph7305@g.rit.edu)']

from graph_node import Vertex


class Graph:
    __slots__ = 'vertex_list', 'vertices'

    def __init__(self):
        """
        Constructor to initialize graph. It puts list of all vertices to a dictionary.
        It also keeps track of number of vertices in a graph
        """
        self.vertex_list = {}
        self.vertices = 0

    def get_vertex(self, identifier):
        """
        This function returns None if the vertex is not in the vertex_list, else it returns the
        vertex that we are looking for.
        :param identifier: id of a vertex
        :return: None or Vertex
        """
        if identifier not in self.vertex_list:
            return None
        else:
            return self.vertex_list[identifier]

    def add_vertex(self, identifier):
        """
        This function adds a vertex to a graph. Also increments number of vertices in graph by 1
        :param identifier: id of a vertex
        :return: None
        """
        v = Vertex(identifier)
        self.vertex_list[identifier] = v
        if self.get_vertex(identifier) is None:
            self.vertices += 1

    def add_edge(self, from_vertex, to_vertex, cost=0):
        """
        This function adds an edge from from_vertex to to_vertex with the given cost.
        :param from_vertex: from_vertex identifier
        :param to_vertex: to_vertex identifier
        :param cost: cost of going from from_vertex to to_vertex
        :return: None
        """
        if from_vertex not in self.vertex_list:     # if not in
            self.add_vertex(from_vertex)            # add
        if to_vertex not in self.vertex_list:       # if not in
            self.add_vertex(to_vertex)              # add
        self.vertex_list[from_vertex].add_neighbor(self.vertex_list[to_vertex], cost)

    def __iter__(self):
        """
        This function overrides built-in iterator
        :return: iterator to graph vertices
        """
        return iter(self.vertex_list.values())

    def print_graph(self):
        """
        This function prints the graph. It uses defined iterator
        :return: None
        """
        print('ADJACENCY LIST representation of given graph, \n')
        for node in self:
            print(node)


def test_graph():
    """
    This is trivial test of graph. It creates a graph from dictionary of states and
    the connections between them
    :return: None
    """
    states = {
        'CT': ('MA', 'RI'),
        'MA': ('CT', 'NH', 'RI', 'VT'),
        'ME': ('NH',),
        'NH': ('MA', 'ME', 'VT'),
        'RI': ('CT', 'MA'),
        'VT': ('MA', 'NH')
    }
    ne = Graph()
    for state, nbr in states.items():
        for neighbor in nbr:
            ne.add_edge(state, neighbor)

    # for state in ne:
    #     print(state)
    ne.print_graph()


if __name__ == '__main__':
    test_graph()
