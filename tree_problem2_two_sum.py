# Given a binary search tree containing integers and a target integer, 
# come up with an efficient way to locate two nodes in the tree whose sum is 
# equal to the target value.

# ASSUMPTIONS
# Valid BST
# BST is not empty
# access to data, left, right, root

# PSEUDO BRAINSTORM
# initialize set that will contain complements
# in order traversal. NOTE I don't think what traversal I pick matters after thinking about it?
# target - node.data added to set
# while traversing nodes if node.data in set return node.data, target - node.data

from collections import deque

class BinaryTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def two_sum_pre_order_recursive(self, node, target, complements = set()):
        if len(complements) == 0: # initialize by adding root complement
            complements.add(target - node.data)
        if node.left:
            if node.left.data in complements:
                return [(target - node.left.data), node.left.data]
            else:
                complements.add(target - node.left.data)
            left_ret = self.two_sum_pre_order_recursive(node.left, target, complements)
            if left_ret is not None: # Conditional return for if both numbers on left side
                return left_ret
        if node.right:
            if node.right.data in complements:
                return [(target - node.right.data), node.right.data]
            else:
                complements.add(target - node.right.data)
            right_ret = self.two_sum_pre_order_recursive(node.right, target, complements)
            if right_ret is not None: # Conditional return for if both numbers on right side
                return right_ret

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

    print(bst.two_sum_pre_order_recursive(node = bst.root, target = 10))
    # print(bst.two_sum_pre_order_recursive(node = bst.root, target = 11))
    # print(bst.two_sum_pre_order_recursive(node = bst.root, target = 80))
    # print(bst.two_sum_pre_order_recursive(node = bst.root, target = 4))
    # print(bst.two_sum_pre_order_recursive(node = bst.root, target = 12))