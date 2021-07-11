n=int(input())
a=[]
edge=[set()for _ in range(n)]

for _ in range(n):
    a.append(list(map(int,input().split())))


m=int(input())
for _ in range(m):
    x,y=map(int,input().split())
    x,y=x-1,y-1
    edge[x].add(y)
    edge[y].add(x)


from itertools import permutations

p = permutations([i for i in range(n)])

ans=float('inf')
for c in p:
    tmp=0
    flg=0
    for j in range(n-1):
        if c[j+1] in edge[c[j]]:
            flg+=1
            break
        else:
            tmp+=a[c[j]][j]
    if flg==0:
        tmp+=a[c[n-1]][n-1]
    else:
        continue

    ans = min(tmp,ans)
        
if ans==float('inf'):
    ans=-1
print(ans)
