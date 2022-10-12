
# iterative solution
# def print_linked_list_values(head):
#     values = []
#     current = head
#     while current is not None:
#         values.append(current.value)
#         current = current.next

#     return values

# recursive solution
# def print_linked_list_values(head):
#     values = []
#     if head is None:
#         return
#     values.append(head.value)
#     print_linked_list_values(head.next)
#     return values

# optimize recursive solution
def print_linked_list_values(head):
    values = []
    fill_values(head,values)
    return values

def fill_values(head,values):
    if head is None:
        return
    values.append(head.value)
    fill_values(head.next,values)

