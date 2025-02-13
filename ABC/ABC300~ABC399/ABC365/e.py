from collections import Counter

N = int(input())
A = list(map(int, input().split()))
L = 28
B = [[0] * N for _ in range(L)]
for i in range(N):
    for j in range(L):
        if A[i] & (1 << j):
            B[j][i] += 1
ans = 0
for bit in range(L):
    C = [0]
    for i in range(N):
        C.append(C[-1] ^ B[bit][i])
    cnt = Counter(C)
    res = cnt[0] * cnt[1] - sum(B[bit])
    ans += res * (1 << bit)
print(ans)
