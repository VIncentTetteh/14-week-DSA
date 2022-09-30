# convert a text like ' my name is vince and my add is 25 ' into 234562789
text = 'My name is Vincent and my age is 28'
text_array = text.lower().split()
text_code = ''
for i in text_array:
    text_code += str(text_array.index(i))
print(text_array)
print(text_code)