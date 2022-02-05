n,q=map(int,input().split())
snow=[0]*n
for _ in range(q):
    l,r,x=map(int,input().split())
    l,r=l-1,r-1
    snow[l]+=x
    if r<n-1:
        snow[r+1]-=x

for i in range(1,n):
    snow[i]+=snow[i-1]

ans=[]
for i in range(n-1):
    if snow[i]>snow[i+1]:
        ans.append('>')
    elif snow[i]==snow[i+1]:
        ans.append('=')
    else:
        ans.append('<')

answer=''.join(ans)
print(answer)
