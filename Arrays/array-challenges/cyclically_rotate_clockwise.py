
def cyclical_array_rotate(arr):
    slice_by_one = arr[-1]
    sliced_arr = arr[0:-1]
    sliced_arr.insert(0,slice_by_one)
    return sliced_arr

arr = [i for i in range(11)]
print(cyclical_array_rotate(arr))