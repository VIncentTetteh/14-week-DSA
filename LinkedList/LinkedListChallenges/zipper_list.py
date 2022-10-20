
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

def zipper(head_1,head_2):
    tail = head_1
    current_1 = head_1.next
    current_2 = head_2
    count = 0
    while current_1 is not None and current_2 is not None:
        if count % 2 == 0:
            tail.next = current_2
            current_2 = current_2.next
        else:
            tail.next = current_1
            current_1 = current_1.next
        tail = tail.next
        count += 1

    if current_1 is not None:
        tail.next = current_1
    if current_2 is not None:
        tail.next = current_2

    return head_1

