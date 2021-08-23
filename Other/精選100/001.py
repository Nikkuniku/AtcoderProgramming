N=[]
X=[]
cnt=0
while True:
    n,x=map(int,input().split())
    if n==0 and x==0:
        break
    N.append(n)
    X.append(x)
    cnt+=1

for i in range(cnt):
    m=N[i]
    y=X[i]
    ans=0
    for j in range(1,m-1):
        for k in range(j+1,m):
            for l in range(k+1,m+1):
                if j+k+l==y:
                    ans+=1

    print(ans)