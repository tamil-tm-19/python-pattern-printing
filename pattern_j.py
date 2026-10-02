""" 

*
**
***
****
*****
****
***
**
*
    
"""

n = int(input())

for i in range((n*2)):
    change_Row = i if i <= 5 else (n*2) - i
    for _ in range(change_Row):
        print("*",end=" ")
    print()