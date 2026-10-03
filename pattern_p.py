"""
    * * * * *
     * * * *
      * * *
       * *
        *
        *
       * *
      * * *
     * * * *
    * * * * *
    
"""


n = int(input())

for i in range(n*2):

    space = i if i < 5 else 2 * n - i - 1
    star = n - i if i < 5 else i - n + 1

    for _ in range(space):
        print(" ",end="")
    for _ in range(star):
        print("*",end=" ")
    print()