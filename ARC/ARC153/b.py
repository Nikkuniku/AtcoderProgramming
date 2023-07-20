H, W = map(int, input().split())
A = [input()for _ in range(H)]
ans = [['']*W for _ in range(H)]
Q = int(input())
row1 = 0
row2 = 1
col1 = 0
col2 = 1
for _ in range(Q):
    a, b = map(int, input().split())
    # row
    if row1 < a:
        row1 = a-1-row1
    else:
        row1 = H-1-row1+a
    if row2 < a:
        row2 = a-1-row2
    else:
        row2 = H-1-row2+a
    # column
    if col1 < b:
        col1 = b-1-col1
    else:
        col1 = W-1-col1+b
    if col2 < b:
        col2 = b-1-col2
    else:
        col2 = W-1-col2+b
pos_row = [-1]*H
pos_col = [-1]*W
pos_row[0] = row1
pos_row[1] = row2
pos_col[0] = col1
pos_col[1] = col2
for i in range(2, H):
    diff_row = pos_row[i-1]-pos_row[i-2]
    pos_row[i] = (pos_row[i-1]+diff_row) % H
for i in range(2, W):
    diff_col = pos_col[i-1]-pos_col[i-2]
    pos_col[i] = (pos_col[i-1]+diff_col) % W
for i in range(H):
    for j in range(W):
        p = pos_row[i]
        q = pos_col[j]
        ans[p][q] = A[i][j]
for c in ans:
    print(''.join(c))
