n,m=map(int,input().split())
a=[]
for _ in range(2*n):
    a.append(list(input()))

from collections import deque
rank=deque([])
for i in range(2*n):
    rank.append([i,0])

for j in range(m):

    for i in range(n):
        l=rank.popleft()
        r=rank.popleft()

        te_l=a[l[0]][j]
        te_r=a[r[0]][j]

        if te_l=='G':
            if te_r=='C':
                l[1]+=1
            elif te_r=='P':
                r[1]+=1
        elif te_l=='C':
            if te_r=='G':
                r[1]+=1
            elif te_r=='P':
                l[1]+=1
        elif te_l=='P':
            if te_r=='G':
                l[1]+=1
            elif te_r=='C':
                r[1]+=1
        
        rank.append(l)
        rank.append(r)

    rank=sorted(rank,key=lambda x:x[0])
    rank=deque(sorted(rank,key=lambda x:x[1],reverse=True))

for k in range(2*n):
    print(rank[k][0]+1)