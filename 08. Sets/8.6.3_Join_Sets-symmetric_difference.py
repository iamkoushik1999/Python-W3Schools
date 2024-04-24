# The symmetric_difference() method keeps all items EXCEPT the duplicates.
# -----------------------------------------------------------------------------------------------------------
# Symmetric Difference
mySet1 = {"apple", "banana", "cherry"}
mySet2 = {"google", "microsoft", "apple"}
mySet3 = mySet1.symmetric_difference(mySet2)
print(mySet3)
mySet4 = mySet1 ^ mySet2
print(mySet4)
print('----------------------------------------------')
# Symmetric Difference Update
mySet1.symmetric_difference_update(mySet2)
print(mySet1)
