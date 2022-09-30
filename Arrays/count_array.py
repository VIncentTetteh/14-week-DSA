data = [1,2,5,4,7,8,8,8,4]
print(data.count(2))
counter = {}
for i in data:
    counter[i] = data.count(i)

print(counter)