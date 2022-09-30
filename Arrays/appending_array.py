import array
data = array.array('i',[1,2,3,4,5,6])
print(data)
data.append(7)
print(data)
for i in range(11):
    data.append(i)
print(data)