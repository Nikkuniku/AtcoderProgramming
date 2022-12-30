n=int(input())

d=[0]*(n+1)

for i in range(1,n+1):
    for j in range(i,n+1,i):
        d[j]+=1
        
ans=0
for j in range(n+1):
    ans+=j*d[j]
print(ans)