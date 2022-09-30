data = [1,2,3,4,5]
new_data = data.copy()
print(data)
print(new_data)
data.append(6)
result = []
# print(data)
# print(new_data)
for item in data:
    for item2 in new_data:
        if item + item2 == 7:
            result.extend([item,item2])

print(result)

