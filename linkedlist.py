from node import Node


class LinkedList:
    __slots__ = 'head', 'current'

    def __init__(self):
        self.head = None
        self.current = None

    def push(self, value):
        node = Node(value, None)
        if self.current is not None:
            self.current.link = node
        else:
            self.head = node
        self.current = node

    def pop(self, value):
        traverser = self.head
        while traverser.link is not None:
            if traverser.link.value == value:
                traverser.link = traverser.link.link
                return True
            traverser = traverser.link

        else:
            return False

    def find(self, value):
        traverser = self.head
        while traverser is not None:
            if traverser.value == value:
                return True
            traverser = traverser.link
        else:
            return False

    def is_empty(self):
        return self.head is None

    def __str__(self):
        result = 'LinkedList[ '
        start = self.head
        while start != None:
            result += str(start.value) + ' '
            start = start.link
        result += ']'
        return result

    insert = push
    delete = pop


def test_linkedlist():
    l = LinkedList()
    print(l)
    print(l.is_empty())
    l.insert(2190374)
    print(l)
    l.insert(973)
    print(l)
    l.insert(9303740)
    print(l)
    print(l.find(973))
    print('sasd', l.delete(973))
    print(l)
    print('sdhgjahsd', l.find(340803))
    print('HIngu')
    print('lshgahdkja;jdsgvnacga', l.delete(973))
    print(l.is_empty())


if __name__ == '__main__':
    test_linkedlist()
