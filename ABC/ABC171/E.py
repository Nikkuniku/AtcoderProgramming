n=int(input())

a=list(map(int,input().split()))

tmp=[]

for i in range(n):
    if i%2==1:
        continue
    x=a[i]^a[i+1]
    tmp.append(x)

S=0
for j in range(len(tmp)):
    S = S^tmp[j]

ans=[]

for k in range(n):
    p = a[k]^S
    ans.append(p)

print(*ans)