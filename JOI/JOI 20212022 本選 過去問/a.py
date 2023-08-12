from bisect import bisect_left
N = int(input())
ans = []
S = []
for _ in range(N):
    a = int(input())
    c = 1
    while a % 2 == 0:
        a //= 2
        c *= 2
    S.append((a, c))
C = [0]
for i in range(N):
    C.append(C[-1]+S[i][1])
Q = int(input())
for i in range(Q):
    x = int(input())
    idx = bisect_left(C, x)-1
    ans.append(S[idx][0])
print(*ans, sep="\n")
