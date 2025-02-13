from collections import Counter

N, X = map(int, input().split())
A = list(map(int, input().split()))
C = Counter(A)
ans = "No"
for a in A:
    if C[X + a] > 0:
        ans = "Yes"
print(ans)
