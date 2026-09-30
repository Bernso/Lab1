unit_name = "Level 4 Procedural Programming" # assign variable
print("This unit is: ", unit_name) # print variable
print("The 1st character is:", unit_name[0]) # Display first character using index 0
print("The 4th character is:", unit_name[3]) # 4th character is of index 4 - 1 = 3
print("The 9th character is:", unit_name[8]) # 9th character is of index 9 - 1 = 8

# My edits are below
print("The 2nd character is:", unit_name[1])

print("The first 5 characters are", unit_name[0:5])

# Changing the 5th letter to p
# unit_name[4] = "p" # Python strings are immutable, meaning you cannot edit them and this will not work as a result
unit_name = unit_name[0:4] + 'p' + unit_name[5:len(unit_name)]
print("The 5th character has been changed to a p", unit_name)