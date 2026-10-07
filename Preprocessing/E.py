people = int(input())
directions = " " + input() + " "
east = [0]*(people+1)
west = [0]*(people+1)
for i in range(1,people+1):
    if directions[i] == 'E':
        east[i] = east[i-1] + 1
        west[i] = west[i-1]
    elif directions[i] == 'W':
        west[i] = west[i-1] + 1
        east[i] = east[i-1]
    else:
        east[i] = east[i-1]
        west[i] = west[i-1]
leader = people
for i in range(1,people+1):
    curr  = (east[people]-east[i])+west[i-1]
    if curr < leader:
        leader = curr
print(leader)