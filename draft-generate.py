import random

# define the array
a = [random.randint(1, 4) for i in range(16)]
print("loading ...")
i = 0

# generate the sudoku array
# check if there are any duplicates in the same row
while a[0] == a[1] or a[0] == a[2] or a[0] == a[3] or a[1] == a[2] or a[1] == a[3] or a[2] == a[3]:
    a = [random.randint(1, 4) for i in range(16)]

    while a[4] == a[5] or a[4] == a[6] or a[4] == a[7] or a[5] == a[6] or a[5] == a[7] or a[6] == a[7]:
      a = [random.randint(1, 4) for i in range(16)]

      while a[8] == a[9] or a[8] == a[10] or a[8] == a[11] or a[9] == a[10] or a[9] == a[11] or a[10] == a[11]:
        a = [random.randint(1, 4) for i in range(16)]

        while a[12] == a[13] or a[12] == a[14] or a[12] == a[15] or a[13] == a[14] or a[13] == a[15] or a[14] == a[15]:
          a = [random.randint(1, 4) for i in range(16)]

          # check if there are any duplicates in the same column
          while a[0] == a[4] or a[0] == a[8] or a[0] == a[12] or a[4] == a[8] or a[4] == a[12] or a[8] == a[12]:
            a = [random.randint(1, 4) for i in range(16)]

            while a[1] == a[5] or a[1] == a[9] or a[1] == a[13] or a[5] == a[9] or a[5] == a[13] or a[9] == a[13]:
              a = [random.randint(1, 4) for i in range(16)]

              while a[2] == a[6] or a[2] == a[10] or a[2] == a[14] or a[6] == a[10] or a[6] == a[14] or a[10] == a[14]:
                a = [random.randint(1, 4) for i in range(16)]

                while a[3] == a[7] or a[3] == a[11] or a[3] == a[15] or a[7] == a[11] or a[7] == a[15] or a[11] == a[15]:
                  a = [random.randint(1, 4) for i in range(16)]

print("hiding some numbers ...")

print(a)

# randomly  give "x" to 3 numbers in the array
a[random.randint(0, 15)] = "x"
a[random.randint(0, 15)] = "x"
a[random.randint(0, 15)] = "x"

# print the array
print(a[0], a[1], a[2], a[3])
print(a[4], a[5], a[6], a[7])
print(a[8], a[9], a[10], a[11])
print(a[12], a[13], a[14], a[15])


