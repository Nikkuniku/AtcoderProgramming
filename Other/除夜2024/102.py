from collections import defaultdict

d = defaultdict(lambda: -1)
N = int(input())
A = list(map(int, input().split()))
B = []
for i, a in enumerate(A):
    B.append(d[a])
    d[a] = i + 1
print(*B)
