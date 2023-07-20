N, M = map(int, input().split())
leave = set()
seen = [False]*(N+1)
seen[1] = True
now = 1
parent = [-1]*(N+1)
while 1:
    if now == N:
        print('OK')
        exit()
    info = input().split()
    info = list(map(int, info))
    seen[now] = True
    k = info[0]
    edge = info[1:]
    for e in edge:
        if e == parent[now]:
            continue
        if seen[e]:
            continue
        parent[e] = now
        now = e
        print(e, flush=True)
        break
    else:
        print(parent[now], flush=True)
        now = parent[now]
