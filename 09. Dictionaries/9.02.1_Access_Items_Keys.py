# Keys
# The keys() method will return a list of all the keys in the dictionary.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)
print('--------------------------------------')
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print("Before adding keys")
print(x)
car['color'] = 'white'
print("After adding keys")
print(x)
