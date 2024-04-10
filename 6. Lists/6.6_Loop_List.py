# For in
list1 = ['apple', 'banana', 'kiwi']

for x in list1:
    print(x)
print('-----------------------------------')
# For in
list2 = ['apple', 'banana', 'kiwi']
print(len(list2))
print(range(len(list2)))
for i in range(len(list2)):
    print(list2[i])
print('-----------------------------------')
# While Loop
list3 = ['football', 'cricket', 'rugby']
i = 0
while i < len(list3):
    print(list3[i])
    i = i + 1
print('-----------------------------------')
# Loop Comprehension
list4 = ['football', 'cricket', 'rugby']
[print(x) for x in list4]

