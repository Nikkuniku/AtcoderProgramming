n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
m_a=[]
for i in range(n):
    m_a.append([a[i],0])
m_b=[]
for i in range(m):
    m_b.append([b[i],1])
    
arr=m_a+m_b
arr=sorted(arr)

ans=10**9
for i in range(n+m-1):
    p=arr[i]
    q=arr[i+1]
    if p[1]!=q[1]:
        ans=min(ans,abs(p[0]-q[0]))
print(ans)