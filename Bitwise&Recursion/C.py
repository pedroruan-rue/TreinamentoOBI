simulations = int(input())

for i in range(simulations):

    input1 = list(map(int, input().split()))
    a, b = bin(min(input1)), bin(max(input1))
    sizea = len(str(a))
    if a == b:
        print(0)
    elif str(a) == str(b)[:sizea] and int(str(b)[sizea:]) == 0:

        diff = len(str(b)) - len(str(a))
        if diff % 3 == 0:
            print(diff//3)
        else:
            count = diff // 3
            diff = diff % 3
            if diff % 2 == 0:   
                print(count + diff//2)
            else:
                count += diff // 2
                print(count + diff%2)

    else: 
        print(-1)