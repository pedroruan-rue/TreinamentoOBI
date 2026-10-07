simulations = int(input())
for i in range(simulations):
    input1 = input().split()
    y = int(input1[0]) #|
    x = int(input1[1]) #_
    if x >= y:
        if x % 2 == 0:
            n = (x-1) ** 2 + 1
            print(n+y-1)
        else:
            n = x ** 2
            print(n-y+1)
    else:
        if y % 2 == 1:
            n = (y-1) ** 2 + 1
            print(n+x-1)
        else:
            n = y ** 2
            print(n-x+1)
    