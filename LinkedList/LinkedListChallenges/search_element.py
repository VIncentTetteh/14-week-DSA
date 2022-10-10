def search(node,value):
    itr = node
    while itr:
        if value == itr.data:
            return True
        itr = itr.next
    return False
