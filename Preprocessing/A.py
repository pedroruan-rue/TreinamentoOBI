simulations = int(input())

for i in range(simulations):
    input1 = input().split()
    n = int(input1[0])
    q = int(input1[1])
    array = list(map(int, input().split()))
    odd = 0
    summ = [0]
    for i in range(n):  
        if array[i] % 2 == 1: odd += 1
        summ.append(odd)
    for i in range(q):
        input2 = list(map(int, input().split()))
        step = odd
        step -= (summ[input2[1]]-summ[input2[0]-1]) 
        if input2[2] % 2 == 1:
            step += 1+input2[1]-input2[0]
        if step % 2 == 1: print("YES")
        else: print("NO")