from collections import Counter

N = int(input())
S = input()
P = [0] * 10
for s in S:
    P[int(s)] += 1

L = 4000000
ans = 0
for i in range(L + 1):
    s = i**2
    T = str(s)
    tmp = [0] * 10
    for t in T:
        tmp[int(t)] += 1
    isOK = True
    for j in range(1, 10):
        if tmp[j] != P[j]:
            isOK = False
            break
    if P[0] < tmp[0]:
        isOK = False
    if not isOK:
        continue
    ans += 1
print(ans)
