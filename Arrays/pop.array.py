import array
data = array.array('i',[1,2,3])
print(data)
pop_data = 0

for idx, value in enumerate(data):
    if value % 2 == 0:
        pop_data = data.pop(idx)

print(pop_data)
print(data)

