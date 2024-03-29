from itertools import pairwise

N = int(input())
A = list(map(int, input().split()))
ans = 1 << 60
for i in range(1 << (N - 1)):
    tmp = [0]
    for j in range(N - 1):
        if i & (1 << j):
            tmp.append(j + 1)
    tmp.append(N)
    cum = 0
    for a, b in pairwise(tmp):
        tmp_OR = 0
        for m in range(a, b):
            tmp_OR |= A[m]
        cum ^= tmp_OR
    ans = min(ans, cum)
print(ans)
