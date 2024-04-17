# Check if apple is present in the fruits set.
print('Exercise 1')
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")
print('-----------------------------------------------')
# Use the add method to add orange to the fruits set.
print('Exercise 2')
fruits = {"apple", "banana", "cherry"}
fruits.add('orange')
print(fruits)
print('-----------------------------------------------')
# Use the correct method to add multiple items (more_fruits) to the fruits set.
print('Exercise 3')
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)
print('-----------------------------------------------')
# Use the remove method to remove banana from the fruits set.
print('Exercise 4')
fruits = {"apple", "banana", "cherry"}
fruits.remove('banana')
print(fruits)
print('-----------------------------------------------')
# Use the discard method to remove "banana" from the fruits set.
print('Exercise 5')
fruits = {"apple", "banana", "cherry"}
fruits.discard('banana')
print(fruits)
