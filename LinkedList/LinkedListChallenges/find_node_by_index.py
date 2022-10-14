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

def find_by_index(head,index):
    if head is None:
        return
    count = 0
    current = head
    while current:
        if count == index:
            return current.value
        count += 1
        current = current.next


#recursive solution
def find_by_index2(head,index):
    if head is None:
        return
    if index == 0:
        return head.value
    return find_by_index2(head.next,index - 1)



print(find_by_index2(a,1))

