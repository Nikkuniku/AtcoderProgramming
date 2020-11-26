n,w=map(int,input().split())

a=[0]*(2*(10**5)+1)
for _ in range(n):
    s,t,p=map(int,input().split())
    a[s]+=p
    a[t]-=p


for i in range(len(a)):
    if i>0:
        a[i]+=a[i-1]


ans='Yes'
for j in range(len(a)):
    if a[j]>w:
        ans='No'
        break

# print(a[:10])
print(ans)