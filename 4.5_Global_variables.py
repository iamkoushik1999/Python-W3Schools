# x = "Awesome"
#
#
# def function():
#     print("Python is " + x)
#
#
# function()

# -------------------------------------------

# x = "Awesome"
#
#
# def function():
#     x = "crazy"
#     print("Python is " + x)
#
#
# function()
#
# print("Python is " + x)

# -------------------------------------------

# def function():
#     global x
#     x = "Global"
#
#
# function()
#
#
# print(x)

# -------------------------------------------

x = "Awesome"


def function():
    global x
    x = "fantastic"


function()

print(x)
