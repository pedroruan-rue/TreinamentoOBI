simulations = int(input())

for i in range(simulations):
    input1 = input().split()
    n = int(input1[0])
    k = int(input1[1])
    numbers = list(map(int, input().split()))
    size = n*k
    if n % 2 == 0: distance = n-(n//2)+1
    else: distance = n-(n//2)
    curr = size - distance*k
    add = 0
    for i in range(k):
        add += numbers[curr]
        curr += distance
    print(add)