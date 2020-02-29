# Given a binary search tree, reverse the order of its values by modifying the nodes’ links.

# Example from https://leetcode.com/problems/invert-binary-tree/
# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Edge cases
# what if only 1 child?

# Simplifications
# 3 nodes
# 

# PSEUDO BRAINSTORM
# level order traversal
# if node has children, left becomes right and right becomes left

from collections import deque

class BinaryTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def print_level_order(self):
        items = []
        # assumes binary tree never empty
        self.traverse_level_order(self.root, items.append)
        for node in items:
            print(node.data)

    def traverse_level_order(self, start, visited):
        queue = deque()
        queue.append(start)

        while len(queue) > 0:
            node = queue.popleft()
            visited(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return queue

    def invert(self, root):
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.root = BinaryTreeNode(4)

    level_1l = BinaryTreeNode(2)
    bst.root.left = level_1l
    level_1r = BinaryTreeNode(7)
    bst.root.right = level_1r

    level_2ll = BinaryTreeNode(1)
    level_1l.left = level_2ll
    level_2lr = BinaryTreeNode(3)
    level_1l.right = level_2lr

    level_2rl = BinaryTreeNode(6)
    level_1r.left = level_2rl
    level_2rr = BinaryTreeNode(9)
    level_1r.right = level_2rr

    bst.invert(bst.root)
    # print(bst.root.right.data)
    print(bst.print_level_order())
