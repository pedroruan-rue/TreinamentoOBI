s = input() + " "
pref = [0]*(len(s))
m = int(input())
for i in range(0,len(s)-1):
    if s[i] == s[i+1]:
        pref[i+1] = pref[i] + 1
    else:
        pref[i+1] = pref[i]
for i in range(m):
    query = input().split()
    l = int(query[0])
    r = int(query[1])
    print(pref[r-1]-pref[l-1])