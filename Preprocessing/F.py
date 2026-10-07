input1 = input().split()
n = int(input1[0])
q = int(input1[1])
ints = [0] + list(map(int, input().split()))
sums = [0]
for i in range(1,n+1):
    sums.append(sums[i-1] + ints[i])
for i in range(q):
    input2 = input().split()
    a = int(input2[0])
    b = int(input2[1])
    print(sums[b]-sums[a-1])