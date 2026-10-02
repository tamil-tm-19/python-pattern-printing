""" 1
    0 1
    1 0 1
    0 1 0 1
    1 0 1 0 1  """


n = int(input())

for i in range(1, n+1):
    binary_Val = 0 if i % 2 == 0 else 1

    for j in range(1, i+1):
        print(binary_Val,end=" ")
        binary_Val = 0 if binary_Val == 1 else 1
    print()