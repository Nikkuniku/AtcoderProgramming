N, C = map(int, input().split())
lim = 100001
rec = [[0]*(lim+5) for _ in range(C)]
for _ in range(N):
    s, t, c = map(int, input().split())
    rec[c-1][s] += 1
    rec[c-1][t+1] -= 1

for c in range(C):
    for i in range(lim+4):
        rec[c][i+1] += rec[c][i]
        if rec[c][i+1] == 2:
            rec[c][i+1] = 1

ans = 0
for i in range(lim+5):
    tmp = 0
    for c in range(C):
        tmp += rec[c][i]
    ans = max(ans, tmp)
print(ans)
