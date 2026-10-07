simulations = int(input())
def look(end, n):
    target = end[1]
    count = 0
    check = 0
    for i in reversed(n):
        if i == target:
            target, check = end[0], check + 1
            if check == 2: break
        else:
            count += 1
    return count


for i in range(simulations):
    n = input()
    m00 = look('00', n)
    m25 = look('25', n)
    m50 = look('50', n)
    m75 = look('75', n)
    print(min([m00, m50, m25, m75]))