# Convert letters to upper case
my_text = "Hello, world"
print(my_text.upper())

# Replace all 'apple' with 'orange'
my_text = "I have an apple, you have an apple"
print(my_text.replace('apple', 'orange'))

# Remove trailing whitespace
my_text = "             I have an apple, you have an apple.                      "
print(my_text.strip())

# Split the string into a list using split
my_text = "Python Java C++"
print(my_text.split(' ')) # split at ever space

# Get the length of the string
print(len(my_text))

# Concatenate strings
part_one = 'hi, '
part_two = 'my name is '
part_three = 'ben'

print(part_one + part_two + part_three)