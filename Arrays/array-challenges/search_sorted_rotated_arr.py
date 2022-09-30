# constant time O(n)
def search_array(arr,key):
    if not arr[key]:
        raise IndexError
    return arr[key]



# log time O(logN)
def binary_search(arr,key):
    start = 0
    end = len(arr) - 1
    mid_index = 0
    while start <= end:
        mid_index = (start + end) // 2
        mid_number = arr[mid_index]
        if mid_index == key:
            return mid_number
        elif mid_index > key:
            end = mid_index -1
        else:
            start = mid_index + 1

arr = [a for a in range(10,21)]
print(arr)

print(search_array(arr,0))

print(binary_search(arr,0))


