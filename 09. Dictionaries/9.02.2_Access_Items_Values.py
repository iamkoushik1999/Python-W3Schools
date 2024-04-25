# Values
# The values() method will return a list of all the values in the dictionary.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}
x = car.values()
print(x)
print('--------------------------------------')
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}
x = car.values()
print("Before the change")
print(x)
car['year'] = 2020
print("After the change ")
print(x)
print('--------------------------------------')
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print("Before the change")
print(x)
car['color'] = 'white'
print("After the change")
print(x)
