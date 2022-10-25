N, x, y = map(int, input().split())
A = list(map(int, input().split()))

yoko = []
tate = []
for i in range(1, N):
    if i % 2 == 0:
        yoko.append(A[i])
    else:
        tate.append(A[i])
lim = 10000
dp1 = [[False]*(2*lim + 1) for _ in range(len(yoko)+1)]
dp1[0][lim] = True
dp2 = [[False]*(2*lim + 1) for _ in range(len(tate)+1)]
dp2[0][lim] = True

for i in range(len(yoko)):
    for j in range(2*lim+1):
        if j-yoko[i] >= 0:
            dp1[i+1][j] |= dp1[i][j-yoko[i]]
    for j in range(2*lim, -1, -1):
        if j+yoko[i] <= 2*lim:
            dp1[i+1][j] |= dp1[i][j+yoko[i]]

for i in range(len(tate)):
    for j in range(2*lim+1):
        if j-tate[i] >= 0:
            dp2[i+1][j] |= dp2[i][j-tate[i]]
    for j in range(2*lim, -1, -1):
        if j+tate[i] <= 2*lim:
            dp2[i+1][j] |= dp2[i][j+tate[i]]

dx = x-A[0]+lim
dy = y+lim
# print(yoko)
# print(dp1[len(yoko)])

# print(tate)
# print(dp2[len(tate)])
ans = 'No'
if dp1[len(yoko)][dx] and dp2[len(tate)][dy]:
    ans = 'Yes'
print(ans)
