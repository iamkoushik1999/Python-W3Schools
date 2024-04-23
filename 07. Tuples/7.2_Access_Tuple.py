# Access a Tuple
# Tuples are indexed
myTuple1 = ('apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange')
print(myTuple1)
print(myTuple1[1])
# Negative Index
# -1 means last item
print(myTuple1[-1])
# Range
print(myTuple1[2:5])
print(myTuple1[:4])
print(myTuple1[2:])
# Nehative Range
print(myTuple1[-4:-1])
# Check if Item exists
if 'apple' in myTuple1:
    print('Apple is there')
