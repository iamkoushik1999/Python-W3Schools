# Join List
myList1 = ['apple', 'banana']
myList2 = ['Kiwi', 'Mango', 'Orange']
myList3 = myList1 + myList2
print(myList3)
print('--------------------------------------')
# Loop
numList1 = [1, 2, 3, 4, 5]
numList2 = [6, 7, 8, 9, 0]

for x in numList2:
    numList1.append(x)

print(numList1)
print('--------------------------------------')
# Extend
alphaList1 = ['a', 'b', 'c']
alphaList2 = ['d', 'e', 'f']

alphaList1.extend(alphaList2)

print(alphaList1)
