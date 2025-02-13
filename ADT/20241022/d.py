A = list(map(int, input().split()))
ans = 0
for i in range(len(A)):
    ans += A[i] * (1 << i)
print(ans)
