# Given a linked list, rearrange the elements by interleaving the first half of the linked list with the second half.
# Example: If the given linked list is A → B → C → D → E → F → G → H, nodes should be rearranged so the list becomes A → C → E → G → B → D → F → H.

# Edge cases
# LL len 0 or 1
# If LL len 2 do I just reverse it?
# 

# Simplifications
# len 4
# has a size + prev property

# PSEUDO BRAINSTORM
# Keep track of 2previous, initiated to head of LL
# Keep track of previous
# at 3rd node set previous.next to node.next
# set 2previous.next to node