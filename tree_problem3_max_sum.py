# Given a binary tree containing numbers, find the maximum sum path (the path that has the largest sum of node values). The path may start and end at any node in the tree.

# Sample trees from https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/

# Simple
# Input: Root of below tree
#        1
#       / \
#      2   3
# Output: 6

# Has to temporarily visit negative number to see if there's anything good
# Input: Root of below tree
#        10
#       /  \
#      2    10
#     / \   / \
#    20  1 1  -1
#            /  \
#           3   100
# Output: 141

# Root is negative
# Input: Root of below tree
#       -100
#       /  \
#      2    10
#     / \   / \
#    20  1 1  -1
#            /  \
#           3   100
# Output: 110

# Assumptions
# does not have to be a valid bst
# always has only numbers
# tree can have negative numbers

# PSEUDO BRAINSTORM
# init max sum to keep track of total
# init temp sum to explore all branches and determine if selected branch produces > 1
# if it does change temp sum to max sum

# traversal would involve checking to see if there's a left and right node
# if theres no more children check to see if left or right side is bigger NOTE simple for now. Greater number could lie 1 level deeper
# add numbers to max_sum

# if traversal comes across negative number do a full traversal to see temp_sum

import math

class BinaryTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def helper_path_sum(self, node):
        """Recursively traverses left + right nodes until leaves are reached. Then recursively finds
        best path to take from the bottom up"""
        if node == None: # When leaf is reached
            return 0
        left = max(0, self.helper_path_sum(node.left)) # traverses left node until leaf is reached
        right = max(0, self.helper_path_sum(node.right)) # traverses right node until leaf is reached
        # Once this line is reached go up call stack and sum up the best branch
        self.max_sum = max(self.max_sum, left + right + node.data)
        return max(left,right) + node.data # function scope variable used to keep track of temp max


    def max_path_sum(self, root):
        self.max_sum = -math.inf # class scope variable that will be used to keep track of global max
        self.helper_path_sum(root)
        return self.max_sum

if __name__ == "__main__":
    bst = BinaryTree()

    # # Example 1 - Simple
    # bst.root = BinaryTreeNode(1)

    # level_1l = BinaryTreeNode(2)
    # bst.root.left = level_1l
    # level_1r = BinaryTreeNode(3)
    # bst.root.right = level_1r

    # # Example 2 - Has to temporarily visit negative number to see if there's anything good
    # bst.root = BinaryTreeNode(10)

    # level_1l = BinaryTreeNode(2)
    # bst.root.left = level_1l
    # level_1r = BinaryTreeNode(10)
    # bst.root.right = level_1r

    # level_2ll = BinaryTreeNode(20)
    # level_1l.left = level_2ll
    # level_2lr = BinaryTreeNode(1)
    # level_1l.right = level_2lr

    # level_2rl = BinaryTreeNode(1)
    # level_1r.left = level_2rl
    # level_2rr = BinaryTreeNode(-1)
    # level_1r.right = level_2rr

    # level_3rrl = BinaryTreeNode(3)
    # level_2rr.left = level_3rrl
    # level_3rrr = BinaryTreeNode(100)
    # level_2rr.right = level_3rrr

    # Example 3 - Root is negative
    bst.root = BinaryTreeNode(-100)

    level_1l = BinaryTreeNode(2)
    bst.root.left = level_1l
    level_1r = BinaryTreeNode(10)
    bst.root.right = level_1r

    level_2ll = BinaryTreeNode(20)
    level_1l.left = level_2ll
    level_2lr = BinaryTreeNode(1)
    level_1l.right = level_2lr

    level_2rl = BinaryTreeNode(1)
    level_1r.left = level_2rl
    level_2rr = BinaryTreeNode(-1)
    level_1r.right = level_2rr

    level_3rrl = BinaryTreeNode(3)
    level_2rr.left = level_3rrl
    level_3rrr = BinaryTreeNode(100)
    level_2rr.right = level_3rrr

    print(bst.max_path_sum(bst.root))