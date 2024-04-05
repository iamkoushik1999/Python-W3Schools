# age = 25
# txt = "I'm Koushik, I am " + age
# print(txt)

age = 25
txt = "I'm Koushik, I am {}"

print(txt.format(age))

item = 'apple'
quantity = 2
price = 50

order = "I want {} of {} which are ${}"
print(order.format(item,quantity,price))


myOrder = "I want {1} {0} which are ${2}"
print(myOrder.format(item, quantity, price))
