N = int(input())
A = list(map(int, input().split()))
ans = "Yes"
for i in range(N - 1):
    if A[i] >= A[i + 1]:
        ans = "No"
print(ans)
