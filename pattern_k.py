"""

    *
   **
  ***
 ****
*****
 
"""


n = int(input())

for i in range(n+1):
    for space in range(n-i+1):
        print(" ",end=" ")

    for star in range(i):
        print("*", end=" ")
    print()