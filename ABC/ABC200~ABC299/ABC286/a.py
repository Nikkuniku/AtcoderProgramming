N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for i in range(N):
    if P-1 <= i <= Q-1:
        ans.append(A[i-(P-1)+R-1])
    elif R-1 <= i <= S-1:
        ans.append(A[i-(R-1)+P-1])
    else:
        ans.append(A[i])
print(*ans)
