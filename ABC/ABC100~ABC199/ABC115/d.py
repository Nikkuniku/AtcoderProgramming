import sys
sys.setrecursionlimit(10**6)
n,X=map(int,input().split())
f=[1]
g=[1]
for i in range(52):
    tmp_f=2*f[-1]+3
    tmp_g=2*g[-1]+1
    f.append(tmp_f)
    g.append(tmp_g)
def re(x) :
    re=1
    if x!='P' and x!='B':
        re=f[x]
    return re
def score(x):
    re=0
    if x=='P' or x==0:
        re=1
    elif x!='B':
        re=g[x]
    return re

ans=0
def dfs(le,i):
    global ans
    burger=['B',le-1,'P',le-1,'B']
    if le==0:
        burger=['P']
    csum=i
    for x in burger:
        csum+=re(x)
        if X>csum:
            ans+=score(x)
            i+=re(x)
        else:
            if x==0 or x=='P':
                ans+=score(x)
            elif x!='B' and x!='P':
                dfs(le-1,i)
            break
            

dfs(n,0)
print(ans)