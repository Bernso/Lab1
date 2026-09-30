x = "hello"
y = 11
z = 1.1

print(f"The data types of the x, y and z are as follows.\nx: {type(x)}\ny: {type(y)}\nz: {type(z)}")

# Adding an integer and a float always becomes a float, even if it is a whole number
print(type(y + z))

# The type of adding two integers will always be an integer
print(type(y + int(z)))

# The type of a string is a string....
print(type(str(z)))

# "Can we add x and y?" no, strings and integers can not be added
# print(x + y)