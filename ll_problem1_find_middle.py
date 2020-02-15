# Given a singly-linked list, find the middle item in the list.
# Example: If the given linked list is A → B → C → D → E, return C.
# Assumptions: The length (n) is odd so the linked list has a definite middle.


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList(object):

    def __init__(self):
        self.head = None

    def find_length(self):
        node = self.head
        ll_len = 0

        while node is not None:
            ll_len += 1
            node = node.next
        return ll_len

    def find_middle(self):
        node = self.head
        ll_len = self.find_length()

        # Assumption is that if the length of LL is even then there are 2 middles. They can't always be
        # combined so I'll try to else return them both
        if ll_len % 2 == 0:
            counter = 0
            middle = ll_len - 2
            while counter != middle:
                counter += 1
                if counter == middle:
                    try:
                        return "The middle is {}".format((node.data + node.next.data)/2)
                    except:
                        return "There are 2 middles {} & {}".format(node.data, node.next.data) 
                node = node.next
        else:
            counter = 0
            middle = ll_len - 1
            while counter != middle:
                counter += 1
                if counter == middle:
                    return "The middle is {}".format(node.data)
                node = node.next
                


if __name__ == "__main__":
    ll = LinkedList()

    ll.head = Node("A")
    
    second = Node("B")
    ll.head.next = second
    
    third = Node("C")
    second.next = third

    fourth = Node("D")
    third.next = fourth

    print(ll.find_middle())
