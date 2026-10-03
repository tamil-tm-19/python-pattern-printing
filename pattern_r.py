"""

     *********
      *     *
       *   *
        * *
         *

"""

n = int(input())

for i in range(n):
    for space in range(i):
        print(" ", end= " ")

    for star in range((n - i) * 2 - 1):

        if i == 0 or star == 0 or star == (n - i) * 2 - 2:
            print("*", end= " ")
        else:
            print(" ", end= " ")
    print()