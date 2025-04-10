from bisect import bisect_right

M = 1000000
A = [0] * (M + 1)
for i in range(2, M + 1):
    if A[i] != 0:
        continue
    j = i
    while j < M + 1:
        A[j] += 1
        j += i
S = []
for i in range(M + 1):
    if A[i] == 2:
        S.append(i * i)
Q = int(input())
ans = []
for _ in range(Q):
    a = int(input())
    k = bisect_right(S, a)
    ans.append(S[k - 1])
print(*ans, sep="\n")
