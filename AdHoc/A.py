input1 = input().split()
candidates = int(input1[0])
power_enemy = int(input1[1])
power_candidates = sorted(list(map(int, input().split())))
available = candidates
win = 0
for i in range(candidates):
    greater = power_candidates.pop()
    needed = (power_enemy // greater) + 1  
    if available >= needed:
        win += 1
        available -= needed
    else:
        break
print(win)