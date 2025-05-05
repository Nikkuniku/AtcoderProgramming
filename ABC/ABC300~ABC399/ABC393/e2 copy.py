N, K = map(int, input().split())
A = list(map(int, input().split()))
L = 10**6
s = [0] * (L + 1)
for a in A:
    s[a] += 1
for g in range(2, L + 1):
    j = g
    temp = 0
    while j < L + 1:
        temp += s[j]
        j += g
    s[g] = temp
t = [1] * (L + 1)
for g in range(2, L + 1):
    j = g
    if s[g] < K:
        continue
    while j < L + 1:
        t[j] = g
        j += g
ans = []
for a in A:
    ans.append(t[a])
print(*ans, sep="\n")
