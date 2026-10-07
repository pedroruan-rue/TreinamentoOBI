import math
input1 = input().split()
n = int(input1[0])
k = int(input1[1])
q = int(input1[2])
ind = [0]*200002
pref = [0]*200002
for i in range(n):
    recipe = input().split()
    min_degree = int(recipe[0])
    max_degree = int(recipe[1])
    ind[max_degree+1] -= 1
    ind[min_degree] += 1
for i in range(1,200001):
    ind[i] += ind[i-1]  
    if ind[i] >= k: pref[i] = pref[i-1] + 1
    else: pref[i] = pref[i-1]
for i in range(q):
    quest = input().split()
    print(pref[int(quest[1])] - pref[int(quest[0])-1])