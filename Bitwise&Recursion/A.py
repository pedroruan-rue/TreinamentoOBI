simulations = int(input())

for i in range(simulations):
    input1 = input().split()
    a, b = int(input1[0]), int(input1[1])
    print(a^b)