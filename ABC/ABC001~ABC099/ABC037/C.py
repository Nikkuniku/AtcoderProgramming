n,k=map(int,input().split())
a=list(map(int,input().split()))

ruiseki=[]

prev=0
for i in range(n):
    ruiseki.append(a[i]+prev)
    prev=ruiseki[-1]

ans=0

for j in range(n):
    if j==k-1:
        ans+=ruiseki[j]
    elif j>k-1:
        ans+=ruiseki[j]-ruiseki[j-k]
        
print(ans)