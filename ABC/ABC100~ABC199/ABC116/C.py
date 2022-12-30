n=int(input())
h=list(map(int,input().split()))



under=min(h)
for i in range(n):
    h[i]-=under
ans=under

while True:
    if max(h)==0:
        break
    i=0
    while i<n:
        if h[i]==0:
            i+=1
        else:
            ans+=1
            while i<n and h[i]>0:
                h[i]-=1
                i+=1
                
print(ans)