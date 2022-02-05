from operator import ne


n,k=map(int,input().split())
a=list(map(int,input().split()))

s=set()
s.add(0)
path=[0]
node=[0]*(n+1)
while True:
    p=path[-1]
    node[p]=len(path)
    next=a[p]-1
    if next in s:
        path.append(next)
        break
    else:
        s.add(next)
        path.append(next)

c=len(path)-node[next]
k-=node[next]-1
k%=c
ans=path[node[next]-1+k]+1
print(ans)