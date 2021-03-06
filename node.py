class Node:
    __slots__ = "value", "link"

    def __init__(self, value, link=None):
        self.value = value
        self.link = link

    def __str__(self):
        return str(self.value, self.link)

    def __repr__(self):
        return 'Node ( ' + repr(self.value) + ', ' + repr(self.link) + ' )'


def test():
    nodes = Node(1, Node("two", Node(3.0)))
    n = nodes
    while n != None:
        print(n.value)
        n = n.link
    print()
    print(nodes)
    print(repr(nodes))


if __name__ == "__main__":
    test()
