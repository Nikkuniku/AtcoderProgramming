N, M, T, X, Y = map(int, input().split())
penalty = [[0]*(M+1) for _ in range(N+1)]
opened = [[0]*(M+1) for _ in range(N+1)]
INF = 1 << 60
accepted = [[INF]*(M+1) for _ in range(N+1)]
ans = []
Points = [int(input()) for _ in range(M)]
for _ in range(Y):
    t, i, j, status = input().split()
    t = int(t)
    i = int(i)
    j = int(j)
    if status == 'open':
        opened[i][j] = t
    elif status == 'correct':
        accepted[i][j] = t
    elif status == 'incorrect':
        penalty[i][j] += 1
for i in range(1, N+1):
    score = 0
    for j in range(1, M+1):
        if accepted[i][j] == INF:
            continue
        tmp = Points[j-1]-(accepted[i][j]-opened[i][j])-penalty[i][j]*120
        score += max(tmp, X)
    ans.append(score)
print(*ans, sep="\n")
