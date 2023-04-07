
# ask for an array under number, 'string', number format
string = input("Enter 16 numbers separated by commas: ")
# remove the ' ' from the string
string = string.replace("'", "")
# replace X by 0
a = string.split(",")
a = [int(i) for i in a]

# remplace the 0 by the right sudoku number 
# (the one that is not in the same row or column)
# and print the sudoku
for i in range(0, 16):
  if a[i] == 0:
    a[i] = 10 - a[i-1] - a[i-4]
  print(a[i], end=" ")
  if i == 3 or i == 7 or i == 11 or i == 15:
    print()

# print the sudoku in a list
print(a)

