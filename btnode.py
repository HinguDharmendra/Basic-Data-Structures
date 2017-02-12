class BTNode:
    __slots__ = "data", "left", "right"

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return '\nThe binary node is, ' + str(self.data) + '\nleft child is, ' + str(
            self.left) + ' and \nright child is, ' + str(self.right)


def test_node():
    node = BTNode(5)
    print(node)
    node = BTNode(5, BTNode(3), BTNode(9))
    print(node)


if __name__ == '__main__':
    test_node()
