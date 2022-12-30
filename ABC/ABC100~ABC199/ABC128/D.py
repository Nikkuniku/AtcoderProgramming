N, K = map(int, input().split())
V = list(map(int, input().split()))
rev_V = list(reversed(V))

Left = [[0]*(K+1) for _ in range(N)]
Right = [[0]*(K+1) for _ in range(N)]
if N == 1:
    print(max(max(V), 0))
    exit()
# 左から
tmp = []
for i in range(N):
    tmp.append(V[i])
    # 何回まで操作できるか
    for k in range(K+1):
        for j in range(k+1):
            value = 0
            tmp_j = sorted(tmp[:j], reverse=True)
            nokori = k-len(tmp_j)
            while tmp_j and nokori > 0:
                if tmp_j[-1] < 0:
                    tmp_j.pop()
                    nokori -= 1
                else:
                    break
            Left[i][k] = max(sum(tmp_j), Left[i][k])
# 右から
tmp = []
for i in range(N):
    tmp.append(rev_V[i])
    # 何回まで操作できるか
    for k in range(K+1):
        for j in range(k+1):
            value = 0
            tmp_j = sorted(tmp[:j], reverse=True)
            nokori = k-len(tmp_j)
            while tmp_j and nokori > 0:
                if tmp_j[-1] < 0:
                    tmp_j.pop()
                    nokori -= 1
                else:
                    break
            Right[i][k] = max(sum(tmp_j), Right[i][k])

ans = 0
for i in range(N):
    for j in range(N):
        if i+j > N-2:
            continue
        for k in range(K+1):
            tmp = Left[i][k]+Right[j][K-k]
            ans = max(ans, tmp)
print(ans)
