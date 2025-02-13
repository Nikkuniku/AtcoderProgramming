from collections import defaultdict

N, S = map(int, input().split())
A = list(map(int, input().split()))
M = sum(A)
d = defaultdict(int)
d[0] = 0
S %= M
if S == 0:
    exit(print("Yes"))
B = A + A
cum = 0
ans = "No"
for i in range(2 * N):
    cum += B[i]
    if cum - S in d:
        ans = "Yes"
    d[cum] += 1
print(ans)
