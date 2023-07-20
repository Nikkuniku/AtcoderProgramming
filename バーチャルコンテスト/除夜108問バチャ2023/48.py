N = int(input())
user = [list(input().split()) for _ in range(N)]
isOK = [True]*N
for i in range(N):
    flg = [True, True]
    for k in range(2):
        s = user[i][k]
        for j in range(N):
            if j == i:
                continue
            if s in user[j]:
                flg[k] = False
    if flg == [False, False]:
        isOK[i] = False
ans = 'Yes'
if isOK != [True]*N:
    ans = 'No'
print(ans)
