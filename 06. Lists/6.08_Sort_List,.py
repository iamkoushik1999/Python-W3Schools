# Sort List Alphanumerically
myList1 = ['orange', 'apple', 'mango', 'banana', 'kiwi']
myList1.sort()
print(myList1)
print('-----------------------------------------------------')
# Sort the list numerically:
myList2 = [4, 9, 6, 8, 5, 1, 3, 7, 2]
myList2.sort()
print(myList2)
print('-----------------------------------------------------')
# Descending Order
myList1.sort(reverse=True)
print(myList1)
myList2.sort(reverse=True)
print(myList2)
print('-----------------------------------------------------')
# Sort the list based on how close the number is to 50:
def myfunc(n):
    return abs(n - 50)


myList = [100, 50, 65, 82, 23]
myList.sort(key=myfunc)
print(myList)
print('-----------------------------------------------------')
# Case Sensetive Sort
myList3 = ['apple', 'Banana', 'kiwi', 'Orange', 'mango']
myList3.sort()
print(myList3)
myList3.sort(key=str.lower)
print(myList3)
print('-----------------------------------------------------')
# Reverse
myList4 = ['apple', 'Banana', 'kiwi', 'Orange', 'mango']
myList4.reverse()
print(myList4)


