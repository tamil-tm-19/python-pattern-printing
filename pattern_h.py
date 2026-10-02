""" 

5 5 5 5 5
4 4 4 4
3 3 3
2 2
1   
    
"""


n = int(input())

"""for i in range(n+1):
    print(str(n-i)*(n-i),end=" ")"""

# or

for i in range(n+1):
    for _ in range(n-i):
        print(n-i ,end=" ") 
    print()