N = int(input())
A = list(map(int, input().split()))
R = set()
if N <= 2:
    exit(print("Yes"))
ans = "Yes"
for i in range(1, N - 1):
    if A[i - 1] * A[i + 1] != A[i] * A[i]:
        ans = "No"
print(ans)
