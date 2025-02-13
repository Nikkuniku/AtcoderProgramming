from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
S = input()
M = [[] for _ in range(3)]
X = [[] for _ in range(3)]
for i, v in enumerate(A):
    if S[i] == "M":
        M[v].append(i)
    if S[i] == "X":
        X[v].append(i)
ans = 0
for i in range(N):
    if S[i] != "E":
        continue
    for a in range(3):
        for b in range(3):
            Mex = set([0, 1, 2, 3])
            Mex.discard(a)
            Mex.discard(b)
            Mex.discard(A[i])
            V = min(Mex)
            k = bisect_left(M[a], i)
            l = bisect_left(X[b], i)
            ans += k * (len(X[b]) - l) * V
print(ans)
