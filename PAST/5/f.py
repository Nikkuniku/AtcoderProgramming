N, M = map(int, input().split())
Bann = [list(map(int, input().split())) for _ in range(M)]
ans = 0
for pattern in range(1 << N):
    tmp = 0
    isOK = True
    s = set()
    for a, b, c in Bann:
        a -= 1
        b -= 1
        c -= 1
        cnt = 0
        if pattern & (1 << a):
            cnt += 1
        if pattern & (1 << b):
            cnt += 1
        if pattern & (1 << c):
            cnt += 1
        if cnt == 2:
            if not (pattern & (1 << a)):
                s.add(a)
            if not (pattern & (1 << b)):
                s.add(b)
            if not (pattern & (1 << c)):
                s.add(c)
        if cnt == 3:
            isOK = False
            break
    if isOK:
        ans = max(ans, len(s))
print(ans)
