class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

# printing linkedlist iteratively
# def print_linked_list(head):
#     current = head
#     while current is not None:
#         print(current.value)
#         current = current.next


a.next = b
b.next = c
c.next = d

# print_linked_list(a)
