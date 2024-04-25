family = {
    "child1": {
        "name": "John",
        "age": 24
    },
    "child2": {
        "name": "Jane",
        "age": 22
    },
    "child3": {
        "name": "Joe",
        "age": 20
    }
}
print(family)
print('--------------------------------------')

child1 = {
    "name": "John",
    "age": 24
}
child2 = {
    "name": "Jane",
    "age": 22
}
child3 = {
    "name": "Joe",
    "age": 20
}

myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}
print(myfamily)
print('--------------------------------------')

print(myfamily["child2"]["name"])
