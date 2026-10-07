simulations = int(input())
for i in range(simulations):
    input1 = input().split()
    n = int(input1[0])
    k = int(input1[1])
    x = int(input1[2])
    min_sum = (1 + k)*k/2
    max_sum = (2*n - k + 1)*k/2
    if x <= max_sum and x >= min_sum:
        print("YES")
    else:
        print("NO")