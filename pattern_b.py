""" 1 1 1 1
    2 2 2 2
    3 3 3 3
    4 4 4 4  
    5 5 5 5 """

# 5 Row and 5 Column with static numbers

n = int(input())

for i in range(1, n+1):
    for _ in range(n+1):
        print(i, end=" ")
    print()