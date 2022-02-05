nimotsu=[]
x,y=map(int,input().split())
n=int(input())
nimotsu.append((x,y,0))
for _ in range(n):
    nimotsu.append(tuple(map(float,input().split())))
n+=1
INF=10**18
dp=[[INF]*n for _ in range(1<<n)]
dp[0][0]=0

def t(weight):
    return (weight+100)/120

for s in range(1<<n):
    w=0
    # 今持っている荷物の重さ
    for j in range(n):
        if not (s>>j)&1:
            w+=nimotsu[j][2]
    for v in range(n):
        if (s>>v)&1:
            continue
        xv,yv,_ =nimotsu[v]
        for u in range(n):
            xu,yu,wu=nimotsu[u]
            dp[s|(1<<v)][v]=min(dp[s|(1<<v)][v],dp[s][u]+t(w)*(abs(xu-xv)+abs(yu-yv))+wu )

ans=dp[(1<<n)-1][0]
print(ans)