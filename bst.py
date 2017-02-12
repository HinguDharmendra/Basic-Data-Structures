from btnode import BTNode


class BinarySearchTree:
    __slots__ = 'root', 'size'

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, item):
        if self.root is None:
            self.root = BTNode(item)
        else:
            self.__insert(self.root, item)
        self.size += 1

    def __insert(self, node, item):
        if item < node.data:
            if node.left is None:
                node.left = BTNode(item)
            else:
                self.__insert(node.left, item)
        else:
            if node.right is None:
                node.right = BTNode(item)
            else:
                self.__insert(node.right, item)

    def contains(self, item):
        return self.__contains(self.root, item)

    def __contains(self, node, item):
        if node is None:
            return False
        elif item == node.data:
            return True
        elif item < node.data:
            return self.__contains(node.left, item)
        else:
            return self.__contains(node.right, item)

    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        if node is None:
            return 0  # 0 is height is being calculated as number of edges in the longest path from root
        else:
            return max(self.__height(node.left), self.__height(node.right)) + 1

    def __in_order(self, node):
        if node is None:
            return ''
        else:
            return self.__in_order(node.left) + str(node.data) + ' ' + self.__in_order(node.right)

    def in_order(self):
        return 'Inorder: ' + self.__in_order(self.root)

    def __pre_order(self, node):
        if node is None:
            return ''
        else:
            return str(node.data) + ' ' + self.__pre_order(node.left) + self.__pre_order(node.right)

    def pre_order(self):
        return 'Preorder: ' + self.__pre_order(self.root)

    def __post_order(self, node):
        if node is None:
            return ''
        else:
            return self.__post_order(node.left) + self.__post_order(node.right) + str(node.data) + ' '

    def post_order(self):
        return 'Postorder: ' + self.__post_order(self.root)

    def __str__(self):
        return self.in_order()

    def size_of_tree(self):
        return self.size

    def __get_ancestor(self, node, item):
        if node is None:
            return False
        if node.data == item:
            return True
        if self.__get_ancestor(node.left, item) or self.__get_ancestor(node.right, item):
            print(node.data, end=' ')

        return False

    def get_ancestor(self, item):
        if self.root is None:
            return 'The root node is empty'
        else:
            return self.__get_ancestor(self.root, item)

    def get_all_ancestors(self, node, item):
        if node is not None:
            # print('current node: ', str(node.data))
            if node.data == item:
                return
            elif node.data > item:
                print(node.data, end=' ')
                if node.left is not None:
                    self.get_all_ancestors(node.left, item)
            else:
                print(node.data, end=' ')
                if node.right is not None:
                    self.get_all_ancestors(node.right, item)

    def nodes_in_subtree(self, item):
        return self.__nodes_in_subtree(self.root, item)

    def __nodes_in_subtree(self, node, item):
        if node is not None:
            # print('current node', node.data)
            if node.data == item:
                return self.count_nodes(node)
            elif item < node.data and node.left is not None:
                return self.__nodes_in_subtree(node.left, item)
            elif item > node.data and node.right is not None:
                return self.__nodes_in_subtree(node.right, item)

    def count_nodes(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def __find_min(self, node):
        if node.left is not None:
            return self.__find_min(node.left)
        else:
            return node.data

    def find_min(self):
        if self.root is None:
            return None
        else:
            return self.__find_min(self.root)

    def __find_max(self, node):
        if node.right is not None:
            return self.__find_max(node.right)
        else:
            return node.data

    def find_max(self):
        if self.root is None:
            return None
        else:
            return self.__find_max(self.root)

    def find_path(self, node, path, paths):
        if node is None:
            return
        path.append(node.data)
        if node.left is None and node.right is None:
            paths.append(path)
        else:
            self.find_path(node.left, path, paths)
            self.find_path(node.right, path, paths)
        return paths

    def check_path(self, lst):
        paths = self.find_path(self.root, [], [])
        for path in paths:
            if lst in path:
                print(lst)
        else:
            print(None)


def _check_bst(node):
    if node.left is not None:
        if node.left.data < node.data:
            _check_bst(node.left)
            return True
        else:
            return False
    if node.right is not None:
        if node.right.data > node.data:
            _check_bst(node.right)
            return True
        else:
            return False


def test():
    # bt = BinarySearchTree()
    #
    # print(bt)
    # print(bt.pre_order())
    # print(bt.post_order())
    # print('Contains 239,', bt.contains(239))
    # print('Height:', bt.height())
    # print('Total nodes:', bt.size_of_tree())
    # print('Immediate Ancestor of 73')
    # bt.get_ancestor(73)
    # print()

    bt = BinarySearchTree()
    bt.insert(53)
    bt.insert(73)
    bt.insert(10)
    bt.insert(3)
    bt.insert(129)
    bt.insert(62)
    bt.insert(14)
    bt.insert(11)

    print()
    print(bt)
    print(bt.pre_order())
    print(bt.post_order())
    print('Contains 73,', bt.contains(73))
    print('Contains 239,', bt.contains(239))
    print('Height:', bt.height())
    print('Total nodes:', bt.size_of_tree())
    print('Immediate Ancestor of 73')
    bt.get_ancestor(73)
    print()
    print('Immediate Ancestor of 11')
    bt.get_ancestor(11)
    print()

    print('Get all ancestors of 11')
    bt.get_all_ancestors(bt.root, 11)
    print()
    print('Get all ancestors of 129')
    bt.get_all_ancestors(bt.root, 129)
    print()

    print('Nodes in sub-tree rooted at 53')
    print(bt.nodes_in_subtree(53))
    print('Nodes in sub-tree rooted at 73')
    print(bt.nodes_in_subtree(73))
    print('Nodes in sub-tree rooted at 11')
    print(bt.nodes_in_subtree(11))

    print('Find min, ')
    print(bt.find_min())

    print('Find max, ')
    print(bt.find_max())

    print(_check_bst(bt.root))
    # bt2 = BinarySearchTree()
    # # bt2.insert(34)
    # # bt2.insert(91)
    # # bt2.insert(98)
    # bt2 = BTNode(34, None, BTNode(91, None, BTNode(98)))
    # print(_check_bst(bt2))

    # print('Path, ', bt.check_path([1, 2]))
    # print('Path, ', bt.check_path([10, 14]))


if __name__ == '__main__':
    test()
