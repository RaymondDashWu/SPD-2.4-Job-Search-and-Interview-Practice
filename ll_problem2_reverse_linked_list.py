# Given a singly-linked list, reverse the order of the list by modifying the nodes’ links.

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
    # PSEUDO BRAINSTORM
    # keep track of a prev, cur, next pointer
    # when prev is not none set cur.next to prev, cur to nxt, and nxt to nxt.next
    # break when cur is none 

    def reverse(self):
        prev = None
        curr = self.head
        nxt = curr.next

        while curr is not None:
            curr.next = prev
            prev = curr
            curr = nxt
            try:
                nxt = nxt.next
            except:
                break
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(curr, prev):
            if curr is None:
                return prev

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            return _reverse_recursive(curr, prev)
        self.head = _reverse_recursive(self.head, None)


if __name__ == "__main__":
    ll = LinkedList()

    ll.head = Node("A")
    
    second = Node("B")
    ll.head.next = second
    
    third = Node("C")
    second.next = third

    fourth = Node("D")
    third.next = fourth

    # ll.reverse()
    ll.reverse_recursive()
    print(ll.print_ll())
    print("Head of LL", ll.head.data)