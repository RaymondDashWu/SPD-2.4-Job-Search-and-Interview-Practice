# Given an array of k linked lists, each of whose items are in sorted order, combine all nodes (do not create new nodes) into a single linked list with all items in order.

# LL1 1 → 4 → 10
# LL2 5 → 8 → 11

# Expected 1 → 4 → 5 → 8 → 10 → 11

# PSEUDO BRAINSTORM
# have 3 sets of pointers per ll (total 6)
# 1 pointer for prev, curr, next
# compare curr pointers and use prev pointers to change next

# NOTE TODO Unfinished

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

    def compare_nodes(self, node):
        pass

    def sort_ll(self, ll2):
        ll1_prev = None
        ll2_prev = None
        ll1_curr = self.head
        ll2_curr = ll2.head
        ll1_next = ll1_curr.next
        ll2_next = ll2_curr.next


# LL1 1 → 4 → 10
# LL2 5 → 8 → 11

        # while neither are none
        while (ll1_curr, ll2_curr) is not None:
            ll2_prev = ll2_curr
            ll1_prev = ll1_curr
            # moving comparison section
            while ll1_curr.data > ll2_curr.data:
                ll2_curr = ll2_curr.next
                ll2_next = ll2_next.next
                if ll1_curr.data > ll2_curr.data:
                    ll2_curr.next = ll1_prev
            while ll2_curr.data > ll1_curr.data:
                ll1_curr = ll1_curr.next
                ll1_next = ll1_next.next
                if ll2_curr.data > ll1_curr.data:
                    ll1_curr.next = ll2_prev
            # changing pointer section

        # compare curr pointers
        # change pointers with prev
        # ll that is higher gets moved up one

if __name__ == "__main__":
    ll = LinkedList()

    ll.head = Node(1)
    
    second = Node(4)
    ll.head.next = second
    
    third = Node(10)
    second.next = third

    ll2 = LinkedList()

    ll2.head = Node(5)

    fourth = Node(8)
    ll2.head.next = fourth

    fifth = Node(11)
    fourth.next = fifth
    
    ll.sort_ll(ll2)
    print("ll", ll.print_ll())
    print("Head of LL", ll.head.data)