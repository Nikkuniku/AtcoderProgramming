N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(1, N):
    if A[i] >= A[i-1]:
        continue
    ans += -(A[i]-A[i-1])
    A[i] += -(A[i]-A[i-1])
print(ans)
