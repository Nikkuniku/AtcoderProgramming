n,m=map(int,input().split())

x=list(map(int,input().split()))

if n>=m:
    print(0)
    exit(0)

if n==1:
    print(max(x) - min(x))
    exit(0)

x= sorted(x)

dist =[0]*(m-1)
for i in range(m-1):
    dist[i] = x[i+1]-x[i]

dist = sorted(dist,reverse=True)

total=max(x)-min(x)
for j in range(n-1):
    total -=dist[j]


print(total)