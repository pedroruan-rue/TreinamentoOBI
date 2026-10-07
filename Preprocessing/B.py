input1 = input().split()
n = int(input1[0])
m = int(input1[1])
alist = list(map(int, input().split()))
dam_lr = [0]
dam_lr_v = 0
dam_rl = [0]
dam_rl_v = 0
for i in range(n-1):
    if alist[i] > alist[i+1]:
        dam_lr_v += alist[i]-alist[i+1]
        dam_lr.append(dam_lr_v)
        dam_rl.append(dam_rl_v)
    else:
        dam_rl_v += alist[i+1]-alist[i]
        dam_rl.append(dam_rl_v)
        dam_lr.append(dam_lr_v)
for i in range(m):
    mission = input().split()
    p0 = int(mission[0])
    pf = int(mission[1])
    if p0 < pf:
        print(dam_lr[pf-1]-dam_lr[p0-1])
    else:
        print(dam_rl[p0-1]-dam_rl[pf-1])