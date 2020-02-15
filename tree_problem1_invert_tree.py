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

# 