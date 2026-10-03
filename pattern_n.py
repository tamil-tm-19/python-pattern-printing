"""

    *********
     *******
      *****
       ***
        *
        
"""

n = int(input())

for i in range(n+1):

    for space in range(i):
        print(" ",end=" ")
    for star in range((n-i)*2 - 1):
            print("*",end=" ")

    print()