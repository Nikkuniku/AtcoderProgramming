A = [list(map(int, input().split())) for _ in range(9)]
# 行チェック
N = 9
ans = "Yes"
for i in range(N):
    if len(set(A[i])) != 9:
        ans = "No"
# 列チェック
for j in range(N):
    tmp = set()
    for i in range(N):
        tmp.add(A[i][j])
    if len(tmp) != 9:
        ans = "No"
for i in range(N):
    if i % 3 != 0:
        continue
    for j in range(N):
        if j % 3 != 0:
            continue
        tmp = set()
        for k in range(3):
            for m in range(3):
                tmp.add(A[i + k][j + m])
        if len(tmp) != 9:
            ans = "No"
print(ans)
