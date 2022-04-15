n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))

s=[]
for j in range(m):
    p=c[j]
    q=d[j]
    s.append((p,p*q,j))

cum=[set() for _ in range(m)]
for k in range(m-1,-1,-1):
    if k==m-1:
        cum[k].add(s[k][2])
    else:
        cum[k].add(s[k][2])
        cum[k]|=cum[k+1]
edges=[set() for _ in range(n)]
s.sort(key=lambda x:x[1])
s.sort(key=lambda x:x[0])
from bisect import bisect_left

for i in range(n):
    index=bisect_left(s,(a[i],a[i]*b[i],0))
    edges[i]|=cum[index]


# XとYの二部グラフの最大マッチング X={0,1,2,...|X|-1} Y={0,1,2,...,|Y|-1}
#   edges[x]: xとつながるYの頂点のset
#   matched[y]: yとマッチングされたXの頂点(暫定)
 
def dfs(v, visited):
    """
    :param v: X側の未マッチングの頂点の1つ
    :param visited: 空のsetを渡す（外部からの呼び出し時）
    :return: 増大路が見つかればTrue
    """
    for u in edges[v]:
        if u in visited:
            continue
        visited.add(u)
        if matched[u] == -1 or dfs(matched[u], visited):
            matched[u] = v
            return True
    return False
 
matched = [-1] * m
 
# 増大路発見に成功したらTrue(=1)。合計することでマッチング数となる
ans=sum(dfs(s, set()) for s in range(n))
if ans==n:
    ans='Yes'
else:
    ans='No'
print(ans)