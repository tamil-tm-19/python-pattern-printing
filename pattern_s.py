"""

         *
        * *
       *   *
      *     *
     *       *
      *     *
       *   *
        * *
         *
        
"""

n = int(input())

for i in range(1, n*2):

    space = n - i if i < 5 else i - n
    star = (2 * i) - 1 if i < 5 else (((n*2) - i) * 2) -1

    for _ in range(space):
        print(" ", end = " ")

    for j in range(star):

        if j == 0 or j == star - 1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()