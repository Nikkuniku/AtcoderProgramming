H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
Row = [sum(A[i]) for i in range(H)]
Col = []
for j in range(W):
    tmp = 0
    for i in range(H):
        tmp += A[i][j]
    Col.append(tmp)
T = sum(Row)
ans = 0
for i in range(1, H + 1):
    if T % i != 0:
        continue
    p = T // i
    isOK_Row = True
    tmp = 0
    s = set()
    group = []
    for r in range(H):
        tmp += Row[r]
        s.add(r)
        if tmp == p:
            group.append(s)
            tmp = 0
            s = set()
        elif tmp > p:
            isOK_Row = False
            break
    if not isOK_Row:
        continue
    Col_group = [[0] * W for _ in range(i)]
    for k, g in enumerate(group):
        for s in g:
            for j in range(W):
                Col_group[k][j] += A[s][j]
    for j in range(1, W + 1):
        if i == 1 and j == 1:
            continue
        if T % (i * j) != 0:
            continue
        tmp = [0] * i
        q = T // (i * j)
        isOK_Col = True
        for c in range(W):
            for k in range(i):
                tmp[k] += Col_group[k][c]
                if tmp[k] == q:
                    tmp[k] = 0
                elif tmp[k] > q:
                    isOK_Col = False
                    break
        if not isOK_Col:
            continue
        ans += 1
print(ans)
