# Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions.
"""
Input: 
arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
Output: 3 4 5 6 7 1 2
"""

# def rotate_array(arr,positions):
#     slice_arr = arr[0:positions]
#     poped_value = 0
#     count = 0
#     for idx,value in enumerate(arr):
#         while count < len(slice_arr):
#             if value in slice_arr:
#                 poped_value = arr.pop(idx)
#                 arr.append(poped_value)
#                 count += 1

#     return arr

# def rotate_array2(arr,position):
#     slice_arr = arr[0:position]
#     count = 0
#     while count < len(slice_arr):
#         arr.remove(slice_arr[count])
#         count +=1
#     arr.extend(slice_arr)
#     return arr


# print(rotate_array2(arr,4))
def rotate_array3(arr,position):
    first_new_arr = arr[0:position]
    second_new_arr = arr[position:]
    rotated_arr = second_new_arr + first_new_arr
    return rotated_arr

arr = [1,2,3,4,5,6,7]
print(rotate_array3(arr,5))




