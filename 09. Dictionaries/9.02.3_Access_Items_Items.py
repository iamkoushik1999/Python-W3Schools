# Items
# The items() method will return each item in a dictionary, as tuples in a list.
phone = {
    "brand": "Google",
    "model": "Pixel",
    "year": 2024
}
x = phone.items()
print(x)
print('--------------------------------------')
phone = {
    "brand": "Google",
    "model": "Pixel",
    "year": 2024
}
x = phone.items()
print("Before the change")
print(x)
phone['year'] = 2020
print("After the change ")
print(x)
print('--------------------------------------')
phone = {
    "brand": "Google",
    "model": "Pixel",
    "year": 2024
}
x = phone.items()
print("Before the change")
print(x)
phone['color'] = 'white'
print("After the change")
print(x)
print('--------------------------------------')
myDict = {
    "name": "Koushik",
    "age": 24,
    "city": "Kolkata"
}
if 'city' in myDict:
    print("Dictionary has a city as it's key")
