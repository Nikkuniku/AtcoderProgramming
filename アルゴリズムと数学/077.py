n=int(input())
X,Y=[],[]
for _ in range(n):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)

X=sorted(X)
Y=sorted(Y)
ans=0

for k in range(1,n,1):
    p=X[k]-X[k-1]
    q=Y[k]-Y[k-1]
    ans+=p*(n-k)*k
    ans+=q*(n-k)*k
print(ans)