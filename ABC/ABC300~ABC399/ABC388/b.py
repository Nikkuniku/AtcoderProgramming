N, D = map(int, input().split())
ans = []
Snakes = [list(map(int, input().split())) for _ in range(N)]
for k in range(1, D + 1):
    temp = -1
    for t, l in Snakes:
        temp = max(temp, t * (l + k))
    ans.append(temp)
print(*ans, sep="\n")
