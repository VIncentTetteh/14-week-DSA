import array
data = array.array('i',[1,2,3,4,5,6])
print(data)
# data.remove(2)
# print(data)
for idx in range(len(data)+1):
    if idx in data:
        print(data[idx])
        data.remove(idx)

print(data)