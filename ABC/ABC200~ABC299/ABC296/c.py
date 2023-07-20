from collections import Counter
N, X = map(int, input().split())
A = list(map(int, input().split()))
C = Counter(A)
ans = 'No'
for a in A:
    b = a-X
    if C[b] >= 1:
        ans = 'Yes'
print(ans)
