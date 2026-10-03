"""
         *
        * *
       *   *
      *     *
     *********
     
"""

n = int(input())

for i in range(1, n + 1):

    for space in range(n - i):
        print(" ", end = " ")

    for star in range(1, i * 2):
        if star == 1 or star == i * 2 - 1 or i == n:
            print("*", end = " ")
        else:
            print(" ", end=" ")
    print()