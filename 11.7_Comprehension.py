myList = ['apple', 'banana', 'kiwi', 'lemon', 'mango', 'orange']

print(myList)
print(len(myList))

newList = []

for x in myList:
    if 'a' in x:
        newList.append(x)

print(newList)
print(len(newList))
print('--------------------------------------------------')
# Comprehension
myList2 = ['apple', 'banana', 'kiwi', 'lemon', 'mango', 'orange']
print(myList2)
print(len(myList2))

newList2 = [x for x in myList2 if 'a' in x]
print(newList2)
print(len(newList2))
print('--------------------------------------------------')