# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.

myDict1 = {
    "brand": "Apple",
    "model": "Iphone 15",
    "year": 2024
}

print(myDict1)
# Dictionaries store value in key:value pair
print(myDict1['brand'])
# Length
print(len(myDict1))
# Data Types
# String, Int, Boolean, Lists, Tuples, Sets
myDict2 = {
    "brand": "Apple",
    "model": "Iphone 15",
    "year": 2024,
    "available": True,
    "color": ['Black', "White", 'Pink'],
    "country": ('USA', 'Outside USA'),
    "InSide Box": {'Cable', "Papers"}
}
print(myDict2)
# Types
print(type(myDict2))
# Dict Constrcuctor
# Notice its '=' not ':'
myDict = dict(name="John", age=24, country="India")
print(myDict)
