n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

d={}

for i in range(n):
    index =c[i]-1
    b_i = b[index]
    if b_i in d:
        d[b_i]+=1
    else:
        d[b_i]=1

ans=0
for j in range(n):
    if a[j] in d:
        ans+=d[a[j]]

print(ans)