simulations = int(input())

for i in range(simulations):

    length = int(input())
    sequence = list(map(int, input().split()))
    reversed_seq = sequence[::-1]
    total_and = sequence[0]

    for curr in range(length):
        total_and &= sequence[curr]

    print(total_and)