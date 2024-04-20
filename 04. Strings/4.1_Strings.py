x1 = "Hello"
x2 = 'Hello'
print(x1, x2)
print('---------------------------------')

a = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Aenean dapibus magna a velit laoreet aliquam. Vestibulum ante ipsum primis
in faucibus orci luctus et ultrices posuere cubilia curae; Morbi quis rhoncus
ante, sed aliquam urna. Ut euismod lorem eu risus interdum rhoncus. '''
print(a)
print('---------------------------------')

a = "Hello"
print(a[2])
print('---------------------------------')

for x in 'banana':
    print(x)
print('---------------------------------')

z = "Hello world"
print(len(z))
print('---------------------------------')

text = "Python is hard"
print(text)
# print("hard" in text)

if "hard" in text:
    print("Word hard is there")

# print("easy" in text)

if "easy" not in text:
    print("Word easy is not there")