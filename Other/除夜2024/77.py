N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 1
temp = 0
for i in range(N):
    if temp + A[i] <= K:
        temp += A[i]
    else:
        ans += 1
        temp = A[i]
print(ans)
