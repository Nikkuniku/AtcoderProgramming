def check(k, P, Monsters):
    C = [Monsters[i][1] - k * Monsters[i][0] for i in range(len(Monsters))]
    C.sort()
    R = 0
    cnt = 0
    if P:
        R += P[0][1] - k * P[0][0]
        cnt += 1
    while cnt < 5:
        R += C.pop()
        cnt += 1
    return R >= 0


N, M = map(int, input().split())
Monster = [list(map(int, input().split())) for _ in range(N)]
SubMonster = [list(map(int, input().split())) for _ in range(M)]
ans = -1
for i in range(M + 1):
    if i == M:
        Select = []
    else:
        Select = [SubMonster[i]]
    l = 0
    r = 1 << 60
    for _ in range(200):
        mid = (l + r) / 2
        if check(mid, Select, Monster):
            l = mid
        else:
            r = mid
    ans = max(ans, l)
print(ans)
