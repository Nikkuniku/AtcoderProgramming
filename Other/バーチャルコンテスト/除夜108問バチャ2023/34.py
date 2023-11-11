N, Q = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split()))[1:])
ans = []
for _ in range(Q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    ans.append(A[s][t])
print(*ans, sep="\n")
