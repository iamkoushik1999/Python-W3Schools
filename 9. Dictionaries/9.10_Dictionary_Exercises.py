# Use the get method to print the value of the "model" key of the car dictionary.
print("Excercise 1")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
print('----------------------------')
# Change the "year" value from 1964 to 2020.
print("Excercise 2")
car['year'] = 2020
print(car)
print('----------------------------')
# Add the key/value pair "color" : "red" to the car dictionary.
print("Excercise 3")
car["color"] = "red"
print(car)
print('----------------------------')
# Use the pop method to remove "model" from the car dictionary.
print("Excercise 4")
car.pop("model")
print(car)
print('----------------------------')
# Use the clear method to empty the car dictionary.
print("Excercise 5")
car.clear()
print(car)
