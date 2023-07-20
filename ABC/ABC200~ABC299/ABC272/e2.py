N, M = map(int, input().split())
A = list(map(int, input().split()))
res = [set() for _ in range(M+1)]
for i in range(N):
    l = max(0, -A[i]//(i+1))
    r = max(0, (N-A[i])//(i+1))
    for j in range(l, min(r+1, M+1)):
        res[j].add(A[i]+(i+1)*j)
ans = []
for i in range(1, M+1):
    for j in range(N+1):
        if j not in res[i]:
            ans.append(j)
            break

print(*ans, sep="\n")
