# Remove Specified Item
fruitList1 = ['apple', 'banana', 'mango']
fruitList1.remove('banana')
print(fruitList1)
print('-----------------------------------------------')
# Remove Specified Item but the 1st one
fruitList2 = ['apple', 'banana', 'mango', 'banana', 'orange', 'kiwi']
fruitList2.remove('banana')
print(fruitList2)
print('-----------------------------------------------')
# Remove Specified Index
sportList1 = ['football', 'cricket', 'rugby']
sportList1.pop(1)
print(sportList1)
print('-----------------------------------------------')
# Remove last index
sportList2 = ['football', 'cricket', 'rugby']
sportList2.pop()
print(sportList2)
print('-----------------------------------------------')
# Remove first index
sportList3 = ['football', 'cricket', 'rugby']
del sportList3[0]
print(sportList3)
print('-----------------------------------------------')
# Remove Entire List
sportList4 = ['football', 'cricket', 'rugby']
del sportList4
print('Deleted')
print('-----------------------------------------------')
# Remove first index
sportList5 = ['football', 'cricket', 'rugby']
sportList5.clear()
print(sportList5)
