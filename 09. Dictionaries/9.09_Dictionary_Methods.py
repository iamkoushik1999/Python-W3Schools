# The fromkeys() method returns a dictionary with the specified keys and the specified value.
# fromkeys()
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)

# The setdefault() method returns the value of the item with the specified key.
# setdefault()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")
print(x)
