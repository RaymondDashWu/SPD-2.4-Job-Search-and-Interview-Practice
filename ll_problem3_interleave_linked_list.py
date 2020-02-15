# Given a linked list, rearrange the elements by interleaving the first half of the linked list with the second half.
# Example: If the given linked list is A → B → C → D → E → F → G → H, nodes should be rearranged so the list becomes A → C → E → G → B → D → F → H.

# Edge cases
# LL len 0 or 1
# If LL len 2 do I just reverse it?
# 

# Simplifications
# len 4
# has a size + prev property

# NOTE Does not work with a list larger than 4
# PSEUDO BRAINSTORM
# Keep track of 2previous, initiated to head of LL
# Keep track of previous
# at 3rd node set previous.next to node.next
# set 2previous.next to node

# PSEUDO BRAINSTORM 2
# Split the LL into 2 with one at even nodes and another at odd nodes
# ie 0 -> 2 -> 4 evens 1 -> 3 -> 5 odds
# merge both LL evens then odds 

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

    def interleave(self):
        """splits the LL into two called evens/odds. Not numerical but by index-ish 
        (LL don't have indexes per se)
        Ex: A -> B -> C -> D
        Evens splits to A -> C
        Odds splits to B -> D"""
        # keep track of 2 heads for merging later
        evens = self.head
        even_head = evens
        
        odds = evens.next
        odd_head = odds

        while self.head is not None:
            try: # Eventually will get out of bounds 
                # Section to keep track of where to link
                prev_evens = evens
                prev_odds = odds

                # Jump 2 section A -> C ... B -> D
                evens = evens.next.next
                prev_evens.next = evens
                odds = odds.next.next
                prev_odds.next = odds
            except:
                break


        self.merge(even_head, odd_head)

    def merge(self, evens, odds):
        """Takes 2 LL and joins them together"""
        while evens is not None:
            self = evens
            evens = evens.next # Keep traversing evens until end
        self.next = odds # Then just have that pointer point to the odd LL

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

    seventh = Node("G")
    sixth.next = seventh

    eight = Node("H")
    seventh.next = eight
    
    ll.interleave()
    print(ll.print_ll())
    print("Head of LL", ll.head.data)