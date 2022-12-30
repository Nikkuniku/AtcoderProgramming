N = int(input())
edge = [[] for _ in range(N)]
for i in range(N-1):
    b = int(input())-1
    edge[b].append(i+1)
salary = [0]*N


def dfs(v, p=-1):
    cnt = 0
    s_max = 0
    s_min = 1 << 30
    for e in edge[v]:
        if e == p:
            continue
        dfs(e, v)
        cnt += 1
        s_max = max(s_max, salary[e])
        s_min = min(s_min, salary[e])

    if cnt == 0:
        salary[v] = 1
    elif cnt == 1:
        salary[v] = 2*s_max+1
    else:
        salary[v] = s_max+s_min+1


dfs(0)
print(salary[0])
