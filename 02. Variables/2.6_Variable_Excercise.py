# Create a variable named carname and assign the value Volvo to it.
print('Excercise 1')
carname = 'Volvo'
print(carname)
print('------------------------------------------')
# Create a variable named x and assign the value 50 to it.
print('Excercise 2')
x = 50
print(x)
print('------------------------------------------')
# Display the sum of 5 + 10, using two variables: x and y.
print('Excercise 3')
x = 5
y = 10
print(x + y)
print('------------------------------------------')
# Create a variable called z, assign x + y to it, and display the result.
print('Excercise 4')
x = 5
y = 10
z = x + y
print(z)
print('------------------------------------------')
# Insert the correct syntax to assign values to multiple variables in one line:
print('Excercise 5')
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)
print('------------------------------------------')
# Insert the correct syntax to assign the same value to all three variables in one code line.
print('Excercise 6')
x = y = z = "Orange"
print(x, y, z)
print('------------------------------------------')
# Insert the correct keyword to make the variable x belong to the global scope.
print('Excercise 7')


def function():
    global x
    x = "fantastic"


function()
print(x)
