""" *
    **
    ***
    ****
    ***** """


# dynamci row and column

n  = int(input())

"""p = 1 
for i in range(n+1):
    print(p*"*")
    p += 1""" # This is not perfect pattern printing 



for i in range(n+1):
    for j in range(i):
        print("*",end = "")
    print()