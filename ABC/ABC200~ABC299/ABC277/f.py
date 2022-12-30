import itertools
H, W = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(H)]
for i in range(H):
    matrix[i].sort()

matrix_minmax = [[1 << 62, 0] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if matrix[i][j] == 0:
            continue
        matrix_minmax[i][0] = min(matrix_minmax[i][0], matrix[i][j])
        matrix_minmax[i][1] = max(matrix_minmax[i][1], matrix[i][j])
    if matrix_minmax[i] == [1 << 62, 0]:
        matrix_minmax[i] = [0, 0]
matrix_minmax.sort(key=lambda x: x[1])
matrix_minmax.sort(key=lambda x: x[0])


a = list(itertools.chain.from_iterable(matrix_minmax))
b = sorted(a)
ans = 'No'
if a == b:
    ans = 'Yes'
print(ans)
