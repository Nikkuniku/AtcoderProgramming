from math import factorial

used = set()
cnt = 0
L = 1000000
M = 10
ans = []
for i in range(M):
    for j in range(M):
        if j in used:
            continue
        temp = factorial(M - 1 - i)
        if cnt + temp < L:
            cnt += temp
            continue
        ans.append(j)
        used.add(j)
        break
print(*ans, sep="")
