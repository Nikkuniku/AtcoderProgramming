N = 15
ans = [[-1]*(N+10) for _ in range(N+10)]
ans[0][0] = 0
ans[0][1] = 0
ans[1][0] = 0
ans[1][1] = 0


def rec(a, b):
    CanWin = False
    for i in range(1, (a//2)+1):
        if ans[a-2*i][b+i] == -1:
            if rec(a-2*i, b+i) == 0:
                CanWin = True
        else:
            if ans[a-2*i][b+i] == 0:
                CanWin = True
    for j in range(1, (b//2)+1):
        if ans[a+j][b-2*j] == -1:
            if rec(a+j, b-2*j) == 0:
                CanWin = True
        else:
            if ans[a+j][b-2*j] == 0:
                CanWin = True
    if CanWin:
        ans[a][b] = 1
    else:
        ans[a][b] = 0
    return ans[a][b]


for i in range(2, N):
    for j in range(2, N):
        rec(i, j)
for c in ans:
    print(*c, sep="\t")

X, Y = map(int, input().split())
ans = 'Alice'
if abs(X-Y) <= 1:
    ans = 'Brown'
print(ans)
