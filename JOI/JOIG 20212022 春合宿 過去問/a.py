N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda x: x[1])
cumA = [r[0] for r in AB]
cumAB = [sum(AB[-1])]*N
for i in range(1, N):
    cumA[i] = min(cumA[i], cumA[i-1])
    cumAB[N-i-1] = min(sum(AB[N-1-i]), cumAB[N-i])
ans = 1 << 60
for i in range(1, N-1):
    tmp = cumA[i-1]+sum(AB[i])+cumAB[i+1]
    ans = min(ans, tmp)
print(ans)
