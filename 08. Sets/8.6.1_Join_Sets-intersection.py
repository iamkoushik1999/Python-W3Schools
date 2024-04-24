# The intersection() method keeps ONLY the duplicates.
# =---------------------------------
# Intersection
duSet1 = {'apple', 'mango', 'kiwi'}
duSet2 = {'apple', 'cherry', 'orange'}

duSet3 = duSet1.intersection(duSet2)
print(duSet3)

duSet4 = duSet1 & duSet2
print(duSet4)
