# Rotate a given linked list counter-clockwise by k nodes, where k is a given integer.
# Example: If the given linked list is A → B → C → D → E → F and k is 4, nodes should be modified so the list becomes E → F → A → B → C → D.
# Assumptions: k is positive and smaller than n, the length of the linked list.

# Questions
# is counter clockwise the same as reversing it?
# head/tail/prev node?
# Space constraints?
# k > length of LL

# Assumptions
# data is valid
# len > 0
# time constraing O(n)

# Simplifications
# length of LL is known
# LL size 3, k is 1

# PSEUDO BRAINSTORM 1
# iterate through nodes + have a previous
# set previous.next to node.next

# PSEUDO BRAINSTORM 2
# put all data into an array
# iterate through the array at [::-1] and create a new linked list