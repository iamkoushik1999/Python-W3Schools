mySet1 = {'apple', 'banana', 'cherry'}
print(mySet1)
print(len(mySet1))
# Set is unordered so when print it will not show how you wrote it
# Set is unchangeable meaning items cannot be changed but items can be added or removed
# Set does not allow duplicate items

mySet2 = {'apple', 'banana', 'cherry', 'apple'}
print(mySet2)
print(len(mySet2))
# It will show duplicate items once

mySet3 = {'apple', 'banana', True, 1, 2}
print(mySet3)
print(len(mySet3))
# True and 1 considered as same value so only True is showing
mySet4 = {'apple', 'banana', True, False, 0}
print(mySet4)
print(len(mySet4))
# False and 0 considered as same value so only False is showing

# Data Types
mySetString = {'apple', 'banana', 'cherry'}
mySetInt = {1, 2, 3}
mySetBool = {True, False, True}
print(mySetString)
print(mySetInt)
print(mySetBool)

# Different Data Types
mySetAll = {'Apple', 'Banana', 10, 12, True, False}
print(mySetAll)
print(type(mySetAll))

# Type Constructor
mySet = set(('Apple', 'Banana', 'Cherry'))
print(mySet)
