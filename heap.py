class Heap:
    __slots__ = 'data', 'size', 'comparator'

    def __init__(self, comparator):
        self.data = []
        self.size = 0
        self.comparator = comparator

    def _get_parent(self, loc):
        return (loc - 1) // 2

    def insert(self, item):
        self.data.append(item)
        self.size += 1
        self._bubble_up(self.size - 1)

    def _bubble_up(self, size):
        while size > 0 and self.comparator(self.data[size], self.data[self._get_parent(size)]):
            self.data[size], self.data[self._get_parent(size)] = self.data[self._get_parent(size)], self.data[size]
            size = self._get_parent(size)

    def remove(self):
        result = None
        if len(self.data) > 0:
            result = self.data[0]
            self.size -= 1

        if self.size > 0:
            self.data[0] = self.data.pop(self.size)
            self._bubble_down(0)
        else:
            self.data = []

        return result

    def _bubble_down(self, size):
        loc = self.__get_smallest_child(size)
        while size != loc:
            self.data[loc], self.data[size] = self.data[size], self.data[loc]
            size = loc
            loc = self.__get_smallest_child(size)

    def __get_smallest_child(self, index_parent):
        index_left_child = index_parent * 2 + 1
        index_right_child = index_parent * 2 + 2

        # if there are no children
        if index_left_child >= self.size:
            return index_parent

        # if there is left child but no right child
        if index_right_child >= self.size:
            if self.comparator(self.data[index_parent], self.data[index_left_child]):
                return index_parent
            else:
                return index_left_child

        # if there are both left and right child
        if self.comparator(self.data[index_right_child], self.data[index_left_child]):
            if self.comparator(self.data[index_parent], self.data[index_right_child]):
                return index_parent
            else:
                return index_right_child
        else:
            if self.comparator(self.data[index_parent], self.data[index_left_child]):
                return index_parent
            else:
                return index_left_child

    def __str__(self):
        res = '\t\t'
        if len(self.data) <= 0:
            res += "Heap is empty"
        for item in self.data:
            res += str(item) + ' '
        return res

    def __len__(self):
        return len(self.data)

    add = insert
    delete = remove


def test():
    heap = Heap(lambda x, y: x > y)
    heap.insert(3)
    heap.insert(2)
    heap.insert(293)
    heap.insert(22)
    heap.insert(349)
    heap.insert(23)
    print(heap)

    print('->1', heap.remove())
    print(heap)
    print('->2', heap.remove())
    print(heap)
    print('->3', heap.remove())
    print(heap)
    print('->4', heap.remove())
    print(heap)
    print('->5', heap.remove())
    print(heap)
    print('->6', heap.remove())
    print(heap)
    print('->7', heap.remove())
    print(heap)
    print('->8', heap.remove())
    print(heap)
    print('->9', heap.remove())
    print(heap)


if __name__ == '__main__':
    test()
