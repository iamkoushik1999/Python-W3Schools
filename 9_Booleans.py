print(10 > 9)
print(10 == 9)
print(10 < 9)
print("---------------------------------")

a = 20
b = 5

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
print("---------------------------------")

print(bool("hello"))
print(bool(15))

print("---------------------------------")

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

print("---------------------------------")

print(bool("abc"))
print(bool(123))
print(bool(["apple", "banana"]))

print("---------------------------------")

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print("---------------------------------")


def myfunction():
    return True


if myfunction():
    print("Yes")
else:
    print("No")
