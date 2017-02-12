"""
Solution file to Practical Exam #2 in CSCI 603 -- Fall, 2016, Purtee.
Original author (all functions except findPath/pathSum and helpers) below.

CSCI-603: Trees (week 10)
Author: Sean Strout @ RIT CS

This is an implementation of a binary search tree.
"""

from btnodep2 import BTNode


class BST:
    """
    A binary search tree consists of:
    :slot root: The root node of the tree (BTNode)
    :slot size: The size of the tree (int)
    """
    __slots__ = 'root', 'size'

    def __init__(self):
        """
        Initialize the tree.
        :return: None
        """
        self.root = None
        self.size = 0

    def __insert(self, val, node):
        """
        The recursive helper function for inserting a new value into the tree.
        :param val: The value to insert
        :param node: The current node in the tree (BTNode)
        :return: None
        """
        if val < node.val:  # check if need to go left
            if node.left == None:  # if no left child
                node.left = BTNode(val)  # insert it here
            else:  # otherwise
                self.__insert(val, node.left)  # traverse with the left node
        else:  # need to go right
            if node.right == None:  # if no right child
                node.right = BTNode(val)  # insert it here
            else:  # otherwise
                self.__insert(val, node.right)  # traverse with the right node

    def insert(self, val):
        """
        Insert a new value into the tree
        :param val: The value to insert
        :return: None
        """
        if self.root == None:  # if tree is empty
            self.root = BTNode(val)  # create root node with the value
        else:  # otherwise
            self.__insert(val, self.root)  # call helper function with root
        self.size += 1

    def __contains(self, val, node):
        """
        The recursive helper function for checking if a value is in the tree.
        :param val: The value to search for
        :param node: The current node (BTNode)
        :return: True if val is present, False otherwise
        """
        if node == None:  # if there is no node
            return False  # we went past a leaf and the val is not there
        elif val == node.val:  # if the values match
            return True  # return success
        elif val < node.val:  # if no match, but val is lesser
            return self.__contains(val, node.left)  # recurse with left node
        else:  # otherwise
            return self.__contains(val, node.right)  # recurse with right node

    def contains(self, val):
        """
        Returns whether a value is in the tree or not.
        :param val: The value to search for
        :return: True if val is present, False otherwise
        """
        # call the recursive helper function with the root node
        return self.__contains(val, self.root)

    def __height(self, node):
        """
        The recursive helper function for computing the height of a node
        :param node: The current node (BTNode)
        :return: The height of node (int)
        """
        if node == None:  # if no node
            return -1  # the height is -1
        else:  # otherwise
            # add 1 to the greater of the left or right node's height
            return 1 + max(self.__height(node.left), self.__height(node.right))

    def height(self):
        """
        Return the height of a tree.  Recall:
            - The height of an empty tree is -1
            - The height of a tree with one node is 0
            - Otherwise the height is one plus the larger of the heights of
            the left or right children.
        :return: The height (int)
        """
        # just call the recursive helper function with the root node
        return self.__height(self.root)

    def __inorder(self, node):
        """
        The recursive inorder traversal function that builds a string
        representation of the tree.
        :param node: The current node (BTNode)
        :return: A string of the tree, e.g. "1 2 5 9 "
        """
        if node == None:  # if we went past a leaf
            return ' '  # append a space
        else:  # otherwise
            # construct a string in order from left to current to right
            return self.__inorder(node.left) + \
                   str(node.val) + \
                   self.__inorder(node.right)

    def __str__(self):
        """
        Return a string representation of the tree.  By default this will
        be a string with the values in order.
        :return:
        """
        # call the recursive helper function with the root node
        return self.__inorder(self.root)

    def pathSum(self, value):
        return self.__pathSum(self.root, value, True)

    def __pathSum(self, node, value, skip):
        if node.val == value:
            return True
        elif (not skip):
            if value - node.val > 0:
                if node.left and self.__pathSum(node.left, value - node.val, False):
                    return True
                elif node.right and self.__pathSum(node.right, value - node.val, False):
                    return True
            return False
        else:
            if node.left and self.__pathSum(node.left, value - node.val, False):
                return True
            elif node.right and self.__pathSum(node.right, value - node.val, False):
                return True
            elif node.left and self.__pathSum(node.left, value, True):
                return True
            elif node.right and self.__pathSum(node.right, value, True):
                return True
            else:
                return False

    def findPath(self, lst):
        return lst and self.__findPath(self.root, lst)

    def __findPath(self, node, lst):
        n = node.left and self.__findPath(node.left, lst)
        if n:
            return n
        if self.__checkPath(node, lst):
            return node
        n = node.right and self.__findPath(node.right, lst)
        if n:
            return n
        return None

    def __checkPath(self, node, lst):
        if len(lst) == 0 or node is None:
            return node
        elif node.val == lst[0]:
            if len(lst) == 1 or self.__checkPath(node.left, lst[1:]) or self.__checkPath(node.right, lst[1:]):
                return node
        return None


def testFP():
    bt = BST()
    bt.insert(6)
    bt.insert(3)
    bt.insert(9)
    bt.insert(1)
    bt.insert(5)
    bt.insert(7)
    bt.insert(12)
    bt.insert(15)

    print("Ts")
    for p in [[3, 5], [9, 12, 15], [6, 9, 7], [1]]:
        print(str(p) + " " + str(bt.findPath(p)))

    print("Fs")
    for p in [[5, 3], [16], [6, 12], [3, 9]]:
        print(str(p) + " " + str(bt.findPath(p)))


def testPS():
    bt = BST()
    bt.insert(6)
    bt.insert(3)
    bt.insert(9)
    bt.insert(1)
    bt.insert(5)
    bt.insert(7)
    bt.insert(12)
    bt.insert(15)

    print("Ts")
    for v in [3, 6, 9, 14, 27]:
        print(str(v) + " " + str(bt.pathSum(v)))

    print("Fs")
    for v in [2, 40, 18, 28]:
        print(str(v) + " " + str(bt.pathSum(v)))


def testBST():
    """
    Test function for the binary search tree.
    :return: None
    """
    # empty tree
    t0 = BST()
    print('t0:', t0)
    print('t0 size (0):', t0.size)
    print('t0 contains 10 (False)?', t0.contains(10))
    print('t0 height (-1)?', t0.height())

    # single node tree
    t1 = BST()
    t1.insert(10)
    print('t1:', t1)
    print('t1 size (1):', t1.size)
    print('t1 contains 10 (True)?', t1.contains(10))
    print('t1 contains 0 (False)?', t1.contains(0))
    print('t1 height (0)?', t1.height())

    # tree with a parent (20), left child (10) and right child (30)
    t2 = BST()
    for val in (20, 10, 30): t2.insert(val)
    print('t2:', t2)
    print('t2 size (3):', t2.size)
    print('t2 contains 30 (True)?', t2.contains(30))
    print('t2 contains 0 (False)?', t2.contains(0))
    print('t2 height (1)?', t2.height())

    # a larger tree
    t3 = BST()
    for val in (17, 5, 35, 2, 16, 29, 38, 19, 33): t3.insert(val)
    print('t3:', t3)
    print('t3 size (9):', t3.size)
    print('t3 contains 16 (True)?', t3.contains(16))
    print('t3 contains 0 (False)?', t3.contains(0))
    print('t3 height (3)?', t3.height())

    print('----->', t3.pathSum(19 + 29))

    t4 = BST()
    for val in (23, 45, 3, 7, 234, 34): t4.insert(val)
    print('>>>>', t4.findPath([]))


if __name__ == '__main__':
    testBST()
