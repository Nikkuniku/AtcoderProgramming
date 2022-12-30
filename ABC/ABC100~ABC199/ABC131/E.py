N, K = map(int, input().split())
cnt = (N-1)*(N-2)//2
# 頂点1を中心にする
edge = []
for i in range(2, N+1):
    edge.append((1, i))
if cnt < K:
    print(-1)
    exit()
if cnt == K:
    print(len(edge))
    for c in edge:
        print(*c)
    exit()
for i in range(2, N+1):
    s = i
    for t in range(s+1, N+1):
        edge.append((s, t))
        cnt -= 1

        if cnt == K:
            break

    if cnt == K:
        break

print(len(edge))
for c in edge:
    print(*c)
