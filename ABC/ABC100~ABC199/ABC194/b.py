N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
# 一人
ans = min([sum(AB[i]) for i in range(N)])
for i in range(N):
    for j in range(i + 1, N):
        tmp1 = max(AB[i][0], AB[j][1])
        tmp2 = max(AB[i][1], AB[j][0])
        ans = min(ans, tmp1, tmp2)
print(ans)
