A = list(map(int, input().split()))
ans = 0
for i in range(64):
    ans += A[i] * pow(2, i)
print(ans)
