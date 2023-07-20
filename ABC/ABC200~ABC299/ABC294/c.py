from collections import defaultdict
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(A+B)
ans_A = []
ans_B = []
d = defaultdict(int)
for i in range(N+M):
    d[C[i]] = i+1

for a in A:
    ans_A.append(d[a])
for b in B:
    ans_B.append(d[b])
print(*ans_A)
print(*ans_B)
