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

# Iterative solution
def find_item(head,value_to_find):
    current = head
    while current:
        if current.value == value_to_find:
            return True
        current = current.next
    return False

#recursive solution
def find_item2(head,value_to_find):
    if head is None:
        return False
    if value_to_find == head.value:
        return True
    return find_item2(head.next,value_to_find)

print(find_item2(a,3))