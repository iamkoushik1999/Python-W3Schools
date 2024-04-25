phone = {
    'brand': 'Apple',
    'model': 'Iphone',
    'year': 2024,
    'color': 'white'
}
for x in phone:
    print(x)
print('-------------------------------------')
for x in phone:
    print(phone[x])
print('-------------------------------------')
for x in phone.values():
    print(x)
print('-------------------------------------')
for x in phone.keys():
    print(x)
print('-------------------------------------')
for x, y in phone.items():
    print(x, y)
