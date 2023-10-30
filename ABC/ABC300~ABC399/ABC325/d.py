N=int(input())
kukan=[]
for _ in range(N):
    T,D=map(int,input().split())
    kukan.append((T,D))
kukan.sort(key=lambda x:x[0])
kukan.sort(key=lambda x:x[1])
ans=0
now=0
for l,r in kukan:
    if now<=l:
        ans+=1
        now=l+1
    elif now<=r:
        ans+=1
        now+=1
print(ans)