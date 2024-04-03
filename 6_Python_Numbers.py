# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 70
y = 84321384653134
z = -69
print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
a = 99.9
b = 56.58484e00
c = -86.215
print(type(a))
print(type(b))
print(type(c))

# Complex numbers are written with a "j" as the imaginary part:

p = 1+5j
q = 6j
r = -3j
print(type(p))
print(type(q))
print(type(r))

# You can convert from one type to another with the int(), float(), and complex() methods:
m = 10
n = 9.9
o = 4j

f = complex(m)
g = int(n)
h = float(m)
# You cannot convert complex numbers into another number type.
print(f)
print(g)
print(h)
print(type(f))
print(type(g))
print(type(h))

# Random Number
import random

print(random.randrange(1, 10))
