N, K = map(int, input().split())
A = list(map(int, input().split()))
tmp = 0
ans = 1
for i in range(N):
    if tmp + A[i] <= K:
        tmp += A[i]
    else:
        tmp = A[i]
        ans += 1
print(ans)
