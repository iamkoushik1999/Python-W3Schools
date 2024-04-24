# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# -----------------------------------------------------------------------------------------------------------
mySet1 = {'apple', 'banana', 'mango'}
mySet2 = {1, 2, 3}
mySet3 = mySet1.union(mySet2)
print(mySet3)
# =---------------------------------
mySet4 = mySet1 | mySet2
print(mySet4)
# =---------------------------------
newSet1 = {'apple', 'mango', 'kiwi'}
newSet2 = {10, 20, 30}
newSet3 = {'male', 'female'}
newSet4 = {True, False}
newSet5 = newSet1.union(newSet2, newSet3, newSet4)
print(newSet5)
# =---------------------------------
newSet6 = newSet1 | newSet2 | newSet3 | newSet4
print(newSet6)
# =---------------------------------
# Join Set and Tuple
mySet = {'a', 'b', 'c'}
myTuple = (1, 2, 3)
set_tuple = mySet.union(myTuple)
print(set_tuple)
# =---------------------------------
# The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
# As union will retuen in a new set
# Update doesnot return a new set it changes the original one

helloSet1 = {'apple', 'mango', 'kiwi'}
helloSet2 = {10, 20, 30}
helloSet1.update(helloSet2)
print(helloSet1)
# Both Union and Update removes duplicate items
