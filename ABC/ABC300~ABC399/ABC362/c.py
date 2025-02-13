N = int(input())
P = []
for _ in range(N):
    LR = list(map(int, input().split()))
    P.append(LR)
ans = "Yes"
L = [P[i][0] for i in range(N)]
R = [P[i][1] for i in range(N)]
if not (sum(L) <= 0 and sum(R) >= 0):
    exit(print("No"))
X = R[:]
S = sum(X)
for i in range(N):
    xi = X[i]
    if S > 0:
        diff = xi - L[i]
        if diff < S:
            X[i] = L[i]
            S -= diff
        else:
            X[i] -= S
            S = 0
print(ans)
print(*X)
