from random import sample

N = int(input())
P = [i + 1 for i in range(N)]
Q = sample(P, N)
ans = 0
for i in range(1 << N):
    tmp = set()
    for j in range(N):
        if i & (1 << j):
            tmp.add(P[j])
            tmp.add(Q[j])
    ans += len(tmp) == N
print(N)
print(*P)
print(*Q)
print("--")
print(ans)
