"""
    file_name   :   graph_node.py
    version     :   11/29/2016 19:12, v1.0
    description :   This is graph node or vertex, which stores its identity as identifier and
                    vertices to which this vertex is connected. This is modified version of code
                    provided by instructor in mycourses
"""

__author__ = ['Dharmendra Hingu (dph7305@g.rit.edu)']


class Vertex:
    __slots__ = "identifier", "connectedTo"

    def __init__(self, identifier):
        """
        Constructor to initialize vertex
        :param identifier: id of vertex
        """
        self.identifier = identifier
        self.connectedTo = {}  # dictionary of vertices to which this vertex is connected

    def add_neighbor(self, identifier, cost=0):
        """
        This function adds a vertex to this vertex's dictionary as its neighbor
        :param identifier: id of vertex
        :param cost: cost of going from this vertex to which other vertex
        :return: None
        """
        self.connectedTo[identifier] = cost

    def get_all_neighbors(self):
        """
        This function returns all the vertices to which this vertex is connected
        :return: list of vertices
        """
        return self.connectedTo.keys()

    def get_cost(self, identifier):
        """
        This function returns the cost associated with this vertex
        :param identifier: id of vertex
        :return: cost
        """
        return self.connectedTo[identifier]

    def __str__(self):
        """
        This function overrides built-in __str__ method
        :return: string representation of vertex
        """
        return '' + str(self.identifier) + ' = ' + str([str(nbr.identifier) for nbr in self.connectedTo])


def test_vertex():
    """
    This is trivial test of graph node. It creates bunch of vertices and adds neighbors
    :return: None
    """
    student = Vertex('Student')
    maths = Vertex('Mathematics')
    cs = Vertex('Computer Science')
    bm = Vertex('Business Management')
    wd = Vertex('Web Development')
    student.add_neighbor(maths, 7)
    student.add_neighbor(cs, 9)
    student.add_neighbor(bm, 6)
    student.add_neighbor(wd, 9)
    print(student.identifier)
    print(student)


if __name__ == '__main__':
    test_vertex()
