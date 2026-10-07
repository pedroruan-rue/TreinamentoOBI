simulations = int(input())
for i in range(simulations):
    pile = input().split()
    n1 = int(pile[0])
    n2 = int(pile[1])
    con1 = (n1 + n2) % 3 == 0
    if con1 and n1 <= n2*2 and n2 <= n1*2:
        print("YES")
    else:
        print("NO")