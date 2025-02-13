from itertools import accumulate

N = int(input())
M = 1000000
C = [0] * (M + 2)
for _ in range(N):
    a, b = map(int, input().split())
    C[a] += 1
    C[b + 1] -= 1
print(max(accumulate(C)))
