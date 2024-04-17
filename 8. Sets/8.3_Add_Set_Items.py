# Add Set Items
# Once a set is created you cannot change it's items but can add items
mySet1 = {'apple', 'banana', 'cherry'}
mySet1.add('orange')
print(mySet1)
print('----------------------------------')
# TO Add one set to another, Use update method
mySetAdd1 = {'apple', 'banana'}
mySetAdd2 = {'mango', 'kiwi'}
mySetAdd1.update(mySetAdd2)
print(mySetAdd1)
print('----------------------------------')
# Add Any Iterables
mySet = {'apple', 'banana'}
myList = ['Cherry', 'Pinapple']
mySet.update(myList)
print(mySet)
