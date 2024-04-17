# The difference() method keeps the items from the first set that are not in the other set(s).
# -----------------------------------------------------------------------------------------------------------
# Difference
mySet1 = {"apple", "banana", "cherry"}
mySet2 = {"google", "microsoft", "apple"}
mySet3 = mySet1.difference(mySet2)
print(mySet3)
# =---------------------------------
mySet4 = mySet1 - mySet2
print(mySet4)
print('----------------------------------------------')
# Differenc Update
mySet1.difference_update(mySet2)
print(mySet1)
print('----------------------------------------------')
