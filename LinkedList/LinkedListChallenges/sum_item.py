class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# printing linkedlist iteratively
# def print_linked_list(head):
#     current = head
#     while current is not None:
#         print(current.value)
#         current = current.next


a.next = b
b.next = c
c.next = d

# iterative solution
def sum(head):
    current = head
    total = 0
    while current:
        total += current.value
        current = current.next
    return total

# recursive solution
def sum2(head):
    if head is None:
        return
    total = head.value + sum(head.next)
    return total

print("total is ",sum2(a))

