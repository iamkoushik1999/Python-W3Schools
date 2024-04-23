basket1 = ('apple', 'banana', 'cherry')
(red, blue, green) = basket1

print(red)
print(blue)
print(green)
print('------------------------------------------')
# If Variables less that items. give '*'
basket2 = ('apple', 'banana', 'cherry', 'kiwi', 'mango')
(f1, f2, f3, *f4) = basket2

print(f1)
print(f2)
print(f3)
print(f4)
print('------------------------------------------')
(f01, f02, *f03 ,f04) = basket2

print(f01)
print(f02)
print(f03)
print(f04)
