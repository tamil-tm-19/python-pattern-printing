"""

          *****
         *   *
        *   *
       *   *
      *****
      

"""


n = int(input())

for i in range(1, n + 1):

    for space in range(n - i):
        print(" ", end = " ")

    for star in range(n):
        if i == 1 or i == n or star == 0 or star == n - 1:
            print("*", end = "")

        else:
            print(" ", end = "")
    print()