n,m=map(int,input().split())
takahashi=[set() for _ in range(n)]
aoki=[set() for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    takahashi[a].add(b)
    takahashi[b].add(a)

for _ in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    aoki[a].add(b)
    aoki[b].add(a)
from itertools import permutations
p = list(permutations(range(n),n))
ans='No'
for q in p:
    flg=0
    for i in range(n):
        for j in range(i+1,n):
            if (j in takahashi[i]) and (q[j] not in aoki[q[i]]):
                flg+=1
            if (j not in takahashi[i]) and (q[j] in aoki[q[i]]):
                flg+=1
    if flg ==0:
        ans='Yes'
        break

print(ans)
