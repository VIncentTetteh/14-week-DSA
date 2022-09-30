def find_pair_sum(arr,sum):
    if arr is None or len(arr) == 0:
        raise ValueError("arr cant be empty")

    for first_value in arr:
        for second_value in arr:
            if first_value + second_value == sum:
                return True
    return False

arr = [11,15,26,38,9,10]
print(find_pair_sum(arr,35))