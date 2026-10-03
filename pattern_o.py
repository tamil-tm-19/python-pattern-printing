"""
        *
       ***
      *****
     *******
    ********* 
     *******
      *****
       ***
        *  
        
"""


n = int(input())

for i in range(n*2):

    change_Space = (n - i) + 1 if i <= 5 else (i - n) + 1
    change_Star = (i*2) - 1 if i <= 5 else (((n*2) - i) * 2) -1

    for _ in range(change_Space):
        print(" ", end=" ")
    for _ in range(change_Star):
        print("*",end=" ")
    print()