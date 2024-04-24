# Remove Set Items
# Remove Method
mySet1 = {'apple', 'banana', 'cherry'}
mySet1.remove('apple')
print(mySet1)
print('------------------------------------')
# Discard Method
mySet2 = {'apple', 'banana', 'cherry'}
mySet2.discard('banana')
print(mySet2)
print('------------------------------------')
# Pop Method
# Sets are unordered so pop removes random item
mySet3 = {'apple', 'banana', 'cherry'}
x = mySet3.pop()
print(x)
print(mySet3)
print('------------------------------------')
# Clear Method
mySet4 = {'apple', 'banana', 'cherry'}
mySet4.clear()
print(mySet4)
# Delete/del Method
mySet5 = {'apple', 'banana', 'cherry'}
del mySet5
