from collections import Counter

N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
ans = -1
temp = -1
for i, v in enumerate(A):
    if C[v] == 1:
        if v > temp:
            ans = max(ans, i + 1)
            temp = v
print(ans)
