class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self,index):
        if index < 0 or index > self.get_lenght():
            raise Exception("index out of bounds")

        if index == 0:
            self.head = self.head.next
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print("Linked list is empty")
        itr = self.head
        while itr:
            print(itr.data,end=" -> ")
            itr = itr.next

    
                

ll = LinkedList()
# ll.insert_at_start(5)
# ll.insert_at_start(4)
# ll.insert_at_end(10)
arr = [1,2,3]
ll.insert_values(arr)
print(ll.get_lenght())
ll.remove_at(0)
ll.print()
