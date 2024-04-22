# Apend item in list
fruitList = ["apple", "orange", "kiwi"]
fruitList.append('orange')

print(fruitList)
print('-----------------------------------------------')
# insert item in list
sportList = ['football', 'cricket', 'hoockey']
sportList.insert(2, 'rugby')

print(sportList)
print('-----------------------------------------------')
# Extend List
phoneList = ['apple', 'samsung', 'google']
addPhone = ['oneplus', 'xiaomi', 'realme']
phoneList.extend(addPhone)
print(phoneList)
print('-----------------------------------------------')
# Add Iterables
myList = ['amazone', 'flipkart', 'myntra']
myTuple = ('ajio', 'meesho')
myList.extend(myTuple)
print(myList)

