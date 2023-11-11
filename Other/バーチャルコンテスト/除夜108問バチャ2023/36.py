N, M = map(int, input().split())
kekka = [[0]*N for _ in range(N)]
for _ in range(M):
    X = list(map(int, input().split()))[1:]
    for i in range(len(X)):
        for j in range(i+1, len(X)):
            kekka[X[i]-1][X[j]-1] = 1
            kekka[X[j]-1][X[i]-1] = 1

ans = 'Yes'
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if kekka[i][j] == 0:
            ans = 'No'
print(ans)
