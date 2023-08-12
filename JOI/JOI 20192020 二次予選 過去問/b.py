N = int(input())
A = []
T = []
for i in range(N):
    a, t = map(int, input().split())
    A.append(a)
    T.append(t)
Tmax = max(T)
ans = 2*max(A)
if ans < max(T):
    for i in range(N-1, -1, -1):
        if T[i] == Tmax:
            break
    ans = Tmax+A[i]
print(ans)
