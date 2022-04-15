w,n=map(int,input().split())
spice=[]
for _ in range(n):
    spice.append(tuple(map(int,input().split())))
p=1
while w+1>p:
    p*=2
data = [0]*(2*p-1)
INF=10**8
def update(k,x):
    k+=p-1
    data[k]=x
    while k>0:
        k=(k-1)//2
        data[k]=max(data[2*k +1],data[2*k +2])
def query(a,b):
    return query_sub(a,b,0,0,w+1)
def query_sub(a,b,k,l,r):
    # //対象外
    if r<=a or b<=l:return 0
    # 完全被覆
    if a<=l and r<=b:return data[k]
    # 一部被覆
    vl = query_sub(a,b,2*k +1,l,(l+r)//2)
    vr = query_sub(a,b,2*k +2,(l+r)//2,r)
    return max(vl,vr)

dp=[[-INF]*(w+1) for _ in range(n+1)]
dp[0][0]=0
update(0,0)

for i in range(n):
    l,r,v=spice[i]
    for j in range(w+1):
        dp[i+1][j]=dp[i][j]

    for j in range(w+1):
        cr=max(0,j-r)
        cl=max(0,j-l)
        if cr==cl:continue
        maxvalue=query(cr,cl)
        if maxvalue!=-INF:
            dp[i+1][j]=max(maxvalue+v,dp[i+1][j])
    
    for j in range(w+1):
        update(j,dp[i+1][j])

print(dp[n][w],sep="\n")
