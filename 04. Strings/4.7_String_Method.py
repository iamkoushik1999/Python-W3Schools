# Upper Case
txt1 = "hello"
print(txt1.capitalize())
print("--------------------------------------")
# Lower Case
txt2 = "WORLD"
print(txt2.casefold())
print("--------------------------------------")
# Count
# Returns the number of times a specified value occurs in a string
txt3 = "I like Football. I like Cricket"
print(txt3.count("like"))
print("--------------------------------------")
# Ends With
txt4 = "Hello World!"
print(txt4.endswith("!"))
print(txt4.endswith("."))
print("--------------------------------------")
# Find
# Index
txt5_1 = "Hello, Welcome to my world"
txt5_2 = "Hello, Welcome to my world"
print(txt5_1.find("Welcome"))
print(txt5_2.index("Welcome"))
print("--------------------------------------")
# Format
txt6 = "My name is {}".format("Koushik")
print(txt6)
print("--------------------------------------")
# Join
myThings = {"car", "phone", "plane"}
x7 = ","
txt7 = x7.join(myThings)
print(txt7)
print("--------------------------------------")
# Replace
txt8 = 'I like mangoes'
x8 = txt8.replace("mangoes", "oranges")
print(x8)
txt8_2 = "I like mangoes, mangoes are my favourite. I like mangoes too"
x8_2 = txt8_2.replace("mangoes", "oranges", 2)
print(x8_2)
print("--------------------------------------")
# Split
txt9_1 = "Banana Orange Apple Mango"
x9_1 = txt9_1.split(" ")
x9_2 = txt9_1.split(" ", 2)
print(x9_1)
print(x9_2)
print("--------------------------------------")
# Starts with
txt10 = "Hello, welcome to Pyhton"
x10 = txt10.startswith("wel", 7, 20)
print(x10)

