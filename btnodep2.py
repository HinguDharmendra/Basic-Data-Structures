"""
CSCI-603: Trees (week 10)
Author: Sean Strout @ RIT CS

This is an implementation of a binary tree node.
"""

"Name: Dharmendra Hingu Exam 2"


class BTNode:
    """
    A binary tree node contains:
     :slot val: A user defined value
     :slot left: A left child (BTNode or None)
     :slot right: A right child (BTNode or None)
    """
    __slots__ = 'val', 'left', 'right'

    def __init__(self, val, left=None, right=None):
        """
        Initialize a node.
        :param val: The value to store in the node
        :param left: The left child (BTNode or None)
        :param right: The right child (BTNode or None)
        :return: None
        """
        self.val = val
        self.left = left
        self.right = right


def isBST(node):
    if node.left is not None:           # if the left child is not None
        if node.left.val < node.val:    # if the value at the left child is smaller than the root
            isBST(node.left)
            return True
        else:
            return False                # BST property is violated, this BTNode can't represent BST root
    elif node.right is not None:        # if the right child is not None
        if node.right.val > node.val:   # if the value at the right child is larger than the root
            isBST(node.right)
            return True
        else:
            return False                # BST property is violated, this BTNode can't represent BST root


def testBTNode():
    """
    A test function for BTNode.
    :return: None
    """
    left = BTNode(10)
    right = BTNode(20)
    parent = BTNode(30)
    parent.left = left
    parent.right = right
    print('parent (30):', parent.val)
    print('left (10):', parent.left.val)
    print('right (20):', parent.right.val)
    print(isBST(parent))

    bt = BTNode(45, None, BTNode(78, None, BTNode(90)))
    print(isBST(bt))

    bt = BTNode(45, BTNode(78, None, BTNode(90)))
    print(isBST(bt))


if __name__ == '__main__':
    testBTNode()
