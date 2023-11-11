N, Q = map(int, input().split())
S = input()
ans = []
rot = 0
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        rot += x
    else:
        ans.append(S[(x-1-rot) % N])
print(*ans, sep="\n")
