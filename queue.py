from node import Node


class Queue:
    __slots__ = "front", "rear"

    def __init__(self):
        """
        Constructor
        """
        self.front = None
        self.rear = None

    def is_empty(self):
        """
        Checks of the queue is empty
        :return:
        """
        return self.front is None

    def push(self, value):
        node = Node(value, None)
        if self.front is None:
            self.front = node
        else:
            self.rear.link = node
        self.rear = node

    def pop(self):
        if not self.is_empty():
            result = self.front.value
            if self.front.link is not None:
                self.front = self.front.link
            else:
                self.front = None
                self.rear = None
            return result
        else:
            print('Can\'t pop empty queue')

    def __str__(self):
        result = 'Queue[ '
        start = self.front
        while start is not None:
            result += str(start.value) + ' '
            start = start.link
        result += ']'
        return result

    enqueue = push
    dequeue = pop


def test_queue():
    q = Queue()
    print(q)
    q.dequeue()
    q.enqueue(923)
    print(q)
    q.enqueue(23958)
    print(q)
    q.enqueue(2)
    print(q)
    q.enqueue(1048)
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.is_empty())


if __name__ == '__main__':
    test_queue()
