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
# A -> B -> C , k = 1
# keep track of number of node traversals
# keep track of original_head

# when node.next is none change modified head to point to k + 1 node
# tail points to original head
# change modified head to self.head

# PSEUDO BRAINSTORM 2
# put all data into an array
# iterate through the array at [::-1] and create a new linked list

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.head = None

    def print_ll(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def rotate_counter_clockwise(self, k):
        traversal_counter = 0
        original_head = self.head
        node = self.head

        # traverses up until k and splits it into 2 linked lists in memory. One starting with 
        # modified head & original head
        # ex: A → B → C → D → E → F, k = 4
        # modified head E → F
        # original head A → B → C → D
        while node is not None:
            if traversal_counter == k:
                modified_head = node
                break

            prev = node
            node = node.next
            traversal_counter += 1

        # splits into 2 LL and then sets the end point of the original_head
        prev.next = None

        # continued traversal through modified_head LL
        while node is not None:
            prev = node
            node = node.next
        prev.next = original_head
        self.head = modified_head
        

if __name__ == "__main__":
    ll = LinkedList()

    ll.head = Node("A")
    
    second = Node("B")
    ll.head.next = second
    
    third = Node("C")
    second.next = third

    fourth = Node("D")
    third.next = fourth

    fifth = Node("E")
    fourth.next = fifth

    sixth = Node("F")
    fifth.next = sixth
    
    ll.rotate_counter_clockwise(4)
    print(ll.print_ll())
    print("Head of LL", ll.head.data)