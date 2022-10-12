class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def print(self):
        if self.head is None:
            print("liskedlist is empty")
        itr = self.head
        while itr:
            print(itr.data,end=" ")
            prev = itr.next -1

ll = LinkedList()
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.insert(6)
ll.print()