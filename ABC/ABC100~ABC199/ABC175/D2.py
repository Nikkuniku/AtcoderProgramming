N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
INF = float('inf')
ans = []
for s in range(N):
    score = -INF
    tmp = 0
    cycle = 0
    cyclelen = 0
    cnt = 0
    v = s
    while 1:
        v = P[v]-1
        tmp += C[v]
        cycle += C[v]
        score = max(score, tmp)
        cyclelen += 1
        cnt += 1
        if v == s:
            break
    if cycle > 0:
        tmp += cycle*((K-cnt)//cyclelen)
        cnt += cyclelen*((K-cnt)//cyclelen)
        score = max(score, tmp)
        for _ in range(K-cnt):
            nextv = P[v]-1
            tmp += C[nextv]
            score = max(score, tmp)
            v = nextv
    ans.append(score)

print(max(ans))
