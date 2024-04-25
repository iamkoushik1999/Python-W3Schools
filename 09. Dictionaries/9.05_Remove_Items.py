phone = {
    'brand': 'Apple',
    'model': 'Iphone',
    'year': 2024,
    'color': 'white'
}
# Pop removes item with specific key
phone.pop('model')
print(phone)
print('------------------------------------------')
phone = {
    'brand': 'Apple',
    'model': 'Iphone',
    'year': 2024,
    'color': 'white'
}
# popitem removes last inserted item
phone.popitem()
print(phone)
print('------------------------------------------')
phone = {
    'brand': 'Apple',
    'model': 'Iphone',
    'year': 2024,
    'color': 'white'
}
# del removes specific key value
del phone['year']
print(phone)
# del can also delete whole dictionary
del phone

print('-----------------------------------------')
phone = {
    'brand': 'Apple',
    'model': 'Iphone',
    'year': 2024,
    'color': 'white'
}
phone.clear()
print(phone)
