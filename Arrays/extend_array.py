data = [1,2,3,4,5,6,6]
print(data)
new_data = []
data.extend([9,8,7])
print(data)
for i in data:
    new_data.extend([[i,data.count(i)]])

print(new_data)