from collections import defaultdict, deque


def swap_row(MATRIX, i):
    res = [a[:] for a in MATRIX]
    res[i], res[i + 1] = res[i + 1], res[i]
    return res


def swap_col(MATRIX, j):
    res = [a[:] for a in MATRIX]
    tmp1 = []
    tmp2 = []
    for i in range(len(res)):
        tmp1.append(res[i][j])
        tmp2.append(res[i][j + 1])
    for i in range(len(res)):
        res[i][j] = tmp2[i]
        res[i][j + 1] = tmp1[i]
    return res


def hash(MATRIX):
    res = []
    for i in range(len(MATRIX)):
        for j in range(len(MATRIX[i])):
            res.append(MATRIX[i][j])
    return tuple(res)


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
d = defaultdict(lambda: -1)
q = deque([A])
d[hash(A)] = 0
while q:
    m = q.popleft()
    hash_m = hash(m)
    # 行
    for i in range(H - 1):
        row = swap_row(m, i)
        hash_row = hash(row)
        if d[hash_row] == -1:
            d[hash_row] = d[hash_m] + 1
            q.append(row)
    for j in range(W - 1):
        col = swap_col(m, j)
        hash_col = hash(col)
        if d[hash_col] == -1:
            d[hash_col] = d[hash_m] + 1
            q.append(col)
print(d[hash(B)])
