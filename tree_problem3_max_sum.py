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

# Assumptions
# does not have to be a valid bst
# always has only numbers
# tree can have negative numbers

# PSEUDO BRAINSTORM
# init max sum to keep track of total
# init temp sum to explore all branches and determine if selected branch produces > 1
# if it does change temp sum to max sum

class BinaryTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def items_in_order(self):
        items = []
        self.traverse_in_order_recursive(self.root, items.append)
        return items

    def traverse_in_order_recursive(self, node, visit, max_sum = 0, tmp_sum = 0):
        max_path = []
        if node.left:
            max_sum += node.left.data
            self.traverse_in_order_recursive(node.left, visit)
        visit(node.data)
        max_sum += node.data
        if node.right:
            max_sum += node.right.data
            self.traverse_in_order_recursive(node.right, visit)
        print(max_sum)

    # def max_sum(self, max = 0, tmp = 0):


if __name__ == "__main__":
    bst = BinaryTree()

    # Example 1 - Simple
    bst.root = BinaryTreeNode(1)

    level_1l = BinaryTreeNode(2)
    bst.root.left = level_1l
    level_1r = BinaryTreeNode(3)
    bst.root.right = level_1r

    # level_2ll = BinaryTreeNode(1)
    # level_1l.left = level_2ll
    # level_2lr = BinaryTreeNode(3)
    # level_1l.right = level_2lr

    # level_2rl = BinaryTreeNode(6)
    # level_1r.left = level_2rl
    # level_2rr = BinaryTreeNode(9)
    # level_1r.right = level_2rr

    print(bst.items_in_order())