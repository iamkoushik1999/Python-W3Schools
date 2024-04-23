# Tuple is unchangeable
# But Tuple can be converted into List
# And List is changeable
# Convert Tuple to list, Update list then convert back to Tuple
myTuple1 = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango')
print("1st Tuple -> ")
print(myTuple1)
myList1 = list(myTuple1)
print("Coverted List -> ")
print(myList1)
myList1[1] = 'pinapple'
print("Updated List -> ")
print(myList1)
myTuple1 = tuple(myList1)
print('Converted Tuple -> ')
print(myTuple1)
print('-----------------------------------------------------------')
# Add Item
myTuple2 = ('apple', 'banana', 'cherry')
print('Tuple -> ')
print(myTuple2)
mylist2 = list(myTuple2)
print("Converted List -> ")
print(mylist2)
mylist2.append('kiwi')
myTuple2 = tuple(mylist2)
print('Updated and Converted to Tuple -> ')
print(myTuple2)
print('-----------------------------------------------------------')
# A new Tuple can be added to another Tuple
myTuple3 = ('x', 'y', 'z')
print('Tuple -> ')
print(myTuple3)
newTuple1 = ('a', 'b')
myTuple3 += newTuple1
print('Added another Tuple -> ')
print(myTuple3)
print('-----------------------------------------------------------')
# Item cannot be removed from a Tuple
# Convert Tuple to List
# Remove from list then conbert to Tuple again
myTuple4 = ('apple', 'banana', 'cherry')
myList4 = list(myTuple4)
myList4.remove('apple')
myTuple4 = tuple(myList4)
print(myTuple4)
print('-----------------------------------------------------------')
# Delete Tuple
# myTuple5 = (1, 2, 3, 4, 5)
# del myTuple5
# print(myTuple5)
# myTuple5 will show error as 'not defined' it is deleted already
