N, K = map(int, input().split())
A = []
pre = -1
for i in range(N):
    T = int(input())
    if i > 0:
        A.append(T-pre)
    pre = T+1
A.sort()
ans = N+sum(A[:N-K])
print(ans)
