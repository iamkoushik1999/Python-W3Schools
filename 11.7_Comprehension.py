# Select those which has 'a' in them
myList = ['apple', 'banana', 'kiwi', 'lemon', 'mango', 'orange']
print(myList)

newList = []
for x in myList:
    if 'a' in x:
        newList.append(x)

print(newList)
print('--------------------------------------------------')
# Select those which has 'a' in them
# Comprehension
myList2 = ['apple', 'banana', 'kiwi', 'lemon', 'mango', 'orange']
newList2 = [x for x in myList2 if 'a' in x]
print(newList2)
print('--------------------------------------------------')
# Show without 'apple'
myList3 = ['apple', 'banana', 'kiwi', 'lemon', 'mango', 'orange']
newList3 = [x for x in myList3 if x != 'apple']
print(newList3)
print('--------------------------------------------------')
# Show All
newList4 = [x for x in myList3]
print(newList4)
print('--------------------------------------------------')
# Show 1st 10 numbers
newList5 = [x for x in range(10)]
print(newList5)
print('--------------------------------------------------')
# Accept only numbers lower than 5:
newList6 = [x for x in range(10) if x < 5]
print(newList6)
print('--------------------------------------------------')
# Set the values in the new list to upper case:
newList7 = [x.upper() for x in myList3]
print(newList7)
print('--------------------------------------------------')
# Set all values in the new list to 'hello':
newList8 = ['hello' for x in myList3]
print(newList8)
print('--------------------------------------------------')
# Return 'orange' instead of 'banana':
newList9 = [x if x != 'banana' else 'orange' for x in myList3]
print(newList9)
print('--------------------------------------------------')
