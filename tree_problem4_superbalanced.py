# Let’s say a binary tree is "superbalanced" if the difference between the depths of any two leaf nodes 
# is at most one. Write a function to check if a binary tree is "superbalanced".

# Assumptions

# Superbalanced looks something like this with 2 leaves and an accompanying parent node
#      O
#    /   \
#   O     O
#  / \   / \
# O   O O   O           

# Not Superbalanced because the right parent doesn't have a leaf reachable within 1 depth
#      O
#    /   \
#   O     O
#  / \   / 
# O   O O   

# Not Superbalanced because the right leaf can't reach any other leaves with 1 depth traversal
#      O
#    /   \
#   O     O
#  / \    
# O   O   

# PSEUDO BRAINSTORM
