class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

#printing linkedlist iteratively
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value)
        current = current.next


a.next = b
b.next = c
c.next = d

def reverse_linkedList(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

def print_linkedList(head):
    current = head
    while current:
        print(current.value)
        current = current.next

print(reverse_linkedList(a))
print_linked_list(a)