a,b,c=map(int,input().split())
ans=-1
for i in range(a,b+1):
    if i%c==0:
        ans=i
print(ans)