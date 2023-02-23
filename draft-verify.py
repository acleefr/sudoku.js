
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# ask for an array under number, number, number, number format
string = input("Enter 16 numbers separated by commas: ")
a = string.split(",")
a = [int(i) for i in a]

error = "Error: There are duplicates in the same row"
error2 = "Error: There are duplicates in the same column"

if a[0] == a[1] or a[0] == a[2] or a[0] == a[3] or a[1] == a[2] or a[1] == a[3] or a[2] == a[3]:
  print(error)
else:
  if a[4] == a[5] or a[4] == a[6] or a[4] == a[7] or a[5] == a[6] or a[5] == a[7] or a[6] == a[7]:
    print(error)
  else:
    if a[8] == a[9] or a[8] == a[10] or a[8] == a[11] or a[9] == a[10] or a[9] == a[11] or a[10] == a[11]:
      print(error)
    else:
      if a[12] == a[13] or a[12] == a[14] or a[12] == a[15] or a[13] == a[14] or a[13] == a[15] or a[14] == a[15]:
        print(error)
      else:
        if a[0] == a[4] or a[0] == a[8] or a[0] == a[12] or a[4] == a[8] or a[4] == a[12] or a[8] == a[12]:
          print(error2)
        else:
          if a[1] == a[5] or a[1] == a[9] or a[1] == a[13] or a[5] == a[9] or a[5] == a[13] or a[9] == a[13]:
            print(error2)
          else:
            if a[2] == a[6] or a[2] == a[10] or a[2] == a[14] or a[6] == a[10] or a[6] == a[14] or a[10] == a[14]:
              print(error2)
            else:
              if a[3] == a[7] or a[3] == a[11] or a[3] == a[15] or a[7] == a[11] or a[7] == a[15] or a[11] == a[15]:
                print(error2)
              else:
                print("No errors found")

print (a[0], a[1], a[2], a[3])
print (a[4], a[5], a[6], a[7])
print (a[8], a[9], a[10], a[11])
print (a[12], a[13], a[14], a[15])