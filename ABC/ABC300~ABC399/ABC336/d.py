N = int(input())
A = list(map(int, input().split()))
dp_L = [1]
dp_R = [1]
for i in range(1, N):
    if dp_L[-1] < A[i]:
        dp_L.append(dp_L[-1] + 1)
    else:
        dp_L.append(A[i])
for i in range(N - 2, -1, -1):
    if A[i] > dp_R[-1]:
        dp_R.append(dp_R[-1] + 1)
    else:
        dp_R.append(A[i])
dp_R = dp_R[::-1]
ans = 1
for i in range(1, N - 1):
    l = dp_L[i - 1]
    r = dp_R[i + 1]
    tmp = min(min(l, r) + 1, A[i])
    ans = max(ans, tmp)
print(ans)
