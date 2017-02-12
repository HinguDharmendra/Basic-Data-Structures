from node import Node


class Stack:
    """
    This class represents linked stack
    """
    __slots__ = "top"

    def __init__(self):
        """
        Constructor
        """
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        """
        This method pushes data on top of stack
        :param value: data
        :return: true once data is pushed
        """
        self.top = Node(value, self.top)

    def pop(self):
        """
        This comparator pops the element of the stack at top
        :return: data of popped element
        """
        result = None
        if not self.is_empty():
            result = self.top.value
            self.top = self.top.link
        return result

    def peek(self):
        """
        This method returns top of the stack
        :return: data of node at top
        """
        if not self.is_empty():
            return self.top.value

    def __str__(self):
        """
        This is equivalent to toString method, converts the object to String
        :return: string representation of object
        """
        result = 'Stack[ '
        n = self.top
        while n is not None:
            result += str(n.value) + ' '
            n = n.link
        result += ']'
        return result

    insert = push
    remove = pop


def test_stack():
    s = Stack()
    print(s)
    print(s.pop())
    for i in 12, 54, 8:
        s.insert(i)
    print(s)
    print(s.peek())
    print(s.pop())
    print(s)
    print(s.is_empty())


if __name__ == '__main__':
    test_stack()
