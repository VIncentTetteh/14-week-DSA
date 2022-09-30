data = [1,9,8,4,5,6]
# data.sort(reverse=True)
# print(data)

def sort_function(e):
    return len(e)

data.sort(key=sort_function)
print(data)